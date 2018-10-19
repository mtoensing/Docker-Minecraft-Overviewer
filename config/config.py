# My config.py script for overviewer:

worlds["pudel"] = "/tmp/world/"
texturepath = "/tmp/overviewer/client.jar"
outputdir = "/tmp/export/"

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

# Only signs with "~*~" in them, and no others. Otherwise, people

# can't have secret bases and the render is too busy anyways.

def signFilter(poi):
    if poi['id'] in ['Sign', 'minecraft:sign']:
        if '~*~' in poi.values():
            return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])



def townFilter(poi):
    if poi['id'] == 'Town':
        return poi['name']

def chestFilter(poi):
    if poi['id'] == "Chest":
        return ("Chest", "Chest with %d items" % len(poi['Items']))

thingsToMaker = [
    dict(name="Players", filterFunction=playerIcons),
    dict(name="Signs", filterFunction=signFilter),
    dict(name="Towns", filterFunction=townFilter),
    dict(name="Chest", filterFunction=chestFilter)
]

renders["day"] = {
    'world': 'pudel',
    'title': 'Day',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'crop': (-2000, -2000, 2000, 2000),
    'markers': thingsToMaker
}

renders["day_lr"] = {
    'world': 'pudel',
    'title': 'Day Reversed',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'crop': (-2000, -2000, 2000, 2000),
    "northdirection" : "lower-right",
    'markers': thingsToMaker
}


renders["night"] = {
    'world': 'pudel',
    'title': 'Night',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'crop': (-2000, -2000, 2000, 2000),
    'markers': thingsToMaker
}

my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]

renders["cave"] = {
    'world': 'pudel',
    'title': 'Cave',
    'rendermode': my_cave,
    "dimension": "overworld",
    'crop': (-2000, -2000, 2000, 2000),
    'markers': thingsToMaker
}

"""
renders["nether"] = {
    "world": "pudel",
    "title": "Nether",
    "rendermode": 'nether_smooth_lighting',
    "dimension": "nether",
    'crop': (-2000, -2000, 2000, 2000),
    'markers': thingsToMaker
}

renders["end"] = {
    "world": "pudel",
    "title": "End",
    "rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.5)],
    "dimension": "end",
    'crop': (-2000, -2000, 2000, 2000),
    'markers': thingsToMaker
}


renders["overlay_Mineral"] = {
    'world': 'pudel',
    'rendermode': [ClearBase(), MineralOverlay()],
    'title': "Mineral Coloring Overlay",
    "dimension": "overworld",
    'crop': (-2000, -2000, 2000, 2000),
    'overlay': ["day"]
}

renders["overlay_Structure"] = {
    'world': 'pudel',
    'rendermode': [ClearBase(), StructureOverlay()],
    'title': "Structure Coloring Overlay",
    "dimension": "overworld",
    'crop': (-2000, -2000, 2000, 2000),
    'overlay': ["day"]
}


renders["overlay_biome"] = {
    'world': 'pudel',
    'rendermode': [ClearBase(), BiomeOverlay()],
    'title': "Biome Coloring Overlay",
    "dimension": "overworld",
    'crop': (-2000, -2000, 2000, 2000),
    'overlay': ["day"]
}


renders["overlay_mobs"] = {
    'world': 'pudel',
    'rendermode': [ClearBase(), SpawnOverlay()],
    'title': "Mob Spawnable Areas Overlay",
    "dimension": "overworld",
    'crop': (-2000, -2000, 2000, 2000),
    'overlay': ["day"]
}
"""
"""
renders["overlay_slime"] = {
    'world': 'pudel',
    'rendermode': [ClearBase(), SlimeOverlay()],
    'title': "Slime Chunk Overlay",
    "dimension": "overworld",
    'crop': (-2000, -2000, 2000, 2000),
    'overlay': ["day"]
}
"""
