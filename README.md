# Automated-Emailing
This project demonstrates how to build a Serverless Mass Emailing Application using AWS Lambda, API Gateway, and Amazon SES (Simple Email Service) — with a simple HTML + JavaScript frontend for sending bulk emails through a form.

It showcases the power of serverless computing, automation, and AWS-managed services — perfect for cloud portfolio and LinkedIn projects.


# TECH STACK
| Layer              | Technology                     |
| ------------------ | ------------------------------ |
| Backend            | AWS Lambda (Python 3.9)        |
| Email Service      | AWS Simple Email Service (SES) |
| API                | AWS API Gateway                |
| Frontend           | HTML, CSS, JavaScript          |
| Hosting (optional) | Amazon S3 or CloudFront        |

# ⚙️ AWS Setup Instructions
1️⃣ Configure SES

Go to AWS Console → SES

Verify your sender email address

(Optional) Move out of Sandbox mode to send to unverified emails

2️⃣ Create Lambda Function

Go to AWS Lambda → Create function

Choose Author from scratch

Runtime: Python 3.9

Paste code from backend/lambda_function.py

Add environment variable:

SENDER_EMAIL = your_verified_email@domain.com

Add permission for SES:

AmazonSESFullAccess


Deploy the function

3️⃣ Create API Gateway

Go to API Gateway → Create API → HTTP API

Add integration → Lambda function

Deploy and copy the public Invoke URL

4️⃣ Connect Frontend

In frontend/index.html, replace the API URL:

const apiUrl = "https://your-api-id.execute-api.region.amazonaws.com";
