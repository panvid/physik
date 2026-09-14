from manim import *

class ZugUndPersonSzene(Scene):
    def construct(self):
        boden = Line(start=LEFT * 6, end=RIGHT * 6, color=GRAY, stroke_width=3)
        boden_label = MathTex("x").next_to(boden.get_end(), RIGHT, buff=0.15)
        boden_gruppe = VGroup(boden, boden_label).shift(DOWN * 1.5)

        zug_body = Rectangle(width=5.0, height=1.2, fill_opacity=1, color=BLUE_D)

        fenster_gruppe = VGroup(*[
            Square(side_length=0.4, fill_opacity=1, color=LIGHT_GRAY)
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.4).move_to(zug_body.get_center() + UP * 0.1)

        raeder = VGroup(*[
            Circle(radius=0.2, fill_opacity=1, color=BLACK)
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.8).move_to(zug_body.get_bottom() + DOWN * 0.1)

        zug = VGroup(zug_body, fenster_gruppe, raeder)
        zug.move_to(LEFT * 2.5 + DOWN * 0.8)

        a2_label = MathTex("a_2 = 0{,}4\\,\\text{m/s}^2", color=BLUE_B, font_size=32)
        a2_label.next_to(zug, UP, buff=0.2)

        person_head = Circle(radius=0.12, fill_opacity=1, color=ORANGE)
        person_body = Line(start=ORIGIN, end=DOWN * 0.5, color=ORANGE, stroke_width=4)
        person_head.next_to(person_body, UP, buff=0)
        person = VGroup(person_head, person_body)

        person.move_to(zug.get_right() + RIGHT * 0.15 + DOWN * 0.5)

        v1_arrow = Arrow(
            start=person.get_top() + RIGHT * 0.1,
            end=person.get_top() + RIGHT * 1.5,
            color=YELLOW,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        v1_label = MathTex("v_1 = 4\\,\\text{km/h}", color=YELLOW, font_size=28).next_to(v1_arrow, UP, buff=0.1)
        v1_gruppe = VGroup(v1_arrow, v1_label)

        self.add(boden_gruppe, zug, a2_label, person, v1_gruppe)

class ZugPersonXTDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 2.5

        y_axis = Arrow(start=origin, end=origin + UP * 5.5, buff=0, color=WHITE)
        y_label = MathTex("x").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 7.5, buff=0, color=WHITE)
        x_label = MathTex("t").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        schnittpunkt_pos = origin + RIGHT * 4.0 + UP * 3.5

        gerade_person = Line(
            start=origin,
            end=origin + RIGHT * 5.5 + UP * 4.8125,
            stroke_width=4,
            color=YELLOW
        )
        label_person = MathTex("x_1\\text{ (Person)}", color=YELLOW, font_size=28)
        label_person.next_to(gerade_person.get_end(), RIGHT, buff=0.15)

        parabel_zug = ParametricFunction(
            lambda t: origin + RIGHT * t + UP * (0.21875 * t**2),
            t_range=[0, 4.8],
            stroke_width=4,
            color=BLUE
        )
        label_zug = MathTex("x_2\\text{ (Zug)}", color=BLUE, font_size=28)
        label_zug.next_to(parabel_zug.point_from_proportion(0.95), UL, buff=0.15)

        schnittpunkt_dot = Dot(point=schnittpunkt_pos, radius=0.08, color=RED)

        ueberholt_label = Text("Zug überholt Person", font_size=18, color=RED)
        ueberholt_label.next_to(schnittpunkt_pos, UL, buff=0.15)

        t_schnitt_pos = np.array([schnittpunkt_pos[0], origin[1], 0])
        linie_t = DashedLine(start=schnittpunkt_pos, end=t_schnitt_pos, stroke_width=2, color=GRAY)
        label_t = MathTex("t_{\\ddot{u}}").next_to(t_schnitt_pos, DOWN, buff=0.15)

        x_schnitt_pos = np.array([origin[0], schnittpunkt_pos[1], 0])
        linie_x = DashedLine(start=schnittpunkt_pos, end=x_schnitt_pos, stroke_width=2, color=GRAY)
        label_x = MathTex("x_{\\ddot{u}}").next_to(x_schnitt_pos, LEFT, buff=0.15)

        self.add(
            axes_group,
            gerade_person,
            label_person,
            parabel_zug,
            label_zug,
            linie_t,
            linie_x,
            schnittpunkt_dot,
            ueberholt_label,
            label_t,
            label_x
        )