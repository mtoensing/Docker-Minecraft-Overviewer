docker build -f Dockerfile -t marctv/minecraft-overviewer-local .
docker run \
  --rm \
  -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
  -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
  -it marctv/minecraft-overviewer-local
