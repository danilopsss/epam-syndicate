import os
import json
import uuid
import boto3 as aws
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('ApiHandler-handler')


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        print(event, context)
        region = os.environ.get("REGION", "eu-central-1")
        table_name = os.environ.get('TABLE_NAME', "Events")
        data = {
            'id': str(uuid.uuid4()),
            'event': str(event)
        }

        dynamodb = aws.resource('dynamodb',  region_name=region)
        table = dynamodb.Table(table_name)
        
        response = table.put_item(Item=data)
        
        return {
            "statusCode": 201,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response, indent=4)
         }
    

HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
