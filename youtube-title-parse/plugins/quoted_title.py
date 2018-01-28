"""
Handle titles with quotes
"""
import re
from functools import reduce

def clean_quotes(quotes):
    def looseRegs(sset):
        open_set = sset[0]
        close_set = sset[1]
        return re.compile(open_set + r'(.*?)' + close_set)
    match_loose_rxes = map(looseRegs, quotes)

    def startRegs(sset):
        open_set = sset[0]
        close_set = sset[1]
        return re.compile(r'^' + open_set + r'(.*?)' + close_set + r'\\s*')
    match_start_rxes = map(startRegs, quotes)

    def split(text):
        for loose_rex in match_loose_rxes:
            text = re.sub(loose_rex, ' ' + r'\1' + ' ', text)
            match = re.search(loose_rex, text)
            if match:
                split = match.start()
                title = text[split:]
                artist = text[:, split]
                return [artist, title]

    def clean(artistOrTitle):
        return reduce((lambda text, rx: re.sub(
            rx, r'\1 ', text)), match_start_rxes, artistOrTitle).split(' ')
