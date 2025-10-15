from mcp.server.fastmcp import FastMCP
import json
from app.config import MODEL_ID
from app.bedrock_client import get_bedrock_client
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
    bedrock = get_bedrock_client()
    full_prompt = PROMPT_TEXT
    if prompt:
        full_prompt += f"\nUser note: {prompt}"

    # Build the Pixtral request
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
    response = bedrock.invoke_model(
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
    # item = save_result_to_dynamo(result)

    # return {"result": result, "saved_item": item}


if __name__ == "__main__":
    mcp.run()
