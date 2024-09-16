FROM python:10-alphine

WORKDIR /12factor-app

COPY requirements.txt /12factor-app/

RUN pip install -r requirements.txt --no-caches-dir

COPY . /12factor-app/

CMD python app.py
