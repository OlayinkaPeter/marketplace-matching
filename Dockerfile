FROM python:3.10.14-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

COPY ./prompts /code/prompts

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "30120"]
