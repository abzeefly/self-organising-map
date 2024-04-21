# USE PYTHON VERSION 3.11.4
FROM python:3.11.4-slim
#  USE /app AS THE MAIN WORK DIRECTORY
WORKDIR /app
#  COPY REQUIREMENTS
COPY requirements.txt /app/requirements.txt
# INSTALL DEPENDECIES FROM REQUIREMENTS TXT
RUN pip install -r /app/requirements.txt

# RUN PYTHON AFTER INSTALLING DEPENDENCIES
COPY kohonen/src /app/src
COPY kohonen/main.py /app/main.py 

RUN ["python3"]
