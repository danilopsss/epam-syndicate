import json
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
from commons.exception import ApplicationException

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def get_path(self, event):
        return event.get('rawPath')
    
    def get_method(self, event):
        return (
            event
            .get("requestContext", {})
            .get("http", {})
            .get("method")
        )

    def valid_request(self, event) -> dict:
        is_method_allowed = self.get_method(event) == "GET"
        is_path_valid = self.get_path(event) == "/hello"
        return all([is_method_allowed, is_path_valid])
        
    def handle_request(self, event, context):
        response = {
            "statusCode": 0,
            "message": ""
        }
        if self.valid_request(event=event):
            response["statusCode"] = 200
            response["message"] = "Hello from Lambda"
        else:
            response["statusCode"] = 404
            response["message"] = (
                "Bad request syntax or unsupported method. "
                f"Request path: {self.get_path(event)}. "
                f"HTTP method: {self.get_method(event)}"
            )

        return {
            "statusCode": response.get("statusCode"),
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response)
        }
    
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
