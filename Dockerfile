### 1st image for jupyter notebook 
FROM ubuntu:latest
RUN apt-get update

### install python, jupiter notebook and related packages
RUN apt-get install -y build-essential python3.8 python3-pip python3-dev
RUN pip3 -q install pip --upgrade

### install tesseract ocr
ENV TZ=America/Recife
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y software-properties-common wget
RUN apt-get update && apt-get install -y tesseract-ocr-eng

RUN apt-get install ffmpeg libsm6 libxext6  -y
 
### copy dependencies from host to container
RUN mkdir /home/scr/
RUN mkdir /home/scr/templates
RUN mkdir /home/scr/static
COPY ./scr/* /home/scr/
COPY ./scr/templates/* /home/scr/templates/

ADD ./requirements.txt /home/

RUN mkdir /usr/local/lib/python3.8/dist-packages/tessocr_module/
COPY ./lib/python3.8/site-packages/tessocr_module/* /usr/local/lib/python3.8/dist-packages/tessocr_module/

RUN pip3 install -r /home/requirements.txt

RUN pip3 install gunicorn gevent
# set working directory
WORKDIR /home/scr

# EXPOSE 80

# CMD [ "python3","/home/scr/app.py" ]
CMD python3 /home/scr/app.py && gunicorn -k gevent -b 0.0.0.0:$PORT main:app
