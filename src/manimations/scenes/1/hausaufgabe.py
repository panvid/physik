from manim import *

class ZugBegegnungSkizze(Scene):
    def construct(self):
        boden = Line(start=LEFT * 5.5, end=RIGHT * 5.5, color=GRAY, stroke_width=3)
        boden_label = MathTex("x").next_to(boden.get_end(), RIGHT, buff=0.15)
        boden_gruppe = VGroup(boden, boden_label).shift(DOWN * 1.5)

        def create_train(color):
            body = Rectangle(width=2.2, height=0.8, fill_opacity=1, color=color)
            roof = Rectangle(width=1.4, height=0.4, fill_opacity=1, color=color).next_to(body, UP, buff=0)
            wheels = VGroup(*[
                Circle(radius=0.18, fill_opacity=1, color=BLACK)
                for _ in range(3)
            ]).arrange(RIGHT, buff=0.35).move_to(body.get_bottom() + DOWN * 0.05)
            return VGroup(body, roof, wheels)

        zug_a = create_train(BLUE)
        zug_a.move_to(LEFT * 4.0 + DOWN * 0.95)
        label_a = MathTex("Z_A", color=BLUE).next_to(zug_a, UP, buff=0.6)

        v_a_arrow = Arrow(
            start=zug_a.get_top() + UP * 0.1,
            end=zug_a.get_top() + UP * 0.1 + RIGHT * 1.5,
            color=BLUE,
            buff=0,
            stroke_width=4
        )
        v_a_label = MathTex("v_A = 100\\,\\text{km/h}", color=BLUE, font_size=26).next_to(v_a_arrow, UP, buff=0.1)

        zug_b = create_train(RED)
        zug_b.move_to(RIGHT * 4.0 + DOWN * 0.95)
        label_b = MathTex("Z_B", color=RED).next_to(zug_b, UP, buff=0.6)

        v_b_arrow = Arrow(
            start=zug_b.get_top() + UP * 0.1,
            end=zug_b.get_top() + UP * 0.1 + LEFT * 1.2,
            color=RED,
            buff=0,
            stroke_width=4
        )
        v_b_label = MathTex("v_B = -60\\,\\text{km/h}", color=RED, font_size=26).next_to(v_b_arrow, UP, buff=0.1)

        dist_start = np.array([zug_a.get_center()[0], boden.get_y() - 0.4, 0])
        dist_end = np.array([zug_b.get_center()[0], boden.get_y() - 0.4, 0])
        dist_arrow = DoubleArrow(start=dist_start, end=dist_end, buff=0, color=WHITE)
        dist_label = MathTex("d = 20\\,\\text{km}", font_size=28).next_to(dist_arrow, DOWN, buff=0.15)

        x0_a = Dot(np.array([zug_a.get_center()[0], boden.get_y(), 0]), color=BLUE, radius=0.06)
        x0_a_label = MathTex("x_{0A} = 0", font_size=24, color=BLUE).next_to(x0_a, UP, buff=0.15)

        x0_b = Dot(np.array([zug_b.get_center()[0], boden.get_y(), 0]), color=RED, radius=0.06)
        x0_b_label = MathTex("x_{0B} = 20\\,\\text{km}", font_size=24, color=RED).next_to(x0_b, UP, buff=0.15)

        self.add(
            boden_gruppe,
            zug_a, label_a, v_a_arrow, v_a_label,
            zug_b, label_b, v_b_arrow, v_b_label,
            dist_arrow, dist_label,
            x0_a, x0_a_label, x0_b, x0_b_label
        )

class ZugBegegnungXTDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 2.5

        y_axis = Arrow(start=origin, end=origin + UP * 5.5, buff=0, color=WHITE)
        y_label = MathTex("x \\text{ (in km)}").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 7.0, buff=0, color=WHITE)
        x_label = MathTex("t \\text{ (in min)}").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        def to_point(t, x):
            return origin + RIGHT * (t * 0.45) + UP * (x * 0.225)

        p_a_start = to_point(0, 0)
        p_a_end = to_point(12, 20)
        line_a = Line(start=p_a_start, end=p_a_end, color=BLUE, stroke_width=4)
        label_a = MathTex("x_A(t) = v_A \\cdot t", font_size=24, color=BLUE).next_to(line_a.get_end(), UL, buff=0.1)

        p_b_start = to_point(0, 20)
        p_b_end = to_point(12, 8)
        line_b = Line(start=p_b_start, end=p_b_end, color=RED, stroke_width=4)
        label_b = MathTex("x_B(t) = x_0 - v_B \\cdot t", font_size=24, color=RED).next_to(p_b_start, RIGHT, buff=0.2)

        p_schnitt = to_point(7.5, 12.5)
        dot_schnitt = Dot(point=p_schnitt, color=YELLOW, radius=0.08)

        h_line_x = DashedLine(p_schnitt, np.array([p_schnitt[0], origin[1], 0]), color=GRAY, stroke_width=2)
        h_line_y = DashedLine(p_schnitt, np.array([origin[0], p_schnitt[1], 0]), color=GRAY, stroke_width=2)

        label_t_schnitt = MathTex("7{,}5", font_size=24).next_to(np.array([p_schnitt[0], origin[1], 0]), DOWN, buff=0.15)
        label_x_schnitt = MathTex("12{,}5", font_size=24).next_to(np.array([origin[0], p_schnitt[1], 0]), LEFT, buff=0.15)

        label_x0_b = MathTex("20", font_size=24, color=RED).next_to(p_b_start, LEFT, buff=0.15)

        text_treffpunkt = Text("Treffpunkt", font_size=18, color=YELLOW).next_to(p_schnitt, UP, buff=0.2)

        self.add(
            axes_group,
            line_a, label_a,
            line_b, label_b,
            dot_schnitt, text_treffpunkt,
            h_line_x, h_line_y,
            label_t_schnitt, label_x_schnitt, label_x0_b
        )

class HansAnnaXTDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 2.5

        y_axis = Arrow(start=origin, end=origin + UP * 5.5, buff=0, color=WHITE)
        y_label = MathTex("x \\text{ (in m)}").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 7.0, buff=0, color=WHITE)
        x_label = MathTex("t \\text{ (in s)}").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        def to_point(t, x):
            return origin + RIGHT * (t * 0.9) + UP * (x * 0.25)

        line_hans = Line(start=to_point(0, 0), end=to_point(7, 21), color=BLUE, stroke_width=4)
        label_hans = MathTex("x_H(t) = 3 \\cdot t", font_size=24, color=BLUE).next_to(to_point(3, 9), UL, buff=0.1)

        part1_anna = Line(start=to_point(0, 0), end=to_point(3, 0), color=RED, stroke_width=4)
        part2_anna = ParametricFunction(
            lambda t: to_point(t, 2 * (t - 3) ** 2),
            t_range=[3, 6.3],
            stroke_width=4,
            color=RED
        )
        graph_anna = VGroup(part1_anna, part2_anna)
        label_anna = MathTex("x_A(t) = 2(t-3)^2", font_size=24, color=RED).next_to(to_point(5, 8), DR, buff=0.1)

        p_t3_hans = to_point(3, 9)
        dot_hans_t3 = Dot(p_t3_hans, color=YELLOW, radius=0.06)
        h_line_x3 = DashedLine(p_t3_hans, np.array([p_t3_hans[0], origin[1], 0]), color=GRAY, stroke_width=2)
        h_line_y9 = DashedLine(p_t3_hans, np.array([origin[0], p_t3_hans[1], 0]), color=GRAY, stroke_width=2)

        label_t3 = MathTex("3", font_size=24).next_to(np.array([p_t3_hans[0], origin[1], 0]), DOWN, buff=0.15)
        label_x9 = MathTex("9", font_size=24).next_to(np.array([origin[0], p_t3_hans[1], 0]), LEFT, buff=0.15)

        p_schnitt = to_point(6.0, 18.0)
        dot_schnitt = Dot(p_schnitt, color=YELLOW, radius=0.08)

        h_line_x6 = DashedLine(p_schnitt, np.array([p_schnitt[0], origin[1], 0]), color=GRAY, stroke_width=2)
        h_line_y18 = DashedLine(p_schnitt, np.array([origin[0], p_schnitt[1], 0]), color=GRAY, stroke_width=2)

        label_t6 = MathTex("6", font_size=24).next_to(np.array([p_schnitt[0], origin[1], 0]), DOWN, buff=0.15)
        label_x18 = MathTex("18", font_size=24).next_to(np.array([origin[0], p_schnitt[1], 0]), LEFT, buff=0.15)

        text_schnitt = Text("Überholpunkt", font_size=16, color=YELLOW).next_to(p_schnitt, UL, buff=0.15)

        self.add(
            axes_group,
            line_hans, label_hans,
            graph_anna, label_anna,
            dot_hans_t3, h_line_x3, h_line_y9, label_t3, label_x9,
            dot_schnitt, h_line_x6, h_line_y18, label_t6, label_x18, text_schnitt
        )