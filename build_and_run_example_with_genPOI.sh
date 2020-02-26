docker build -t marctv/minecraft-overviewer-local .
docker run \
  --rm \
  -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
  -v /Users/mtoe/Documents/Docker-Minecraft-Overviewer/config_test/:/tmp/config/:ro \
  -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
  -e overviewerParams="--genpoi" \
  -it marctv/marctv/minecraft-overviewer-local
