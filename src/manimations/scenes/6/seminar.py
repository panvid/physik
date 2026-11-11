from manim import *

class SeminarAufgabeGeneigteEbene(Scene):
    def construct(self):
        alpha_val = 22 * DEGREES
        b_len = 7.0
        h_len = b_len * np.tan(alpha_val)

        p_bottom_left = LEFT * 3.5 + DOWN * 1.5
        p_bottom_right = p_bottom_left + RIGHT * b_len
        p_top_right = p_bottom_right + UP * h_len

        ebene = Polygon(p_bottom_left, p_bottom_right, p_top_right, color=WHITE, stroke_width=3)

        winkel_bogen = Arc(
            radius=1.2,
            start_angle=0,
            angle=alpha_val,
            arc_center=p_bottom_left,
            color=WHITE
        )
        winkel_label = MathTex(r"\alpha").next_to(winkel_bogen, RIGHT, buff=0.15).shift(UP * 0.1)

        hyp_vec = p_top_right - p_bottom_left
        unit_hyp = hyp_vec / np.linalg.norm(hyp_vec)
        normal_vec = np.array([-unit_hyp[1], unit_hyp[0], 0])

        box_width = 1.4
        box_height = 0.8
        t_param = 0.45
        box_center_ramp = p_bottom_left + t_param * hyp_vec
        box_center = box_center_ramp + normal_vec * (box_height / 2.0)

        koerper = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.3, stroke_width=3)
        koerper.rotate(alpha_val)
        koerper.move_to(box_center)

        v_start = box_center + normal_vec * (box_height / 2.0 + 0.35)
        arrow_v = Arrow(v_start, v_start + unit_hyp * 1.8, buff=0, color=WHITE, stroke_width=3,
                        max_tip_length_to_length_ratio=0.25)
        label_v = MathTex(r"\vec{v}", color=WHITE).next_to(arrow_v, UP + LEFT, buff=0.1)

        fg_scale = 2.2
        v_FG = DOWN * fg_scale
        v_FN = normal_vec * (fg_scale * np.cos(alpha_val))
        v_FH = -unit_hyp * (fg_scale * np.sin(alpha_val))
        v_FGN = -v_FN

        arrow_FG = Arrow(box_center, box_center + v_FG, buff=0, color=RED, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        arrow_FN = Arrow(box_center, box_center + v_FN, buff=0, color=GREEN, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        arrow_FH = Arrow(box_center, box_center + v_FH, buff=0, color=YELLOW, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        arrow_FGN = Arrow(box_center, box_center + v_FGN, buff=0, color=ORANGE, stroke_width=4,
                          max_tip_length_to_length_ratio=0.2)

        label_FG = MathTex(r"F_{\text{G}}", color=RED).next_to(arrow_FG.get_end(), DOWN)
        label_FN = MathTex(r"F_{\text{N}}", color=GREEN).next_to(arrow_FN.get_end(), UP + LEFT, buff=0.1)
        label_FH = MathTex(r"F_{\text{H}}", color=YELLOW).next_to(arrow_FH.get_end(), DOWN + LEFT, buff=0.1)
        label_FGN = MathTex(r"F_{\text{GN}}", color=ORANGE).next_to(arrow_FGN.get_end(), DOWN + RIGHT, buff=0.1)

        self.add(
            ebene, winkel_bogen, winkel_label,
            koerper,
            arrow_v, label_v,
            arrow_FG, label_FG,
            arrow_FN, label_FN,
            arrow_FH, label_FH,
            arrow_FGN, label_FGN
        )