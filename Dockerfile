FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r /app/requerments.txt
CMD PYTHONPATH=$PYTHONPATH:/app/main.pl \
    FLASK_APP=hero_realms flask run --host=0.0.0.0


#FROM python:3
#
#ARG APP_DIR=/usr/src/hello_world_printer
#
#WORKDIR /tmp
#ADD requirements.txt /tmp/requirements.txt
#RUN pip install -r /tmp/requirements.txt
#
#RUN mkdir -p $APP_DIR
#ADD hello_world/ $APP_DIR/hello_world/
#ADD main.py $APP_DIR
#
#CMD PYTHONPATH=$PYTHONPATH:/usr/src/hello_world_printer \
#      FLASK_APP=hello_world flask run --host=0.0.0.0