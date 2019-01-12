# docker build -t marctv/overviewer113 .
docker run \
  --rm \
  -v /Users/mtoe/Documents/world/:/tmp/world/:ro \
  -v /Users/mtoe/Documents/config/:/tmp/config/:ro \
  -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
  -it marctv/overviewer113
