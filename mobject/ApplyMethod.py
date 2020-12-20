from manim import *
class ApplyMethodExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)
        
        #animate the change of color
        self.play(ApplyMethod(square.set_fill, WHITE))
        self.wait(1)
        
        #animate the change of position
        self.play(ApplyMethod(square.shift, UP))
        self.wait(1)