from manim import *

class SeminarAufgabe2VtDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 0.5

        y_axis = Arrow(start=origin + DOWN * 3.0, end=origin + UP * 3.5, buff=0, color=WHITE)
        y_label = MathTex("v \\text{ (in m/s)}").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin + LEFT * 0.5, end=origin + RIGHT * 7.5, buff=0, color=WHITE)
        x_label = MathTex("t \\text{ (in s)}").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        def to_point(t, v):
            return origin + RIGHT * (t * 0.8) + UP * (v * 0.5)

        p1_start, p1_end = to_point(0, 5), to_point(2, 5)
        line1 = Line(p1_start, p1_end, color=BLUE, stroke_width=5)
        lbl1 = MathTex("v_{\\text{I}}", font_size=22, color=BLUE).next_to(line1, UP, buff=0.1)

        p2_start, p2_end = to_point(2, 0), to_point(4, 0)
        line2 = Line(p2_start, p2_end, color=TEAL, stroke_width=5)
        lbl2 = MathTex("v_{\\text{II}}", font_size=22, color=TEAL).next_to(line2, UP, buff=0.1)

        p3_start, p3_end = to_point(4, -2.5), to_point(6, -2.5)
        line3 = Line(p3_start, p3_end, color=YELLOW, stroke_width=5)
        lbl3 = MathTex("v_{\\text{III}}", font_size=22, color=YELLOW).next_to(line3, DOWN, buff=0.1)

        p4_start, p4_end = to_point(6, -5), to_point(8, -5)
        line4 = Line(p4_start, p4_end, color=RED, stroke_width=5)
        lbl4 = MathTex("v_{\\text{IV}}", font_size=22, color=RED).next_to(line4, DOWN, buff=0.1)

        graph = VGroup(line1, line2, line3, line4, lbl1, lbl2, lbl3, lbl4)

        jump12 = DashedLine(p1_end, p2_start, color=GRAY, stroke_width=2)
        jump23 = DashedLine(p2_end, p3_start, color=GRAY, stroke_width=2)
        jump34 = DashedLine(p3_end, p4_start, color=GRAY, stroke_width=2)
        jumps = VGroup(jump12, jump23, jump34)

        y_vals = [(5, "5"), (-2.5, "-2{,}5"), (-5, "-5")]
        y_labels_group = VGroup()
        for val, txt in y_vals:
            pt = to_point(0, val)
            dash = DashedLine(pt, np.array([origin[0] + 8.0 * 0.8, pt[1], 0]), color=GRAY, stroke_width=1)
            lbl = MathTex(txt, font_size=22).next_to(pt, LEFT, buff=0.15)
            y_labels_group.add(dash, lbl)

        x_vals = [(2, "2"), (4, "4"), (6, "6"), (8, "8")]
        x_labels_group = VGroup()
        for val, txt in x_vals:
            pt = to_point(val, 0)
            lbl = MathTex(txt, font_size=22).next_to(pt, DOWN, buff=0.15)
            x_labels_group.add(lbl)

        self.add(axes_group, graph, jumps, y_labels_group, x_labels_group)