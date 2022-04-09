[![PyPI version shields.io](https://img.shields.io/pypi/v/youtube-title-parse.svg)](https://pypi.org/project/youtube-title-parse/)
[![PyPI license](https://img.shields.io/pypi/l/youtube-title-parse.svg)](https://pypi.org/project/youtube-title-parse/)
[![PyPI status](https://img.shields.io/pypi/status/youtube-title-parse.svg)](https://pypi.org/project/youtube-title-parse/)
![youtube_title_parse CI](https://github.com/lttkgp/youtube_title_parse/workflows/youtube_title_parse%20CI/badge.svg)

# youtube title parse

Parse the title of a YouTube video to try and get artist & song name.

## Description

Video titles on YouTube follow no strict format, and so passing the titles directly to music APIs to fetch metadata hardly works. This module attempts to recognize common patterns (using regex) and extract artist and song name.

## Installation

To install [youtube_title_parse](https://pypi.python.org/pypi/youtube-title-parse/), simply run:

```bash
pip install youtube_title_parse
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
If the module can successfully parse the input, `get_artist_title` will return a tuple of the format `[artist, title]` which you can use as below. If not found, `[None, None]` is returned.

```python
from youtube_title_parse import get_artist_title

artist, title = get_artist_title("Seoul - Stay With Us (Official Video)")
assert artist == "Seoul"
assert title == "Stay With Us"
```

## Credits

This module is originally a Python3 rewrite of the equivalent npm library, [`get-artist-title`](https://www.npmjs.com/package/get-artist-title), but adds some extra functionality to catch more patterns.

## Contributing

Pull requests and stars are always welcome. For bugs and feature requests, [please create an issue](https://github.com/lttkgp/youtube-title-parse/issues/new).

## License

youtube-title-parse is made available under the [MIT license](https://opensource.org/licenses/MIT).


## Unit Testing
```python
pip3 install pytest
pip3 install six
```