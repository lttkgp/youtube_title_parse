"""
Parse the title of a YouTube video to try and get artist & song name
"""
import argparse
import youtube_title_parse.plugins as plugins
from youtube_title_parse.core import mapArtistTitle, mapTitle, get_song_artist_title

def get_artist_title(text, options={}):
    """
    Parse method
    """
    return get_song_artist_title(text, options, {
        'before': [plugins.remove_file_extensions, plugins.clean_fluff],
        'split': [plugins.split_artist_title, plugins.split_text],
        'after': [mapArtistTitle(plugins.clean_artist, plugins.clean_title),
                  mapArtistTitle(plugins.clean, plugins.clean), mapTitle(plugins.clean_common_fluff)]
    })

def process(args):
    options = {}
    if args.defaultArtist:
        options['defaultArtist'] = args.defaultArtist
    if args.defaultTitle:
        options['defaultTitle'] = args.defaultTitle
    result = get_artist_title(args.youtube_title, options)
    if result:
        print("%s - %s" % (result[0], result[1]))
    else:
        print("Could not extract an artist and title.")
    return result

def main():
    argparser = argparse.ArgumentParser(
        description='youtube_title_parse', formatter_class=argparse.RawTextHelpFormatter)
    argparser.add_argument(
        "youtube_title", type=str, help='required youtube video title')
    argparser.add_argument(
        "-da", "--defaultArtist", dest="defaultArtist", type=str,
        metavar='DEFAULT_ARTIST', default=False,
        help="""
        fallback artist name
        This value will be used as the 'artist' if
        parser couldn't get artist from YouTube title.
        """
        )
    argparser.add_argument(
        "-dt", "--defaultTitle", dest="defaultTitle", type=str,
        metavar='DEFAULT_TITLE', default=False,
        help="""
        fallback song title
        This value will be used as the 'title' if
        parser couldn't get song title from YouTube title.
        """
        )
    args = argparser.parse_args()
    process(args)

if __name__ == '__main__':
    main()