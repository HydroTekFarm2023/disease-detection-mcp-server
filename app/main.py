import json
import base64
import uuid
from datetime import datetime
from decimal import Decimal
from mcp.server.fastmcp import FastMCP
from app.config import DYNAMO_TABLE_NAME, MODEL_ID, S3_BUCKET
from app.aws_clients import bedrock_client, dynamodb, s3_client
from app.prompt_text import PROMPT_TEXT

# Initialize FastMCP server
mcp = FastMCP("disease-detection-mcp")


@mcp.tool()
async def detect_disease(image_base64: str, prompt: str | None = None) -> dict:
    """Detects plant disease using Pixtral model and stores results in DynamoDB.

    Args:
        image_base64: Base64 encoded image string (no S3 involved).
        prompt: Optional user prompt; appended to the system prompt.
    """
    # Generate image key and upload to S3
    image_key = f"uploads/{uuid.uuid4()}.png"
    image_bytes = base64.b64decode(image_base64)
    s3_client.put_object(Bucket=S3_BUCKET, Key=image_key, Body=image_bytes)
    print(f"✅ Uploaded image to s3://{S3_BUCKET}/{image_key}")

    full_prompt = PROMPT_TEXT
    if prompt:
        full_prompt += f"\nUser note: {prompt}"

    # Build the Pixtral request
    """
    Note: This is a schema for Pixtral Model, The request body schema changes for other Bedrock models.
    Later on a helper function will be created to handle the request body schema for other Bedrock models.
    """
    request_body = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": full_prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image_base64}"},
                    },
                ],
            }
        ],
        "max_tokens": 1000,
    }

    # Call Bedrock
    response = bedrock_client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(request_body),
    )

    raw_response = json.loads(response["body"].read())
    content = raw_response["choices"][0]["message"]["content"]

    # Parse JSON safely
    try:
        json_str = content.strip("```json\n").rstrip("```").strip()
        result = json.loads(json_str)
    except Exception:
        result = {
            "disease_detected": "ParsingError",
            "health_status": "unknown",
            "fungal_status": "unknown",
            "plant_part": "unknown",
            "recommendations": ["Failed to parse model output."],
            "confidence_score": 0.0,
        }

    # Save to DynamoDB
    table = dynamodb.Table(DYNAMO_TABLE_NAME)
    item = {
        "id": str(uuid.uuid4()),
        "image_key": image_key,
        "disease_detected": result.get("disease_detected", "Unknown"),
        "fungal_status": result.get("fungal_status", "Unknown"),
        "health_status": result.get("health_status", "Unknown"),
        "plant_part": result.get("plant_part", "Unknown"),
        "recommendations": result.get("recommendations", []),
        "confidence_score": Decimal(str(result.get("confidence_score", 0.0))),
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

    table.put_item(Item=item)
    print("✅ Saved to DynamoDB")

    # Return result to client
    return result


if __name__ == "__main__":
    mcp.run()
