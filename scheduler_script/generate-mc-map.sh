rsync -azPh --delete --exclude '@eaDir' /volume1/mcserver-nas/ /volume1/docker/mcserver/
docker start overviewer -a
rsync -azPh --stats --delete --exclude '@eaDir' /volume1/docker/export_test/ ssh-joeuser@marc.tv:/www/htdocs/marctv/mc/isotest
