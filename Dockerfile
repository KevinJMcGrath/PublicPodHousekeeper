FROM python:3.8-slim-buster

MAINTAINER Kevin McGrath "kevin.mcgrath@symphony.com"

# Create the venv for dependencies
RUN virtualenv -p python3.6 /env

# Setting these environment variables are the same as running
# source /env/bin/activate.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Copy req file and install dependencies
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Add app source code to image
ADD . /app

CMD [ "python", "main.py" ]