FROM ubuntu:18.04

RUN apt-get update
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-pillow \
    python3-dev \
    python3-numpy \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/overviewer
RUN git clone --progress --verbose https://github.com/overviewer/Minecraft-Overviewer.git .

# https://mcversions.net/download/1.16.1
ADD https://overviewer.org/textures/latest /tmp/overviewer/client.jar
RUN chmod 775 /tmp/overviewer/client.jar

RUN python3 setup.py build

WORKDIR /tmp/server
WORKDIR /tmp/export
WORKDIR /tmp/config

# use sample config as fallback
ADD config_sample/config.py /tmp/config/config.py

RUN useradd -ms /bin/bash bob
USER bob

#eg. "--genpoi"
ENV overviewerParams=""

ENTRYPOINT /tmp/overviewer/overviewer.py --config=/tmp/config/config.py ${overviewerParams}
