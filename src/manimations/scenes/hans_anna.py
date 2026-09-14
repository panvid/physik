from manim import *

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