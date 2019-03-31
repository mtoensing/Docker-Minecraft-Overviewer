FROM ubuntu:18.04

RUN apt-get update
RUN apt-get update && apt-get install -y \
    build-essential \
    python-pil \
    python-dev \
    python-numpy \
    git \
    wget \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir /tmp/overviewer
WORKDIR /tmp/overviewer

COPY COPY/Minecraft-Overviewer-minecraft113-fixed /tmp/overviewer
COPY COPY/Minecraft-Overviewer-minecraft113-fixed/overviewer_core/aux_files/genPOI.py /tmp/overviewer
RUN python2 setup.py build

COPY COPY/client.jar /tmp/overviewer

RUN mkdir /tmp/world
RUN mkdir /tmp/export
RUN mkdir /tmp/config

RUN useradd -ms /bin/bash bob
USER bob

ENTRYPOINT ["/bin/bash", "-c","/tmp/overviewer/overviewer.py --config=/tmp/config/config.py --skip-scan --genpoi && /tmp/overviewer/overviewer.py --config=/tmp/config/config.py"]
