from manim import *

class AtwoodMaschine(Scene):
    def construct(self):
        pulley_center = UP * 0.5
        pulley_r = 0.6
        x_left = -0.6
        x_right = 0.6

        rolle = Circle(radius=pulley_r, color=WHITE, stroke_width=3).move_to(pulley_center)
        dot_rolle = Dot(pulley_center, radius=0.08, color=WHITE)

        p_left_rope_top = np.array([x_left, 0.5, 0])
        p_right_rope_top = np.array([x_right, 0.5, 0])

        rope_arc = Arc(radius=pulley_r, start_angle=PI, angle=-PI, arc_center=pulley_center, color=GRAY, stroke_width=3)

        y_m1 = -1.2
        y_m2 = -1.2

        p_m1 = np.array([x_left, y_m1, 0])
        p_m2 = np.array([x_right, y_m2, 0])

        rope_left = Line(p_left_rope_top, p_m1, color=GRAY, stroke_width=3)
        rope_right = Line(p_right_rope_top, p_m2, color=GRAY, stroke_width=3)

        box_w, box_h = 0.9, 0.7

        m1_box = Rectangle(width=box_w, height=box_h, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to(p_m1)
        label_m1 = MathTex("m_1", color=WHITE).move_to(p_m1)

        m2_box = Rectangle(width=box_w, height=box_h, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to(p_m2)
        label_m2 = MathTex("m_2", color=WHITE).move_to(p_m2)

        arrow_f1 = Arrow(p_m1, p_m1 + DOWN * 1.3, buff=0, color=RED, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        label_f1 = MathTex(r"F_1", color=RED).next_to(arrow_f1.get_end(), DOWN, buff=0.1)

        arrow_f2 = Arrow(p_m2, p_m2 + UP * 1.3, buff=0, color=GREEN, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        label_f2 = MathTex(r"F_2", color=GREEN).next_to(arrow_f2.get_end(), UP, buff=0.1)

        p_arrow_start = np.array([1.4, 1.2, 0])
        arrow_up = Arrow(p_arrow_start, p_arrow_start + UP * 1.3, buff=0, color=TEAL, stroke_width=3,
                         max_tip_length_to_length_ratio=0.25)

        x_brace = 2.2
        y_bottom = -1.2
        y_pulley = 0.5
        y_peak = 2.2

        p_h_start = np.array([x_brace, y_bottom, 0])
        p_h_end = np.array([x_brace, y_pulley, 0])
        brace_h = BraceBetweenPoints(p_h_start, p_h_end, direction=RIGHT)
        label_h = MathTex("h").next_to(brace_h, RIGHT, buff=0.15)

        p_dh_start = np.array([x_brace, y_pulley, 0])
        p_dh_end = np.array([x_brace, y_peak, 0])
        brace_dh = BraceBetweenPoints(p_dh_start, p_dh_end, direction=RIGHT)
        label_dh = MathTex(r"\Delta h").next_to(brace_dh, RIGHT, buff=0.15)

        dash_bottom = DashedLine(p_m2, np.array([x_brace + 0.3, y_bottom, 0]), color=GRAY, stroke_width=1.5)
        dash_pulley = DashedLine(pulley_center, np.array([x_brace + 0.3, y_pulley, 0]), color=GRAY, stroke_width=1.5)
        dash_peak = DashedLine(np.array([x_right, y_peak, 0]), np.array([x_brace + 0.3, y_peak, 0]), color=GRAY,
                               stroke_width=1.5)

        self.add(
            rolle, dot_rolle, rope_arc, rope_left, rope_right,
            m1_box, label_m1, m2_box, label_m2,
            arrow_f1, label_f1, arrow_f2, label_f2,
            arrow_up,
            dash_bottom, dash_pulley, dash_peak,
            brace_h, label_h, brace_dh, label_dh
        )