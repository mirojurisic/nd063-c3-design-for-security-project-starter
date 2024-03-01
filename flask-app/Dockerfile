# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app
FROM python:3.12.2-alpine

ARG FREE_BUCKET
ENV FREE_BUCKET=${FREE_BUCKET}

ARG FREE_RECIPE_FILE_NAME
ENV FREE_RECIPE_FILE_NAME=${FREE_RECIPE_FILE_NAME}

ARG SECRET_BUCKET
ENV SECRET_BUCKET=${SECRET_BUCKET}

ARG SECRET_RECIPE_FILE_NAME
ENV SECRET_RECIPE_FILE_NAME=${SECRET_RECIPE_FILE_NAME}

ARG ACCESS_KEY
ENV ACCESS_KEY=${ACCESS_KEY}

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}


ARG LOCAL_TESTING
ENV LOCAL_TESTING=${LOCAL_TESTING}

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY ./app.py /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]
CMD ["app.py" ]

