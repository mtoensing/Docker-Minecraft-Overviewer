docker run \
  --rm \
  -v  /volume1/docker/export/:/tmp/export/:rw \
  -it --entrypoint "/usr/bin/python3" marctv/minecraft-overviewer /tmp/overviewer/contrib/png-it.py --memory-limit 12000 --crop 43 --zoom-level 10 --output /tmp/export/full.png /tmp/export/day_complete_smooth/
