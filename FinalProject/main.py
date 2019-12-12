import emotions
from emotions import Emotions
import starwars
from starwars import StarWars

# User Interface for The Emotion Search Engine System
print('Hi there friend!')
print('Choose from one of the following emotions below:')
print('[Happy, Scared, Playful, Cute, Powerful, GOAT]')

""" Emotion Search Engine System takes input from the user and checks to see if it passes any of the conditionals. If there is an equivalent or matching input, the functions defined in starwars.py and emotions.py are ran within the conditionals. """

content = input('How are you feeling today: ')

if content == 'happy' or content == 'Happy' or content == 'HAPPY':
    Emotions().happyFunction()
    StarWars().robotTranslator(content)

elif content == 'scared' or content == 'Scared' or content == 'SCARED':
    Emotions().scaredFunction()
    StarWars().darthvaderTranslator(content)

elif content == 'playful' or content == 'Playful' or content == 'PLAYFUL':
    Emotions().playfulFunction()
    StarWars().pikachuTranslator(content)

elif content == 'cute' or content == 'Cute' or content == 'CUTE':
    Emotions().cuteFunction()
    StarWars().yodaTranslator(content)

elif content == 'goat' or content == 'Goat' or content == 'GOAT':
    Emotions().goatFunction()
    StarWars().chewbaccaTranslator(content)

elif content == 'powerful' or content == 'Powerful' or content == 'POWERFUL':
    Emotions().powerfulFunction()
    print('I do not doubt your powers. Go on and conquer the world! - Siri')

else:
    print('I do not know what you are feeling so I\'ll tell you how I feel!')
    Emotions().computerFunction()
    print('I\'m feeling special! ;) Wink! Wink! - Computer')
