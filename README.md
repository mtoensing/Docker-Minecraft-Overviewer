# Docker Overviewer 1.15 and 1.14.4

Tutorial (german) https://marc.tv/overviewer-minecraft-docker-synology/

## Example

```
docker build -t overviewer114 .
docker run \
  --rm \
  -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
  -v /Users/mtoe/Documents/config/:/tmp/config/:ro \
  -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
  -it overviewer114
