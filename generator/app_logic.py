from .name_generator import generate_name
from .tagline_generator import generate_tagline
from .moodboard import generate_moodboard_keywords

def generate_brand_package():
    name = generate_name()
    tagline = generate_tagline()
    keywords = generate_moodboard_keywords(name)
    return name, tagline, keywords
