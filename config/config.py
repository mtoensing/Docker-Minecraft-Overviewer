# My config.py script for overviewer:
worlds["pudel"] = "/tmp/world/"
texturepath = "/tmp/overviewer/client.jar"
outputdir = "/tmp/export/"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]
my_nowater = [Base(), EdgeLines(), NoFluids()]
defaultzoom = 5

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://mc.marc.tv/assets/steve.png"
        return "Last known location for %s" % poi['EntityId']

thingsToMaker = [
    dict(name="Players", filterFunction=playerIcons),
]

renders["day"] = {
    'world': 'pudel',
    'title': 'Day',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'crop': (-1200, -1600, 900, 400),
    'markers': thingsToMaker
}

renders["night"] = {
    'world': 'pudel',
    'title': 'Night',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'crop': (-1200, -1600, 900, 400),
    'markers': thingsToMaker
}

renders["cave"] = {
    'world': 'pudel',
    'title': 'Cave',
    'rendermode': my_cave,
    "dimension": "overworld",
    'crop': (-1200, -1600, 900, 400),
    'markers': thingsToMaker
}
'''
renders["nowater"] = {
    'world': 'pudel',
    'title': 'No water',
    'rendermode': my_nowater,
    "dimension": "overworld",
    'crop': (-1200, -1600, 900, 400)
}

renders["day_r"] = {
    'world': 'pudel',
    'title': 'Day upside-down',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    "northdirection" : "lower-right",
    'crop': (-1200, -1600, 900, 400)
}
'''
