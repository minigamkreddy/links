FROM ubuntu:16.04

RUN apt-get update && apt-get install -y net-tools && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y python3 && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y vim && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y python3-pip && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y firefox && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y xvfb && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y iputils-ping
RUN pip3 install selenium
RUN pip3 install xvfbwrapper
RUN pip3 install --upgrade pip
RUN pip3 install numpy
RUN pip3 install pandas
COPY manoj/ . 
