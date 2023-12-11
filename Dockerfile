FROM public.ecr.aws/lambda/python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Copy function code. This copies EVERYTHING inside the app folder to the lambda root.
COPY ./src/ ${LAMBDA_TASK_ROOT}/src/

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
# Since we copied
CMD [ "src.main.handler" ]

# reload Container App if you use poetry
# CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]