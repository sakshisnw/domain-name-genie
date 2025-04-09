from generator.name_generator import generate_name

def test_generate_name():
    result = generate_name()
    assert isinstance(result, str)
    assert len(result) > 0
