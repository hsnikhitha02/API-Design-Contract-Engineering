
# API-Design-Contract-Engineering
Goal: Learn how real systems communicate 
Design REST APIs with strict schemas
Learn versioning, validation, error handling 
Create API contracts for all modules

## Project Title
Sentiment Prediction API

## About the project
This is a simple API I built using FastAPI to understand how real systems communicate with each other. The idea is pretty straightforward — you send some text to the API, and it responds with whether the sentiment is positive or negative.

Instead of using any complex model, I kept it basic for now. If the text contains the word “good”, it’s considered positive. Otherwise, it’s marked as negative. The goal here wasn’t accuracy, but to learn how APIs work end-to-end.

## How it works
You send a POST request with some text
The API processes it in the backend
It checks for the word “good”
Then returns a response with the prediction

## Example

Request
{
"text": "This is a good day"
}

Response
{
"prediction": "positive"
}

## Tech used
Python
FastAPI
Pydantic

## How to run
Clone the repo
Open it in your terminal
Install dependencies using pip install fastapi uvicorn
Run the server using uvicorn main:app --reload
Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) and test it there

## What I learned
I got a clear idea of how APIs actually work behind the scenes
Learned how to create endpoints and handle requests
Understood basic validation using schemas
Also got hands-on experience testing APIs

## What can be improved
Right now the logic is very basic, so it can be improved using a proper ML model
Error handling can be made better
Can add versioning for scalability
Security features like authentication can be added later

