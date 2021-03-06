# Chalice Boilerplate
This boilerplate project contains examples for testing for non-API lambda functions and testing for Chalice applications at both unit and integration level.

## Quick Start
```bash
# globally install modules for testing libraries, Chalice, and boto3
$ pip install -Ur extra-requirements.txt
$ cd api
$ virtualenv env
$ source env/Scripts/activate
# locally install modules to virtual environment for project
$ pip install -Ur requirements.txt
```

### Update Chalice Project Name for Deploys
- `/api/.chalice/config.json`
  - "app_name": "CLIENT_PROJECT_NAME" ~~"app_name": "CLIENT_PROJECT_NAME"~~
```json
{
  "version": "2.0",
  "app_name": "CLIENT_PROJECT_NAME",
  # ...
}
```

- `/api/app.py`

```python
from chalice import Chalice, Response

app = Chalice(app_name='CLIENT_PROJECT_NAME') # app = Chalice(app_name='app')
app.debug = True # ! remove in prod
# ...
```

## Chalice Testing

Testing the API create by Chalice requires that you activate the specific virtual environment for the application.

```bash
$ cd api
$ source env/Scripts/activate
# run unit tests
$ pytest test/unit
# run integration tests
$ pytest test/integration
```

## Non-API Lambda Testing
For Pure AWS Lambda functions that are not generated by the Chalice CLI and are stored in the `/lambda/...` directory. Each Lambda function requires their own virtual environment. A template has been included in `/lambda/project_function_lambda/lambda_function.py`
```bash
# requires that you are in the the lambda directory with its requirements.txt
$ virtualenv env
$ pip install -r requirements.txt
# run tests
$ pytest test
```

## Pandoc

Pandoc is a CLI tool that converts one text file format to another.
```bash
# if pandoc is not installed
$ pip install pandoc
# transform Markdown to Docx
$ pandoc -s README.md -t docx -o README.docx
# transform Docx to Markdown
$ pandoc -s README.docx -t markdown-simple_tables-multiline_tables-grid_tables -o README.md
```
