# Docker Overviewer for Minecraft 1.15.2

Tutorial (german) https://marc.tv/overviewer-minecraft-docker-synology/

## mount volumes
*server folder:*
minecraft directory that contains the map folder.

*export folder:* 
writeable folder for the exported files

*config file:*
config.py (optional) by default the config_sample/config.py file is used

## minimal example
```
    docker run \
      --rm \
      -v /Users/mtoe/Documents/mcserver/:/tmp/server/:ro \
      -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
      -it marctv/minecraft-overviewer
```

## use your own config
```
    docker run \
      --rm \
      -v /Users/mtoe/Documents/mcserver/:/tmp/server/:ro \
      -v config_sample/config.py:/tmp/config/:ro \
      -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
      -it marctv/minecraft-overviewer
```

## advanced example with --genpoi parameter as an environment variable
```
  docker run \
    --rm \
    -v /Users/mtoe/Documents/mcserver/:/tmp/server/:ro \
    -v /Users/mtoe/Documents/Docker-Minecraft-Overviewer/config_test/:/tmp/config/:ro \
    -v /Users/mtoe/Documents/export/:/tmp/export/:rw \
    -e overviewerParams="--genpoi" \
    -it marctv/minecraft-overviewer
```

## generate png file
```
docker run \
  --rm \
  -v $(pwd)/mcserver-test/:/tmp/server/:ro \
  -v $(pwd)/config_sample/:/tmp/config/:ro \
  -v $(pwd)/export/:/tmp/export/:rw \
  -it --entrypoint "/usr/bin/python3" marctv/minecraft-overviewer-local /tmp/overviewer/contrib/png-it.py --memory-limit 12000 --zoom-level 6 --output /tmp/export/full.png /tmp/export/day/
```
