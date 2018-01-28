"""
Fallback to given title when no title/artist detected
"""
def fallback(title):
    """
    Fallback method
    """
    def fallback_t(artist):
        return [artist, title]
    return fallback_t
