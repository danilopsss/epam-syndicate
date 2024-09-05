import json
from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "statusCode": 404,
                'message':  'Bad request syntax or unsupported method. Request path: None. '
                        'HTTP method: None'})
            }
            
        )

