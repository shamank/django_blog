FROM python

WORKDIR /usr/local/app
COPY requiments.txt ./

RUN pip install -r requiments.txt 
