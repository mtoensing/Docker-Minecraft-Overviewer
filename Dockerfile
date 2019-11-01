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
ADD https://launcher.mojang.com/v1/objects/8c325a0c5bd674dd747d6ebaa4c791fd363ad8a9/client.jar /tmp/overviewer
RUN git clone https://github.com/overviewer/Minecraft-Overviewer.git .
RUN cp /tmp/overviewer/overviewer_core/aux_files/genPOI.py /tmp/overviewer
RUN python3 setup.py build

RUN mkdir /tmp/world
RUN mkdir /tmp/export
RUN mkdir /tmp/config

RUN useradd -ms /bin/bash bob
USER bob

ENTRYPOINT ["/bin/bash", "-c","/tmp/overviewer/overviewer.py --config=/tmp/config/config.py --genpoi && /tmp/overviewer/overviewer.py --config=/tmp/config/config.py"]
