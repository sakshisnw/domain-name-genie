from generator.tagline_generator import generate_tagline

def test_generate_tagline():
    result = generate_tagline()
    assert isinstance(result, str)
    assert len(result) > 0
