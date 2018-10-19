docker build -t overviewer113 .
docker run \
  --rm \
  -v /Users/mtoe/Documents/mcserver/:/tmp/world/:ro \  #path to map folder
  -v /Users/mtoe/Documents/config/:/tmp/config/:ro \ #path to config.py
  -v /Users/mtoe/Documents/export/:/tmp/export/:rw \ #path to export folder
  -it overviewer113
