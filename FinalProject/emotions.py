import pyglet
import subprocess
# Subprocess module is used to play .wav audio files
# Pyglet module is used to play .gif media files

class Emotions():
    """ The functions within this class have similar functionality. Each function below stores a unique sound file and a unique gif file according to the predefined emotion."""


    def happyFunction(self):
        # Retrieves happy.gif and happy.wav
        subprocess.call(['afplay', 'assets/happy.wav'])

        animationhappy = pyglet.image.load_animation('assets/happy.gif')
        animationhappy_sprite = pyglet.sprite.Sprite(animationhappy)

        w = animationhappy_sprite.width
        h = animationhappy_sprite.height
        window = pyglet.window.Window(width=w, height=h)

        @window.event
        def on_draw():
            window.clear()
            animationhappy_sprite.draw()

        pyglet.app.run()

    def scaredFunction(self):
        # Retrieves scared.gif and scared.wav
        subprocess.call(['afplay', 'assets/scared.wav'])

        animationscared = pyglet.image.load_animation('assets/scared.gif')
        animationscared_sprite = pyglet.sprite.Sprite(animationscared)

        w = animationscared_sprite.width
        h = animationscared_sprite.height
        window = pyglet.window.Window(width=w, height=h)

        @window.event
        def on_draw():
            window.clear()
            animationscared_sprite.draw()

        pyglet.app.run()

    def playfulFunction(self):
        # Retrieves playful.gif and playful.wav
        subprocess.call(['afplay', 'assets/playful.wav'])

        animationplayful = pyglet.image.load_animation('assets/playful.gif')
        animationplayful_sprite = pyglet.sprite.Sprite(animationplayful)

        w = animationplayful_sprite.width
        h = animationplayful_sprite.height
        window = pyglet.window.Window(width=w, height=h)

        @window.event
        def on_draw():
            window.clear()
            animationplayful_sprite.draw()

        pyglet.app.run()

    def cuteFunction(self):
        # Retrieves cute.gif and cute.wav
        subprocess.call(['afplay', 'assets/cute.wav'])

        animationcute = pyglet.image.load_animation('assets/cute.gif')
        animationcute_sprite = pyglet.sprite.Sprite(animationcute)

        w = animationcute_sprite.width
        h = animationcute_sprite.height
        window = pyglet.window.Window(width=w, height=h)

        @window.event
        def on_draw():
            window.clear()
            animationcute_sprite.draw()

        pyglet.app.run()

    def computerFunction(self):
        # Retrieves computer.gif and computer.wav
        subprocess.call(['afplay', 'assets/computer.wav'])

        animationcomputer = pyglet.image.load_animation('assets/computer.gif')
        animationcomputer_sprite = pyglet.sprite.Sprite(animationcomputer)

        w = animationcomputer_sprite.width
        h = animationcomputer_sprite.height
        window = pyglet.window.Window(width=w, height=h)

        @window.event
        def on_draw():
            window.clear()
            animationcomputer_sprite.draw()

        pyglet.app.run()

    def goatFunction(self):
        # Retrieves goat.gif and goat.wav
        subprocess.call(['afplay', 'assets/goat.wav'])

        animationgoat = pyglet.image.load_animation('assets/goat.gif')
        animationgoat_sprite = pyglet.sprite.Sprite(animationgoat)

        w = animationgoat_sprite.width
        h = animationgoat_sprite.height
        window = pyglet.window.Window(width=w, height=h)

        @window.event
        def on_draw():
            window.clear()
            animationgoat_sprite.draw()

        pyglet.app.run()

    def powerfulFunction(self):
        # Retrieves powerful.gif and powerful.wav
        subprocess.call(['afplay', 'assets/powerful.wav'])

        animationpowerful = pyglet.image.load_animation('assets/powerful.gif')
        animationpowerful_sprite = pyglet.sprite.Sprite(animationpowerful)

        w = animationpowerful_sprite.width
        h = animationpowerful_sprite.height
        window = pyglet.window.Window(width=w, height=h)

        @window.event
        def on_draw():
            window.clear()
            animationpowerful_sprite.draw()

        pyglet.app.run()
