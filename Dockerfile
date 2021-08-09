# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
# COPY requirements.txt .

# install dependencies
RUN pip install pandas requests uvicorn[standard] fastapi pydantic starlette typing datetime

# copy the content of the local src directory to the working directory
# COPY src/ .

EXPOSE 80

# command to run on container start
# uvicorn main:app --reload
CMD [ "uvicorn", "main:app", "--reload", "--port", "80" ]
