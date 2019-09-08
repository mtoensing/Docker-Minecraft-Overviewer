# My config.py script for overviewer:
worlds["pudel"] = "/tmp/world/world/"
worlds["pudel_nether"] = "/tmp/world/world_nether/"
texturepath = "/tmp/overviewer/client.jar"
processes = 2
outputdir = "/tmp/export/"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]
my_nowater = [Base(), EdgeLines(), NoFluids()]
defaultzoom = 5
my_crop = (-1200, -1600, 900, 400)

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://mc.marc.tv/assets/steve.png"
        return "Last known location for %s" % poi['EntityId']

def playerSpawns(poi):
    if poi['id']=='PlayerSpawn':
        poi['icon'] = "https://mc.marc.tv/assets/bed.png"
        return "Spawn for %s" % poi['EntityId']

def signFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        poi['icon'] = "https://mc.marc.tv/assets/sign.png"
        text = "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
        if text.__contains__('...'):
            return text.replace('...', '')

def chestFilter(poi):
    if poi['id'] == 'Chest' or poi['id'] == 'minecraft:chest':
        return "Chest with %d items" % len(poi['Items'])


thingsToMaker = [
    dict(name="Players", filterFunction=playerIcons),
    dict(name="Beds", filterFunction=playerSpawns),
    dict(name="Signs", filterFunction=signFilter),
    #dict(name="Chests", filterFunction=chestFilter)
]

renders["day_complete_smooth"] = {
    'world': 'pudel',
    'title': 'Day',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'markers': thingsToMaker
}

renders["night_complete"] = {
    'world': 'pudel',
    'title': 'Night',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'markers': thingsToMaker
}

renders["cave_complete"] = {
    'world': 'pudel',
    'title': 'Cave',
    'rendermode': my_cave,
    "dimension": "overworld",
    'markers': thingsToMaker
}

# Railoverlay
renders["rails"] = {
    'world': 'pudel',
    'title': 'Rails',
    "dimension": "overworld",
    'rendermode': [ClearBase(),
            MineralOverlay(minerals=[
                    (66, (255,0,0)),
                    (27, (255,0,0)),
                    (28, (255,0,0))
            ]), EdgeLines()],
    "overlay": ["day_complete_smooth","night_complete","cave_complete"]
}
'''
# Pistons and Observer
renders["farms"] = {
    'world': 'pudel',
    'title': 'Farms',
    "dimension": "overworld",
    'rendermode': [ClearBase(),
            MineralOverlay(minerals=[
				(29, (255,0,0)),
				(33, (255,0,0)),
				(34, (255,0,0)),
                (154, (255,0,0)),
				(218, (255,0,0))
			]), EdgeLines()],
    "overlay": ["day_complete_smooth","night_complete","cave_complete"]
}
'''
'''
renders["nether"] = {
    "world": "pudel_nether",
    "title": "Nether",
    "rendermode": "nether",
    "dimension": "nether",
    'crop': (-200, -200, 200, 200)
}
'''

# Import the Observers
from .observer import MultiplexingObserver, ProgressBarObserver, JSObserver

# Construct the ProgressBarObserver
pbo = ProgressBarObserver()

# Construct a basic JSObserver
jsObserver = JSObserver(outputdir, 30)

# Set the observer to a MultiplexingObserver
observer = MultiplexingObserver(pbo, jsObserver)

'''
renders["day_smooth"] = {
    'world': 'pudel',
    'title': 'Day',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'crop': my_crop,
    'markers': thingsToMaker
}

renders["night_smooth"] = {
    'world': 'pudel',
    'title': 'Night',
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
'''
