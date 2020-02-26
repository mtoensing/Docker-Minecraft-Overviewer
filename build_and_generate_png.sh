# docker build -t marctv/minecraft-overviewer-local .
docker run \
  --rm \
  -v $(pwd)/mcserver-test/:/tmp/server/:ro \
  -v $(pwd)/config_sample/:/tmp/config/:ro \
  -v $(pwd)/export/:/tmp/export/:rw \
  -it --entrypoint "/usr/bin/python3" marctv/minecraft-overviewer-local /tmp/overviewer/contrib/png-it.py --memory-limit 12000 --zoom-level 6 --output /tmp/export/full.png /tmp/export/day/

  # -it --entrypoint "/usr/bin/python3" marctv/minecraft-overviewer-local /tmp/overviewer/contrib/png-it.py --memory-limit 12000 --crop 43 --zoom-level 10 --output /tmp/export/full.png /tmp/export/day/
