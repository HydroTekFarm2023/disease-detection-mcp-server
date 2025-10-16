import boto3
from .config import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

bedrock_client = session.client("bedrock-runtime")
s3_client = session.client("s3")
dynamodb = session.resource("dynamodb")
