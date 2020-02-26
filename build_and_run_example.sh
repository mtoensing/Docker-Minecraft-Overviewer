docker build -t marctv/minecraft-overviewer-local .
docker run \
  --rm \
  -v $(pwd)/mcserver-test/:/tmp/server/:ro \
  -v $(pwd)/config_sample/:/tmp/config/:ro \
  -v $(pwd)/export/:/tmp/export/:rw \
  -it marctv/minecraft-overviewer-local
