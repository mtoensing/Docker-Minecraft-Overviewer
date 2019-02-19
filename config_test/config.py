# My config.py script for viewer:

worlds["pudel"] = "/tmp/world/world/"
worlds["pudel_nether"] = "/tmp/world/world_nether/"
texturepath = "/tmp/overviewer/client.jar"
outputdir = "/tmp/export/"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]
my_nowater = [Base(), EdgeLines(), NoFluids()]
my_crop = (-200, -600, -100, -500)

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://mc.marc.tv/assets/steve.png"
        return "Last known location for %s" % poi['EntityId']

def playerSpawns(poi):
    if poi['id']=='PlayerSpawn':
        poi['icon'] = "https://mc.marc.tv/assets/bed.png"
        return "Spawn for %s" % poi['EntityId']

def signFilter(poi):
    if poi['id'] == 'Sign':
        poi['icon'] = "https://mc.marc.tv/assets/sign.png"
        return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

def chestFilter(poi):
    if poi['id'] == 'Chest':
        return "Chest with %d items" % len(poi['Items'])


thingsToMaker = [
    dict(name="Players", filterFunction=playerIcons),
    dict(name="Beds", filterFunction=playerSpawns)
]

renders["day"] = {
    'world': 'pudel',
    'title': 'Day',
    'rendermode': 'normal',
    "dimension": "overworld",
    'crop': my_crop,
    'markers': thingsToMaker
}

renders["day_r"] = {
    'world': 'pudel',
    'title': 'Day Reversed',
    'rendermode': 'normal',
    "dimension": "overworld",
    'crop': my_crop,
    'northdirection': "lower-right",
    'markers': thingsToMaker
}


renders["day_lighting"] = {
    'world': 'pudel',
    'title': 'Day Lighting',
    'rendermode': 'lighting',
    "dimension": "overworld",
    'crop': my_crop,
    'markers': thingsToMaker
}

renders["day_nowater"] = {
    'world': 'pudel',
    'title': 'Day No Water',
    'rendermode': my_nowater,
    "dimension": "overworld",
    'crop': my_crop,
    'markers': thingsToMaker
}

renders["night"] = {
    'world': 'pudel',
    'title': 'Night',
    'rendermode': 'night',
    "dimension": "overworld",
    'crop': my_crop,
    'markers': thingsToMaker
}

renders["night_smooth"] = {
    'world': 'pudel',
    'title': 'Night Smooth',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'crop': my_crop,
    'markers': thingsToMaker
}

renders["cave"] = {
    'world': 'pudel',
    'title': 'Cave',
    'rendermode': my_cave,
    "dimension": "overworld",
    'crop': my_crop,
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
    "overlay": ["night", "day","night_smooth","day_lighting","day_nowater"],
    'crop': my_crop,
}

renders["nether"] = {
    "world": "pudel_nether",
    "title": "Nether",
    "rendermode": "nether",
    "dimension": "nether",
    'crop': (-200, -200, 200, 200),
}

# Import the Observers
from observer import MultiplexingObserver, ProgressBarObserver, JSObserver

# Construct the ProgressBarObserver
ProgressBarObserver = ProgressBarObserver()

# Construct a basic JSObserver
jsObserver = JSObserver(outputdir, 30)

# Set the observer to a MultiplexingObserver
observer = MultiplexingObserver(ProgressBarObserver, jsObserver)
