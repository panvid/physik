from manim import *

class NormalkraftSkizze(Scene):
    def construct(self):
        ground_y = -1.5
        ground = Line(start=LEFT * 3.5, end=RIGHT * 3.5, color=WHITE, stroke_width=3).move_to(DOWN * 1.5)

        ground_hatches = VGroup()
        for x in np.linspace(-3.3, 3.3, 18):
            line = Line(
                start=np.array([x, ground_y, 0]),
                end=np.array([x - 0.25, ground_y - 0.3, 0]),
                color=GRAY,
                stroke_width=1.5
            )
            ground_hatches.add(line)

        box_width = 2.0
        box_height = 1.2
        box_center = np.array([0, ground_y + (box_height / 2.0), 0])

        box = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.4).move_to(box_center)
        box_label = MathTex("m").move_to(box_center)
        block = VGroup(box, box_label)

        vector_FN = Arrow(
            start=box_center,
            end=box_center + UP * 1.8,
            buff=0,
            color=GREEN
        )
        label_FN = MathTex("\\vec{F}_N").next_to(vector_FN, UP, buff=0.1)

        vector_FG = Arrow(
            start=box_center + LEFT * 0.35,
            end=box_center + LEFT * 0.35 + DOWN * 1.6,
            buff=0,
            color=YELLOW
        )
        label_FG = MathTex("\\vec{F}_G").next_to(vector_FG, DOWN + LEFT, buff=0.05)

        vector_F = Arrow(
            start=box_center + RIGHT * 0.35,
            end=box_center + RIGHT * 0.35 + DOWN * 1.6,
            buff=0,
            color=RED
        )
        label_F = MathTex("\\vec{F}").next_to(vector_F, DOWN + RIGHT, buff=0.05)

        self.add(
            ground, ground_hatches, block,
            vector_FN, label_FN,
            vector_FG, label_FG,
            vector_F, label_F
        )

class GeneigteEbene(Scene):
    def construct(self):
        alpha_val = 30 * DEGREES
        b_len = 6.0
        h_len = b_len * np.tan(alpha_val)

        p_left_bottom = LEFT * 3 + DOWN * 1.5
        p_right_bottom = p_left_bottom + RIGHT * b_len
        p_left_top = p_left_bottom + UP * h_len

        ebene = Polygon(p_left_bottom, p_right_bottom, p_left_top, color=WHITE, stroke_width=3)

        winkel_bogen = Arc(
            radius=1.0,
            start_angle=180 * DEGREES,
            angle=-alpha_val,
            arc_center=p_right_bottom,
            color=WHITE
        )
        winkel_label = MathTex(r"\alpha").next_to(winkel_bogen, LEFT, buff=0.15).shift(UP * 0.1)

        brace_h = BraceBetweenPoints(p_left_top, p_left_bottom, direction=LEFT)
        label_h = MathTex("h").next_to(brace_h, LEFT)

        brace_b = BraceBetweenPoints(p_left_bottom, p_right_bottom, direction=DOWN)
        label_b = MathTex("b").next_to(brace_b, DOWN)

        hyp_vec = p_right_bottom - p_left_top
        unit_hyp = hyp_vec / np.linalg.norm(hyp_vec)
        normal_vec = np.array([-unit_hyp[1], unit_hyp[0], 0])

        s_offset = normal_vec * 0.4
        s_start = p_left_top + s_offset
        s_end = p_right_bottom + s_offset
        s_arrow = DoubleArrow(s_start, s_end, tip_length=0.15, color=WHITE, stroke_width=2)
        label_s = MathTex("s").next_to(s_arrow, UP, buff=0.1)

        box_width = 1.4
        box_height = 0.8
        t_param = 0.45
        box_center_ramp = p_left_top + t_param * hyp_vec
        box_center = box_center_ramp + normal_vec * (box_height / 2.0)

        koerper = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.3, stroke_width=3)
        koerper.rotate(-alpha_val)
        koerper.move_to(box_center)

        fg_scale = 2.2
        v_FG = DOWN * fg_scale
        v_FN = normal_vec * (fg_scale * np.cos(alpha_val))
        v_FH = unit_hyp * (fg_scale * np.sin(alpha_val))
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
        label_FH = MathTex(r"F_{\text{H}}", color=YELLOW).next_to(arrow_FH.get_end(), DOWN + RIGHT, buff=0.1)
        label_FGN = MathTex(r"F_{\text{GN}}", color=ORANGE).next_to(arrow_FGN.get_end(), DOWN + LEFT, buff=0.1)

        self.add(
            ebene, winkel_bogen, winkel_label,
            brace_h, label_h, brace_b, label_b, s_arrow, label_s,
            koerper,
            arrow_FG, label_FG,
            arrow_FN, label_FN,
            arrow_FH, label_FH,
            arrow_FGN, label_FGN
        )