from fastapi import FastAPI
from mangum import Mangum
import boto3

app = FastAPI()

@app.get("/")
def rootf():
    return "Welcome to Questions API"

@app.get("/questions")
def get_all_questions():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Questions')

    response = table.scan()

    data = response['Items']

    return data

@app.get("/question/{question_id}")
def get_question(question_id: int):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Questions')

    response = table.get_item(Key={
        "Id": question_id,
    })

    return response["Item"]

handler = Mangum(app)