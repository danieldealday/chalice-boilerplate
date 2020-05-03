import os
import json
import logging

import boto3
from chalice import (
  BadRequestError,
  ChaliceViewError,
  NotFoundError,
  Response,
  UnauthorizedError
)

root = logging.getLogger()
root.setLevel('INFO')
logger = logging.getLogger()
if logger.handlers:
    HANDLER = logger.handlers[0]
    HANDLER.setFormatter(logging.Formatter("%(message)s"))

class DateSchema:
  def __init__(self, attr1, attr2):
    self.attr1 = attr1
    self.attr2 = attr2

def main():
  return Response(
    status_code=200,
    body={
      "hello": "world"
    }
  )