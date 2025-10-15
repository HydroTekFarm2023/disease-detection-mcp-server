import os

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
DYNAMO_TABLE_NAME = os.getenv("DYNAMO_TABLE_NAME", "DIAGNOSIS_TABLE_NAME")
MODEL_ID = "us.mistral.pixtral-large-2502-v1:0"
