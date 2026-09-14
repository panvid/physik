from manim import *

class VerzögerteBewegungSzene(Scene):
    def construct(self):
        boden = Line(start=LEFT * 5, end=RIGHT * 5, color=GRAY, stroke_width=3)
        boden_label = MathTex("x").next_to(boden.get_end(), RIGHT, buff=0.15)
        boden_gruppe = VGroup(boden, boden_label).shift(DOWN * 1.5)

        def create_car(color=BLUE, opacity=1.0):
            body = Rectangle(width=2.0, height=0.7, fill_opacity=opacity, color=color)
            roof = Rectangle(width=1.1, height=0.45, fill_opacity=opacity, color=color).next_to(body, UP, buff=0)
            wheel1 = Circle(radius=0.22, fill_opacity=opacity, color=BLACK).move_to(body.get_bottom() + LEFT * 0.55)
            wheel2 = Circle(radius=0.22, fill_opacity=opacity, color=BLACK).move_to(body.get_bottom() + RIGHT * 0.55)
            return VGroup(body, roof, wheel1, wheel2)

        start_pos = LEFT * 3 + DOWN * 1.05
        car_start = create_car(color=BLUE)
        car_start.move_to(start_pos)

        v0_arrow = Arrow(
            start=car_start.get_top() + UP * 0.3 + LEFT * 0.5,
            end=car_start.get_top() + UP * 0.3 + RIGHT * 0.8,
            color=YELLOW,
            buff=0
        )
        v0_label = MathTex("v_0", color=YELLOW).next_to(v0_arrow, UP, buff=0.1)
        v0_gruppe = VGroup(v0_arrow, v0_label)

        end_pos = RIGHT * 2 + DOWN * 1.05
        car_end = create_car(color=GRAY, opacity=0.4)
        car_end.move_to(end_pos)

        v_end_label = MathTex("v = 0", color=RED).next_to(car_end.get_top(), UP, buff=0.2)

        rollweg_start = np.array([car_start.get_center()[0], boden.get_y() - 0.4, 0])
        rollweg_end = np.array([car_end.get_center()[0], boden.get_y() - 0.4, 0])

        rollweg_arrow = DoubleArrow(
            start=rollweg_start,
            end=rollweg_end,
            buff=0,
            color=WHITE
        )
        rollweg_label = MathTex(r"\text{Rollweg } \Delta x = 0{,}85\,\text{m}", font_size=28).next_to(rollweg_arrow, DOWN, buff=0.15)
        rollweg_gruppe = VGroup(rollweg_arrow, rollweg_label)

        self.add(boden_gruppe, car_start, v0_gruppe, car_end, v_end_label, rollweg_gruppe)