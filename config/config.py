# My config.py script for overviewer:
worlds["pudel"] = "/tmp/world/"
texturepath = "/tmp/overviewer/client.jar"
outputdir = "/tmp/export/"

defaultzoom = 3

my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]

renders["day"] = {
    'world': 'pudel',
    'title': 'Day',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'crop': (-1200, -1600, 900, 400)
}

"""
renders["night"] = {
    'world': 'pudel',
    'title': 'Night',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'crop': (-1200, -1600, 900, 400)
}

renders["cave"] = {
    'world': 'pudel',
    'title': 'Cave',
    'rendermode': my_cave,
    "dimension": "overworld",
    'crop': (-1200, -1600, 900, 400)
}
"""
