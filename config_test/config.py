# My config.py script for viewer:

worlds["pudel"] = "/tmp/world/world/"
worlds["pudel_nether"] = "/tmp/world/world_nether/"
texturepath = "/tmp/overviewer/client.jar"
outputdir = "/tmp/export/"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]
my_nowater = [Base(), EdgeLines(), NoFluids()]

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
    'rendermode': 'normal',
    "dimension": "overworld",
    'crop': (-200, -600, -100, -500),
    'markers': thingsToMaker
}

renders["day_lighting"] = {
    'world': 'pudel',
    'title': 'Day Lighting',
    'rendermode': 'lighting',
    "dimension": "overworld",
    'crop': (-200, -600, -100, -500),
    'markers': thingsToMaker
}

renders["day_nowater"] = {
    'world': 'pudel',
    'title': 'Day Lighting',
    'rendermode': my_nowater,
    "dimension": "overworld",
    'crop': (-200, -600, -100, -500),
    'markers': thingsToMaker
}

renders["night"] = {
    'world': 'pudel',
    'title': 'Night',
    'rendermode': 'night',
    "dimension": "overworld",
    'crop': (-200, -600, -100, -500),
    'markers': thingsToMaker
}

renders["night_smooth"] = {
    'world': 'pudel',
    'title': 'Night Smooth',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'crop': (-200, -600, -100, -500),
    'markers': thingsToMaker
}

renders["cave"] = {
    'world': 'pudel',
    'title': 'Cave',
    'rendermode': my_cave,
    "dimension": "overworld",
    'crop': (-200, -600, -100, -500),
    'markers': thingsToMaker
}

# Railoverlay
renders["rails"] = {
    'world': 'pudel',
    'title': 'Subway',
    "dimension": "overworld",
    'rendermode': [ClearBase(),
            StructureOverlay(structures=[
                    (((0, 0, 0, 66), (0, -1, 0, 4)), (255, 0,   0, 255)),
                    (((0, 0, 0, 27), (0, -1, 0, 4)), (0,   255, 0, 255)),
                    (((0, 0, 0, 28), (0, -1, 0, 4)), (255, 255, 0, 255))
            ]), EdgeLines()],
    "overlay": ["night", "day","night_smooth","day_lighting"],
    'crop': (-200, -600, -100, -500)
}

renders["nether"] = {
    "world": "pudel_nether",
    "title": "Nether",
    "rendermode": "nether",
    "dimension": "nether",
    'crop': (-200, -200, 200, 200),
}
