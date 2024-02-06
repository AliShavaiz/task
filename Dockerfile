FROM python:3.12-slim-buster

WORKDIR / SelteqTask
ADD . /SelteqTask
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python mnaage.py runserver 0:8000