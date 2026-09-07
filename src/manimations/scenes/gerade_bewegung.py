from manim import *

config.frame_width = 8
config.frame_height = 5

class Geradlinig(Scene):
    def construct(self):
        linie = Line(start=[-3, 0, 0], end=[3, 0, 0], stroke_width=4, color=BLUE)

        massepunkt = Dot(point=[1, 0, 0], radius=0.15, color=RED)

        self.add(linie, massepunkt)


class Kreisfoermig(Scene):
    def construct(self):
        kreis = Circle(radius=1.8, stroke_width=4, color=TEAL)

        punkt_pos = kreis.point_from_proportion(0.125)
        massepunkt = Dot(point=punkt_pos, radius=0.15, color=RED)

        self.add(kreis, massepunkt)


class KrummlinigChaotisch(Scene):
    def construct(self):
        punkte = [
            np.array([-3, -1.5, 0]),
            np.array([-2, 1.8, 0]),
            np.array([-0.5, -1.2, 0]),
            np.array([1, 1.5, 0]),
            np.array([1.8, -1.5, 0]),
            np.array([0.8, -0.8, 0]),
            np.array([2.8, 0.5, 0])
        ]

        pfad = VMobject()
        pfad.set_points_smoothly(punkte)
        pfad.set_stroke(width=4)
        pfad.set_color_by_gradient(BLUE, TEAL, GREEN)

        massepunkt = Dot(point=pfad.get_end(), radius=0.15, color=RED)

        self.add(pfad, massepunkt)