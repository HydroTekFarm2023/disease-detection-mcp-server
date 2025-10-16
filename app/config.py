import os
from dotenv import load_dotenv
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
DYNAMO_TABLE_NAME = os.getenv("DYNAMO_TABLE_NAME")
MODEL_ID = "us.mistral.pixtral-large-2502-v1:0"
