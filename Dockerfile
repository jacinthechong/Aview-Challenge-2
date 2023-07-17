# Base image
FROM public.ecr.aws/lambda/python:3.10

# Copy the requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}
COPY lambda_function.py ${LAMBDA_TASK_ROOT}
COPY service_account.json ${LAMBDA_TASK_ROOT}
# Install dependencies
RUN pip install -r requirements.txt -t ${LAMBDA_TASK_ROOT}

CMD [ "lambda_function.lambda_handler" ]
