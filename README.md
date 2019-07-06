# Docker Overviewer 1.14.X

Tutorial (german) https://marc.tv/wie-generiere-ich-isometrische-karten-fuer-minecraft-mit-docker-und-synology/

## Example

```
docker build -t overviewer114 .
docker run \
  --rm \
  -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
  -v /Users/mtoe/Documents/config/:/tmp/config/:ro \
  -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
  -it overviewer114
