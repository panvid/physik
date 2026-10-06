from manim import *

class BouncingBallVectors(Scene):
    def construct(self):
        ground = Line(start=LEFT * 6.0 + DOWN * 2.0, end=RIGHT * 6.0 + DOWN * 2.0, color=GRAY_A, stroke_width=4)
        ground_hatch = DashedLine(
            start=LEFT * 6.0 + DOWN * 2.1,
            end=RIGHT * 6.0 + DOWN * 2.1,
            color=GRAY_C,
            stroke_width=2
        )

        def arc1(t):
            x = -4.5 + 3.0 * t
            y = -2.0 + 3.5 * (1 - (2 * t - 1) ** 2)
            return RIGHT * x + UP * y

        def arc2(t):
            x = -1.5 + 3.0 * t
            y = -2.0 + 3.5 * (1 - (2 * t - 1) ** 2)
            return RIGHT * x + UP * y

        curve1_points = [arc1(t / 60.0) for t in range(61)]
        curve2_points = [arc2(t / 60.0) for t in range(61)]

        curve1 = VMobject(color=WHITE, stroke_width=3).set_points_smoothly(curve1_points)
        curve2 = VMobject(color=WHITE, stroke_width=3).set_points_smoothly(curve2_points)

        t_p = 0.75
        t_q = 0.25
        t_r = 0.50

        pos_p = arc1(t_p)
        pos_q = arc2(t_q)
        pos_r = arc2(t_r)

        dot_p = Dot(pos_p, radius=0.1, color=WHITE)
        dot_q = Dot(pos_q, radius=0.1, color=WHITE)
        dot_r = Dot(pos_r, radius=0.1, color=WHITE)

        label_p = MathTex("P", color=WHITE).next_to(dot_p, UP + LEFT, buff=0.1)
        label_q = MathTex("Q", color=WHITE).next_to(dot_q, UP + LEFT, buff=0.1)
        label_r = MathTex("R", color=WHITE).next_to(dot_r, UP, buff=0.1)

        v_p_dir = RIGHT * 1.0 + DOWN * 2.333
        v_p_dir = v_p_dir / np.linalg.norm(v_p_dir) * 1.5 if hasattr(v_p_dir, "norm") else (v_p_dir / (v_p_dir[0]**2 + v_p_dir[1]**2)**0.5) * 1.5

        v_q_dir = RIGHT * 1.0 + UP * 2.333
        v_q_dir = (v_q_dir / (v_q_dir[0]**2 + v_q_dir[1]**2)**0.5) * 1.5

        v_r_dir = RIGHT * 1.5

        arrow_vp = Arrow(pos_p, pos_p + v_p_dir, buff=0, color=BLUE_C, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        arrow_vq = Arrow(pos_q, pos_q + v_q_dir, buff=0, color=BLUE_C, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        arrow_vr = Arrow(pos_r, pos_r + v_r_dir, buff=0, color=BLUE_C, stroke_width=5, max_tip_length_to_length_ratio=0.2)

        label_vp = MathTex(r"\vec{v}_P", color=BLUE_C).next_to(arrow_vp.get_end(), RIGHT, buff=0.1)
        label_vq = MathTex(r"\vec{v}_Q", color=BLUE_C).next_to(arrow_vq.get_end(), UP, buff=0.1)
        label_vr = MathTex(r"\vec{v}_R", color=BLUE_C).next_to(arrow_vr.get_end(), RIGHT, buff=0.1)

        a_len = 1.2
        arrow_ap = Arrow(pos_p, pos_p + DOWN * a_len, buff=0, color=RED_C, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        arrow_aq = Arrow(pos_q, pos_q + DOWN * a_len, buff=0, color=RED_C, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        arrow_ar = Arrow(pos_r, pos_r + DOWN * a_len, buff=0, color=RED_C, stroke_width=5, max_tip_length_to_length_ratio=0.2)

        label_ap = MathTex(r"\vec{a}_P", color=RED_C).next_to(arrow_ap.get_end(), DOWN, buff=0.1)
        label_aq = MathTex(r"\vec{a}_Q", color=RED_C).next_to(arrow_aq.get_end(), DOWN, buff=0.1)
        label_ar = MathTex(r"\vec{a}_R", color=RED_C).next_to(arrow_ar.get_end(), DOWN, buff=0.1)

        self.add(
            ground, ground_hatch,
            curve1, curve2,
            dot_p, label_p,
            dot_q, label_q,
            dot_r, label_r,
            arrow_vp, label_vp,
            arrow_vq, label_vq,
            arrow_vr, label_vr,
            arrow_ap, label_ap,
            arrow_aq, label_aq,
            arrow_ar, label_ar
        )