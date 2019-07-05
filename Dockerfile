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

RUN mkdir /tmp/overviewer
WORKDIR /tmp/overviewer

COPY COPY/Minecraft-Overviewer /tmp/overviewer
COPY COPY/Minecraft-Overviewer/overviewer_core/aux_files/genPOI.py /tmp/overviewer
RUN python3 setup.py build

COPY COPY/client.jar /tmp/overviewer

RUN mkdir /tmp/world
RUN mkdir /tmp/export
RUN mkdir /tmp/config

RUN useradd -ms /bin/bash bob
USER bob

ENTRYPOINT ["/bin/bash", "-c","/tmp/overviewer/overviewer.py --config=/tmp/config/config.py --skip-scan --genpoi && /tmp/overviewer/overviewer.py --config=/tmp/config/config.py"]
