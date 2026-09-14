from manim import *

class VtAbschnittsdiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 0.5

        y_axis = Arrow(start=origin + DOWN * 2.0, end=origin + UP * 3.5, buff=0, color=WHITE)
        y_label = MathTex("v \\text{ (in m/s)}").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 7.5, buff=0, color=WHITE)
        x_label = MathTex("t \\text{ (in s)}").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        def to_point(t, v):
            return origin + RIGHT * (t * 0.85) + UP * (v * 0.5)

        p1_start = to_point(0, 5)
        p1_end = to_point(2, 5)
        line1 = Line(p1_start, p1_end, color=BLUE, stroke_width=4)

        p2_start = to_point(2, 0)
        p2_end = to_point(4, 0)
        line2 = Line(p2_start, p2_end, color=BLUE, stroke_width=6)

        p3_start = to_point(4, -2.5)
        p3_end = to_point(6, -2.5)
        line3 = Line(p3_start, p3_end, color=BLUE, stroke_width=4)

        p4_start = to_point(6, 5)
        p4_end = to_point(8, 5)
        line4 = Line(p4_start, p4_end, color=BLUE, stroke_width=4)

        sprung1 = DashedLine(p1_end, p2_start, color=GRAY, stroke_width=2)
        sprung2 = DashedLine(p2_end, p3_start, color=GRAY, stroke_width=2)
        sprung3 = DashedLine(p3_end, p4_start, color=GRAY, stroke_width=2)

        h_v5 = DashedLine(p1_start, origin, color=GRAY, stroke_width=2)
        label_v5 = MathTex("5", font_size=24).next_to(origin + UP * 2.5, LEFT, buff=0.15)

        h_v_neg = DashedLine(p3_start, origin + DOWN * 1.25, color=GRAY, stroke_width=2)
        label_v_neg = MathTex("-2{,}5", font_size=24).next_to(origin + DOWN * 1.25, LEFT, buff=0.15)

        label_t2 = MathTex("2", font_size=24).next_to(to_point(2, 0), DOWN, buff=0.15)
        label_t4 = MathTex("4", font_size=24).next_to(to_point(4, 0), UP, buff=0.15)

        h_t6 = DashedLine(to_point(6, 0), p3_end, color=GRAY, stroke_width=2)
        label_t6 = MathTex("6", font_size=24).next_to(to_point(6, 0), UP, buff=0.15)

        self.add(
            axes_group,
            line1, line2, line3, line4,
            sprung1, sprung2, sprung3,
            h_v5, label_v5,
            h_v_neg, label_v_neg,
            label_t2, label_t4, label_t6, h_t6
        )