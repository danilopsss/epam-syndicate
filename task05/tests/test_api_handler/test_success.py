import os
# from moto import dynamodb
from tests.test_api_handler import ApiHandlerLambdaTestCase


class TestSuccess(ApiHandlerLambdaTestCase):
    def setUp(self) -> None:
        os.environ.setdefault("TABLE_NAME", "my_table")   
        return super().setUp()

    # @dynamodb
    def test_success(self):
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), 200)

