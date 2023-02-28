# Python image to use.
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

COPY . .
# copy the requirements file used for dependencies

WORKDIR /app/project


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/project/cloudstorage_token.json"


# Run app.py when the container launches
ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
