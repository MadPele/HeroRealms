FROM python:3.9
RUN pip3 install --upgrade pip
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

ADD hero_realms/ /app/hero_realms
ADD main.py /app/main.py

ENTRYPOINT ["python3"]
CMD ["/app/main.py"]
