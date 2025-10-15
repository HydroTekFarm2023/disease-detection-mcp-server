import os

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET = os.getenv("S3_BUCKET", "hydroponic123")
DYNAMO_TABLE_NAME = os.getenv("DYNAMO_TABLE_NAME", "DIAGNOSIS_TABLE_NAME")
MODEL_ID = "us.mistral.pixtral-large-2502-v1:0"
