FROM python:3

ADD metrics.py requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./metrics.py"]

CMD ["cpu", "mem"]