# Docker Overviewer for Minecraft 1.15.2

Tutorial (german) https://marc.tv/overviewer-minecraft-docker-synology/

## Minimal example
```
    docker build -t overviewer115 .
    docker run \
      --rm \
      -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
      -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
      -it marctv/overviewer115
```

## User your own config
```
    docker build -t overviewer115 .
    docker run \
      --rm \
      -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
      -v config_sample/config.py:/tmp/config/:ro \
      -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
      -it marctv/overviewer115
```



## Advanced example with --genpoi parameter as an environment variable
```
  docker build -t marctv/overviewer115 .
  docker run \
    --rm \
    -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
    -v /Users/mtoe/Documents/Docker-Minecraft-Overviewer/config_test/:/tmp/config/:ro \
    -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
    -e overviewerParams="--genpoi" \
    -it marctv/overviewer115
```
