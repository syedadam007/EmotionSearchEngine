import starwars
from starwars import StarWars

# Test for Robot Translator
def test_robot_translate():
    content = 'Excellent'
    introduction = 'How are you feeling today'
    list1 = introduction.split()

    robot_sentence = StarWars().robotTranslator(content)
    return robot_sentence

    expected_robot_sentence = 'Beebop boobeep. My signals inform me that you are feeling Excellent. - R2D2'

    assert robot_sentence == expected_robot_sentence


# Test for Pikachu Translator
def test_pikachu_translate():
    content = 'Playful'
    introduction = 'How are you feeling today'
    list1 = introduction.split()

    pikachu_sentence = StarWars().pikachuTranslator(content)
    return pikachu_sentence

    expected_pikachu_sentence = 'Pika pika feeling Playful. - Pikachu'

    assert pikachu_sentence == expected_pikachu_sentence


# Test for DarthVader Translator
def test_darthvader_translate():
    content = 'Scared'
    introduction = 'How are you feeling today'
    list1 = introduction.split()

    darthvader_sentence = StarWars().darthvaderTranslator(content)
    return darthvader_sentence

    expected_darthvader_sentence = 'You must feel Scared because I am your father. - Darth Vader'

    assert darthvader_sentence == expected_darthvader_sentence
