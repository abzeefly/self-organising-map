FROM kohonen-base:latest

COPY kohonen/tests /app/tests

RUN pytest
