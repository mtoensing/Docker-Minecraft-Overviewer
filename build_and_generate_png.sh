docker build -t marctv/minecraft-overviewer-local .
docker run \
  --rm \
  -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \
  -v /Users/mtoe/Documents/config_test/:/tmp/config/:ro \
  -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
  --entrypoint "/bin/bash" marctv/minecraft-overviewer-local -c /usr/bin/python3 ./tmp/overviewer/contrib/png-it.py --memory-limit 3000 --zoom-level 6 --output /tmp/export/full.png /tmp/export/day/
