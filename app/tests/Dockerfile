FROM infologistix/docker-selenium-python:3.10-alpine

WORKDIR /opt/seleniumtest
COPY src/ /opt/seleniumtest

RUN adduser -D seleniumtest

USER seleniumtest

CMD ["python3", "test.py"]
