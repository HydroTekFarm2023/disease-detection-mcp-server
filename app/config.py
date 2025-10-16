import os

AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
DYNAMO_TABLE_NAME = os.getenv("DYNAMO_TABLE_NAME")
MODEL_ID = "us.mistral.pixtral-large-2502-v1:0"
