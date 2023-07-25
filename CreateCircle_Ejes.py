from manim import *


class CreateCircle_Ejes(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.0)  # set the color and transparency

        ax = Axes(
            x_range=[-2, 2, .5],
            y_range=[-2, 2, .5],
            tips=False,
#            axis_config={"include_numbers": True},
#            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        self.add(ax)
        self.play(Create(circle))  # show the circle on screen
#        Create(circle)



