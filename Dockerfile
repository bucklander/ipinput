FROM debian:buster

RUN apt-get update -y
RUN apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common gunicorn3 python3 python3-pip -y
RUN python3 -m pip install --upgrade pip
RUN mkdir -p /opt/ipinput/

WORKDIR /opt/ipinput/

ENV APPHOME /opt/ipinput
ENV FLASK_APP=ipinput
ENV FLASK_ENV=development

ADD ipinput.py /opt/ipinput/ipinput.py
ADD gunicorn.py /opt/ipinput/gunicorn.py
ADD api.py /opt/ipinput/api.py
ADD requirements.txt /opt/ipinput/requirements.txt
ADD route_table.json /opt/ipinput/route_table.json

RUN python3 -m pip install -r /opt/ipinput/requirements.txt

EXPOSE 5017

CMD ["/usr/bin/gunicorn3", "-c", "/opt/ipinput/gunicorn.py", "api:app"]