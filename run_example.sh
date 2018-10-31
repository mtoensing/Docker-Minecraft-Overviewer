docker build -t overviewer113 .
docker run \
  --rm \
  -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
  -v /Users/mtoe/Documents/config/:/tmp/config/:ro \
  -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
  -it c2c77a028467
