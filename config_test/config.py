# My config.py script for viewer:

worlds["pudel"] = "/tmp/world/world/"
worlds["pudel_nether"] = "/tmp/world/world_nether/"
texturepath = "/tmp/overviewer/client.jar"
outputdir = "/tmp/export/"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]
my_nowater = [Base(), EdgeLines(), NoFluids()]
my_crop = (-300, -800, 400, -100)
#

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
    'forcerender': True,
    'world': 'pudel',
    'title': 'Day',
    'rendermode': 'normal',
    "dimension": "overworld",
    'crop': my_crop,
    'markers': thingsToMaker
}

# Import the Observers
from .observer import MultiplexingObserver, ProgressBarObserver, JSObserver

# Construct the ProgressBarObserver
ProgressBarObserver = ProgressBarObserver()

# Construct a basic JSObserver
jsObserver = JSObserver(outputdir, 30)

# Set the observer to a MultiplexingObserver
observer = MultiplexingObserver(ProgressBarObserver, jsObserver)
