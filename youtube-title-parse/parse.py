"""
Parse the title of a YouTube video to try and get artist & song name
"""
from plugins.base import clean_fluff, split_artist_title, clean_artist, clean_title
from plugins.remove_file_extensions import remove_file_extensions
from plugins.quoted_title import split_text, clean
from plugins.common import clean_common_fluff
from core import mapArtistTitle, mapTitle, get_song_artist_title

def get_artist_title(text, options=[]):
    """
    Parse method
    """
    return get_song_artist_title(text, options, {
        'before': [remove_file_extensions, clean_fluff],
        'split': [split_artist_title, split_text],
        'after': [mapArtistTitle(clean_artist, clean_title),
                  mapArtistTitle(clean, clean), mapTitle(clean_common_fluff)]
    })

def main():
    result = get_artist_title("Ga-In (가인) - Nostalgia (노스텔지아) - Lyrics [Hangul+Translation] .mov")
    if result:
        print("%s - %s" % (result[0], result[1]))
    else:
        print("Could not extract an artist and title.")

if __name__ == '__main__':
    main()
