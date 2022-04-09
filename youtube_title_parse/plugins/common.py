# -*- coding: utf-8 -*-
"""
Remove common fluff. Main imported file
"""
import re


def clean_common_fluff(title):
    """
    Clean common fluff from title
    """
    # Sub Pop includes "(not the video)" on audio tracks.
    # The " video" part might be stripped by other plugins.
    title = re.sub(r"\(not the( video)?\)\s*$", "", title)

    # Lyrics videos
    title = re.sub(
        r"(\s*[-~_/]\s*)?\b(with\s+)?lyrics\s*", "", title, flags=re.IGNORECASE
    )
    title = re.sub(r"\(\s*(with\s+)?lyrics\s*\)\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\s*\(\s*\)", "", title)  # ()

    #todo: condiational  for "english -  korean words" regex

    #todo: condiational  for "Korean words - english words" regex. Do not remove Korean characters if the patterns match. 

    if re.search(r"([A-Za-z])+", title): #If english characters, remove all korean.
        title = re.sub(r"[\u3131-\uD79D]", "", title) 
        title = re.sub(r"^\s", "", title) 
    
    title = re.sub(
        r"\(", "", title, flags=re.IGNORECASE
    )
    title = re.sub(
        r"\)", "", title, flags=re.IGNORECASE
    )
    return title.strip()


