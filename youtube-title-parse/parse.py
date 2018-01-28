"""
Parse the title of a YouTube video to try and get artist & song name
"""
import plugins.base as base
import plugins.common as common
import plugins.quoted_title as quoted_title
import plugins.remove_file_extensions as remove_file_extensions
from core import get_song_artist_title as split_artist_title

def get_artist_title(text, options=[]):
    """
    Parse method
    """
    return split_artist_title(text, options, [
        remove_file_extensions,
        base,
        quoted_title,
        common
    ])

def main():
    result = get_artist_title("Ga-In (가인) - Nostalgia (노스텔지아) - Lyrics [Hangul+Translation] .mov")
    if result:
        print("%s - %s" % (result[0], result[1]))
    else:
        print("Could not extract an artist and title.")

if __name__ == '__main__':
    main()
