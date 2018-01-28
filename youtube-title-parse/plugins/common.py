"""
Remove common fluff
"""
import re

def clean_title(title):
    """
    Clean common fluff from title
    """
    # Sub Pop includes "(not the video)" on audio tracks.
    # The " video" part might be stripped by other plugins.
    title = re.sub(r'/\(not the( video)?\)\s*$/', '', title)
    # Lyrics videos
    title = re.sub(r'/(\s*[-~_/]\s*)?\b(with\s+)?lyrics\s*/i', '', title)
    title = re.sub(r'/\(\s*(with\s+)?lyrics\s*\)\s*/i', '', title)
    return title.strip(' ')
