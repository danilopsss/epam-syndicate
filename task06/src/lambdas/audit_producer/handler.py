import os
import uuid
import json
import boto3 as aws
from datetime import datetime
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('AuditProducer-handler')


class AuditProducer(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        region = os.environ.get("REGION", "eu-central-1")
        table_name = os.environ.get('TABLE_NAME')
        data = {
            "id": str(uuid.uuid4()), 
            "itemKey": "CACHE_TTL_SEC",
            "modificationTime": datetime.now().isoformat(),
            "updatedAttribute": "value",
            "oldValue": event,
            "newValue": {"key": "CACHE_TTL_SEC", "value": 3600}
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
    

HANDLER = AuditProducer()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
