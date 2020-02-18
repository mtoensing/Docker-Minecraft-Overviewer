# Docker Overviewer for Minecraft 1.15.1

Tutorial (german) https://marc.tv/overviewer-minecraft-docker-synology/

## Example
```
    docker build -t overviewer114 .
    docker run \
      --rm \
      -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
      -v /Users/mtoe/Documents/config/:/tmp/config/:ro \
      -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
      -it marctv/overviewer115
```

## Advanced example with --genpoi parameter as an environment variable
```
  docker build -t marctv/overviewer113 .
  docker run \
    --rm \
    -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
    -v /Users/mtoe/Documents/Docker-Minecraft-Overviewer/config_test/:/tmp/config/:ro \
    -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
    -e overviewerParams="--genpoi" \
    -it marctv/overviewer115
```
