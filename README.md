# youtube\_title\_parse

Parse the title of a YouTube video to try and get artist & song name.

## Description

Video titles on YouTube follow no strict format, and so passing the titles directly to music APIs to fetch metadata hardly works. This module attempts to recognize common patterns (using regex) and extract artist and song name.

## Installation

To install Requests, simply use pipenv (or pip, of course):

```bash
pipenv install youtube_title_parse
```

## Usage

### CLI

`youtube_title_parse` comes with a CLI that you can use directly:

```bash
$ youtube_title_parse "Seoul - Stay With Us (Official Video)"
Seoul - Stay With Us
```

### Module

You can also import `youtube_title_parse` as a module.

```python
from youtube_title_parse import get_artist_title
print(get_artist_title("Seoul - Stay With Us (Official Video)"))
```

## Credits

This module is originally a Python3 rewrite of the equivalent npm library, [`get-artist-title`](https://www.npmjs.com/package/get-artist-title), but adds some extra functionality to catch more patterns.

## Contributing

Pull requests and stars are always welcome. For bugs and feature requests, [please create an issue](https://github.com/lttkgp/youtube-title-parse/issues/new).

## License

youtube-title-parse is made available under the [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0).
