# test modules
from unittest import TestCase

# target test files and modules
import json
import lambda_function

# test inputs
event = {}
context = {}

class TestApp(TestCase):
  def test_get_book(self):
    assert lambda_function.lambda_handler(event, context) == {
      'statusCode': 200,
      'body': json.dumps('Hello from Lambda!')
    }