from manim import *

class SeminarAufgabe1StDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 2.5

        y_axis = Arrow(start=origin, end=origin + UP * 5.5, buff=0, color=WHITE)
        y_label = MathTex("s \\text{ (in km)}").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 7.0, buff=0, color=WHITE)
        x_label = MathTex("t \\text{ (in h)}").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        def to_point(t, s):
            return origin + RIGHT * (t * 5.0) + UP * (s * 0.28125)

        p_start = to_point(0, 0)
        p_abschnitt1 = to_point(0.6, 12)
        p_ende = to_point(1.0, 16)

        linie1 = Line(start=p_start, end=p_abschnitt1, color=BLUE, stroke_width=4)
        linie2 = Line(start=p_abschnitt1, end=p_ende, color=TEAL, stroke_width=4)
        graph = VGroup(linie1, linie2)

        dot1 = Dot(point=p_abschnitt1, color=RED, radius=0.07)
        h_line1_x = DashedLine(p_abschnitt1, np.array([p_abschnitt1[0], origin[1], 0]), color=GRAY, stroke_width=2)
        h_line1_y = DashedLine(p_abschnitt1, np.array([origin[0], p_abschnitt1[1], 0]), color=GRAY, stroke_width=2)

        label_t1 = MathTex("0{,}6", font_size=24).next_to(np.array([p_abschnitt1[0], origin[1], 0]), DOWN, buff=0.15)
        label_s1 = MathTex("12", font_size=24).next_to(np.array([origin[0], p_abschnitt1[1], 0]), LEFT, buff=0.15)

        dot2 = Dot(point=p_ende, color=RED, radius=0.07)
        h_line2_x = DashedLine(p_ende, np.array([p_ende[0], origin[1], 0]), color=GRAY, stroke_width=2)
        h_line2_y = DashedLine(p_ende, np.array([origin[0], p_ende[1], 0]), color=GRAY, stroke_width=2)

        label_t2 = MathTex("1{,}0", font_size=24).next_to(np.array([p_ende[0], origin[1], 0]), DOWN, buff=0.15)
        label_s2 = MathTex("16", font_size=24).next_to(np.array([origin[0], p_ende[1], 0]), LEFT, buff=0.15)

        text_abschnitt1 = MathTex("v_1 = 20\\,\\text{km/h}", font_size=22, color=BLUE).next_to(linie1.get_center(), UL, buff=0.1)
        text_abschnitt2 = MathTex("v_2 = 10\\,\\text{km/h}", font_size=22, color=TEAL).next_to(linie2.get_center(), UL, buff=0.1)

        self.add(
            axes_group,
            graph,
            dot1, dot2,
            h_line1_x, h_line1_y, label_t1, label_s1,
            h_line2_x, h_line2_y, label_t2, label_s2,
            text_abschnitt1, text_abschnitt2
        )

class SeminarAufgabe1VtDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 2.5

        y_axis = Arrow(start=origin, end=origin + UP * 5.5, buff=0, color=WHITE)
        y_label = MathTex("v \\text{ (in km/h)}").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 7.0, buff=0, color=WHITE)
        x_label = MathTex("t \\text{ (in h)}").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        def to_point(t, v):
            return origin + RIGHT * (t * 5.0) + UP * (v * 0.18)

        p1_start = to_point(0, 20)
        p1_end = to_point(0.6, 20)
        line_v1 = Line(start=p1_start, end=p1_end, color=BLUE, stroke_width=5)

        p2_start = to_point(0.6, 10)
        p2_end = to_point(1.0, 10)
        line_v2 = Line(start=p2_start, end=p2_end, color=TEAL, stroke_width=5)

        line_sprung = DashedLine(start=p1_end, end=p2_start, color=GRAY, stroke_width=2)

        h_v1 = DashedLine(p1_start, np.array([origin[0], p1_start[1], 0]), color=GRAY, stroke_width=2)
        label_v1 = MathTex("20", font_size=24).next_to(np.array([origin[0], p1_start[1], 0]), LEFT, buff=0.15)

        h_v2 = DashedLine(p2_start, np.array([origin[0], p2_start[1], 0]), color=GRAY, stroke_width=2)
        label_v2 = MathTex("10", font_size=24).next_to(np.array([origin[0], p2_start[1], 0]), LEFT, buff=0.15)

        h_t1 = DashedLine(p2_start, np.array([p2_start[0], origin[1], 0]), color=GRAY, stroke_width=2)
        label_t1 = MathTex("0{,}6", font_size=24).next_to(np.array([p2_start[0], origin[1], 0]), DOWN, buff=0.15)

        h_t2 = DashedLine(p2_end, np.array([p2_end[0], origin[1], 0]), color=GRAY, stroke_width=2)
        label_t2 = MathTex("1{,}0", font_size=24).next_to(np.array([p2_end[0], origin[1], 0]), DOWN, buff=0.15)

        label_abschnitt1 = MathTex("s_1 = 12\\,\\text{km}", font_size=22, color=BLUE).next_to(line_v1, UP, buff=0.15)
        label_abschnitt2 = MathTex("s_2 = 4\\,\\text{km}", font_size=22, color=TEAL).next_to(line_v2, UP, buff=0.15)

        self.add(
            axes_group,
            line_v1, line_v2, line_sprung,
            h_v1, h_v2, h_t1, h_t2,
            label_v1, label_v2, label_t1, label_t2,
            label_abschnitt1, label_abschnitt2
        )