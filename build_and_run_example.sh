docker build -t marctv/overviewer113 .
docker run \
  --rm \
  -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
  -v /Users/mtoe/Documents/config_test/:/tmp/config/:ro \
  -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
  -it marctv/overviewer113
