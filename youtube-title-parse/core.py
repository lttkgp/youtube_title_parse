"""
Core parsing methods
"""
from plugins.base import clean_fluff, split_artist_title, clean_artist, clean_title
import fallback_artist
import fallback_title

def flow(functions):
    if not functions:
        def failed(arg):
            return arg
        return failed

    def flow_func(arguments):
        result = functions[0](arguments)
        for function in functions[1:]:
            result = function(result)
        return result
    return flow_func

def combine_splitters(splitters):
    def combine_func(text):
        for splitter in splitters:
            result = splitter(text)
            if result:
                return result
    return combine_func

def reduce_plugins(fallbacks):
    split = []
    if fallbacks:
        for fallback in fallbacks:
            split.append(fallback)
    before = [clean_fluff]
    split = [split_artist_title]
    after = [mapArtistTitle(clean_artist, clean_title), mapTitle(clean_title)]
    return [flow(before), combine_splitters(split), flow(after)]

# Helpful-ish plugin checks
def checkPlugin(plugin):
    if not plugin[1]:
        print('no title splitter was specified by any plugin')

def mapArtist(fn):
    def mapA(parts):
        return [fn(parts[0]), parts[1]]
    return mapA

def mapTitle(fn):
    def mapT(parts):
        return [parts[0], fn(parts[1])]
    return mapT

def mapArtistTitle(mapArtist, mapTitle):
    def mapAT(parts):
        return [mapArtist(parts[0]), mapTitle(parts[1])]
    return mapAT

def get_song_artist_title(text, options, plugins):
    fallbacks = []
    if options:
        if 'defaultArtist' in options:
            fallbacks.append(fallback_artist.fallback)
        if 'defaultTitle' in options:
            fallbacks.append(fallback_title.fallback)
    plugin = reduce_plugins(fallbacks)
    checkPlugin(plugin)
    split = plugin[1](plugin[0](text))
    if not split:
        return
    return plugin[2](split)
