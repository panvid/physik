from manim import *


class AufgabenstellungSzene(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-1, 10, 1],
            y_range=[-1, 3, 1],
            x_length=12,
            y_length=4,
            axis_config={"include_tip": True, "tip_shape": StealthTip},
        )
        x_label = ax.get_x_axis_label(Tex("x"))
        self.add(ax.get_x_axis(), x_label)

        car_body = Rectangle(width=2, height=0.8, fill_opacity=1, color=BLUE)
        car_roof = Rectangle(width=1.2, height=0.5, fill_opacity=1, color=BLUE_D).next_to(car_body, UP, buff=0)
        wheel1 = Circle(radius=0.25, fill_opacity=1, color=BLACK).move_to(car_body.get_bottom() + LEFT * 0.6)
        wheel2 = Circle(radius=0.25, fill_opacity=1, color=BLACK).move_to(car_body.get_bottom() + RIGHT * 0.6)
        car = VGroup(car_body, car_roof, wheel1, wheel2)
        car.move_to(ax.c2p(1, 0) + UP * 0.65)

        cyclist_torso = Line(start=ORIGIN, end=UP * 0.8, color=GREEN_E, stroke_width=6)
        cyclist_head = Circle(radius=0.15, fill_opacity=1, color=GREEN_E).next_to(cyclist_torso, UP, buff=0)
        wheel_b = Circle(radius=0.2, color=BLACK, stroke_width=4).move_to(
            cyclist_torso.get_bottom() + LEFT * 0.3 + DOWN * 0.2)
        wheel_f = Circle(radius=0.2, color=BLACK, stroke_width=4).move_to(
            cyclist_torso.get_bottom() + RIGHT * 0.3 + DOWN * 0.2)

        frame_back = Line(wheel_b.get_center(), cyclist_torso.get_bottom(), color=GRAY, stroke_width=3)
        frame_front = Line(wheel_f.get_center(), cyclist_torso.get_bottom(), color=GRAY, stroke_width=3)
        frame_top = Line(cyclist_torso.get_bottom(), cyclist_torso.get_center(), color=GRAY, stroke_width=3)

        cyclist = VGroup(cyclist_torso, cyclist_head, wheel_f, wheel_b, frame_back, frame_front, frame_top)
        cyclist.move_to(ax.c2p(7, 0) + UP * 0.7)

        dist_line = DoubleArrow(
            start=car.get_right() + UP * 0.2,
            end=cyclist.get_left() + UP * 0.2,
            buff=0.1,
            color=RED
        )
        dist_label = MathTex("20\,m", color=RED).next_to(dist_line, UP, buff=0.1)
        distance_group = VGroup(dist_line, dist_label)

        self.add(car, cyclist, distance_group)
        self.wait(1)

        self.play(
            car.animate.shift(RIGHT * 2.5),
            cyclist.animate.shift(RIGHT * 1.0),
            run_time=3,
            rate_func=linear
        )
        self.wait(1)