from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.0)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
#        Create(circle)



