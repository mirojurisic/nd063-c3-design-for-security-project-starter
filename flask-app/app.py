
import os
import logging
from flask import Flask,request
import boto3

app = Flask(__name__)
local_testing = os.environ.get("LOCAL_TESTING","False")
if local_testing == "true":
    _aws_access_key_id = os.environ.get("ACCESS_KEY","")
    _aws_secret_access_key = os.environ.get("SECRET_KEY","")

    s3 = boto3.client('s3',
        aws_access_key_id=_aws_access_key_id,
        aws_secret_access_key=_aws_secret_access_key)
else:
    # EC2 instance can assume role
    s3 = boto3.client('s3')

app.logger.setLevel(logging.DEBUG)

free_bucket = os.environ.get("FREE_BUCKET")
free_recipe_file_name = os.environ.get("FREE_RECIPE_FILE_NAME","free_recipe.txt")
secret_bucket = os.environ.get("SECRET_BUCKET")
secret_recipe_file_name = os.environ.get("SECRET:RECIPE_FILE_NAME","secret_recipe.txt")

# free_bucket="cand-c3-v2-free-recipes-796618404628"
# secret_bucket="cand-c3-v2-secret-recipes-796618404628"

port_number = int(os.environ.get("FLASK_PORT", 5000))


@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/health', methods=['GET'])
def health():
   return 'ok'

@app.route("/free-recipe", methods=['GET'])
def download_free():
    if request.method == 'GET':
        data = s3.get_object(Bucket=free_bucket, Key=free_recipe_file_name)
        contents = data['Body'].read()
        return contents

@app.route("/secret-recipe", methods=['GET'])
def download_secret():
    if request.method == 'GET':
        data = s3.get_object(Bucket=secret_bucket, Key=secret_recipe_file_name)
        contents = data['Body'].read()
        return contents

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port_number)