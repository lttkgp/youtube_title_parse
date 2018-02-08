# -*- coding: utf-8 -*-
"""
Handle titles with quotes
"""
import re
from functools import reduce

QUOTES = [
    '“”',
    '""',
    '\'\''
]

def looseRegs(sset):
    open_set = sset[0]
    close_set = sset[1]
    return re.compile(open_set + r'(.*?)' + close_set)
MATCH_LOOSE_RXES = map(looseRegs, QUOTES)

def startRegs(sset):
    open_set = sset[0]
    close_set = sset[1]
    return re.compile(r'^' + open_set + r'(.*?)' + close_set + r'\\s*')
MATCH_START_RXES = map(startRegs, QUOTES)

def split_text(text):
    for loose_rex in MATCH_LOOSE_RXES:
        text = re.sub(loose_rex, ' ' + r'\1' + ' ', text)
        match = re.search(loose_rex, text)
        if match:
            split = match.start()
            title = text[split:]
            artist = text[:, split]
            return [artist, title]

def clean(artistOrTitle):
    return reduce((lambda text, rx: re.sub(
        rx, r'\1 ', text)), MATCH_START_RXES, artistOrTitle).strip()
