# Aview-Challenge-2

A Python-based serverless application using AWS Lambda that fetches random cat images from The Cat API and then stored in Google Cloud Firestore.

## Getting Started

This guide will help you get started with the app and start exploring its features.

### Prerequisites

Before you begin, you'll need to make sure you have the following installed/ready:

- Python
- Docker (and Docker CLI installed)
- Amazon Web Services (and AWS ECR CLI installed)
- Google Cloud Platform

### Installation

To install and run the app, follow these steps:

1. Create a Cloud Firestore noSQL Database in Native Mode and create a new collection `cat-images`
2. Create a Service Account [following these instructions](https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform?hl=en#step_3_create_service_account_credentials) and set the permissions to editor
3. Download the Service Account JSON and save it in the root directory of this repo (rename it to service_account.json)
4. Run `docker build -t docker-image:test`
5. Create an IAM User on AWS and set required permissions
6. [Follow this documentation](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html) to tag and push the Dockerfile to AWS ECR Registry and create the Lambda function

## Additional Information

This project relies on the following external APIs:

- [TheCatAPI](https://thecatapi.com/): Provides the random cat images used in the Lambda function.

For further details or inquiries, please refer to the project repository or contact the project maintainers.
