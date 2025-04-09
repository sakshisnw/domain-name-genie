import random

adjectives = ["Smart", "Fast", "Bright", "Bold", "Creative"]
nouns = ["Tech", "Genie", "Cloud", "Vision", "Nexus"]

def generate_name():
    return f"{random.choice(adjectives)}{random.choice(nouns)}"
