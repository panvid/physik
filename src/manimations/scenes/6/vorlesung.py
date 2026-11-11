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

class Kraefteparallelogramm(Scene):
    def construct(self):
        alpha_val = 32 * DEGREES
        L = 4.0

        O = UP * 1.8
        P_G = O + DOWN * L

        u_H = np.array([np.cos(alpha_val), -np.sin(alpha_val), 0])
        u_GH = np.array([-np.sin(alpha_val), -np.cos(alpha_val), 0])

        P_H = O + u_H * (L * np.sin(alpha_val))
        P_GH = O + u_GH * (L * np.cos(alpha_val))

        arrow_FG = Arrow(O, P_G, buff=0, color=RED, stroke_width=4, max_tip_length_to_length_ratio=0.15)
        arrow_FGH = Arrow(O, P_GH, buff=0, color=ORANGE, stroke_width=4, max_tip_length_to_length_ratio=0.15)
        arrow_FH = Arrow(O, P_H, buff=0, color=YELLOW, stroke_width=4, max_tip_length_to_length_ratio=0.15)

        dash_left = DashedLine(P_GH, P_G, color=WHITE, stroke_width=2)
        dash_right = DashedLine(P_H, P_G, color=WHITE, stroke_width=2)

        line_FGH = Line(O, P_GH)
        line_FG = Line(O, P_G)
        line_FH = Line(O, P_H)
        line_dash_left = Line(P_GH, P_G)
        line_dash_right = Line(P_H, P_G)
        line_FG_rev = Line(P_G, O)
        line_dash_right_rev = Line(P_G, P_H)

        right_angle_left = RightAngle(line_FGH, line_dash_left, length=0.3, color=WHITE)
        right_angle_right = RightAngle(line_FH, line_dash_right, length=0.3, color=WHITE)

        angle_top_left = Angle(line_FGH, line_FG, radius=0.8, color=WHITE)
        label_alpha_top = MathTex(r"\alpha").next_to(angle_top_left, DOWN, buff=0.1).shift(LEFT * 0.05)

        angle_bottom_right = Angle(line_dash_right_rev, line_FG_rev, radius=0.8, color=WHITE)
        label_alpha_bottom = MathTex(r"\alpha").next_to(angle_bottom_right, UP, buff=0.1).shift(RIGHT * 0.05)

        label_FG = MathTex(r"F_{\text{G}}", color=RED).next_to(P_G, DOWN, buff=0.15)
        label_FGH = MathTex(r"F_{\text{GH}}", color=ORANGE).next_to(P_GH, DOWN + LEFT, buff=0.15)
        label_FH = MathTex(r"F_{\text{H}}", color=YELLOW).next_to(P_H, UP + RIGHT, buff=0.15)

        self.add(
            arrow_FG, arrow_FGH, arrow_FH,
            dash_left, dash_right,
            right_angle_left, right_angle_right,
            angle_top_left, label_alpha_top,
            angle_bottom_right, label_alpha_bottom,
            label_FG, label_FGH, label_FH
        )

class GeneigteEbeneEinfach(Scene):
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

        hyp_vec = p_right_bottom - p_left_top
        unit_hyp = hyp_vec / np.linalg.norm(hyp_vec)
        normal_vec = np.array([-unit_hyp[1], unit_hyp[0], 0])

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
            koerper,
            arrow_FG, label_FG,
            arrow_FN, label_FN,
            arrow_FH, label_FH,
            arrow_FGN, label_FGN
        )

class HaftreibungSkizze(Scene):
    def construct(self):
        boden = Line(LEFT * 4, RIGHT * 4, color=WHITE, stroke_width=3)

        box_width = 2.0
        box_height = 1.0
        box_center = UP * (box_height / 2.0)
        koerper = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.3, stroke_width=3)
        koerper.move_to(box_center)

        kraft_laenge = 2.5
        arrow_fzug = Arrow(box_center, box_center + RIGHT * kraft_laenge, buff=0, color=YELLOW, stroke_width=4,
                           max_tip_length_to_length_ratio=0.2)
        arrow_fhaft = Arrow(box_center, box_center + LEFT * kraft_laenge, buff=0, color=RED, stroke_width=4,
                            max_tip_length_to_length_ratio=0.2)

        label_fzug = MathTex(r"F_{\text{Zug}}", color=YELLOW).next_to(arrow_fzug.get_end(), RIGHT)
        label_fhaft = MathTex(r"F_{\text{Haft}}", color=RED).next_to(arrow_fhaft.get_end(), LEFT)

        gleichung = MathTex(r"F_{\text{Haft}} = F_{\text{Zug}}", font_size=42)
        gleichung.move_to(DOWN * 1.8)

        self.add(
            boden, koerper,
            arrow_fzug, label_fzug,
            arrow_fhaft, label_fhaft,
            gleichung
        )

class GleitreibungSkizze(Scene):
    def construct(self):
        boden = Line(LEFT * 4, RIGHT * 4, color=WHITE, stroke_width=3)

        box_width = 2.0
        box_height = 1.0
        box_center = UP * (box_height / 2.0)
        koerper = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.3, stroke_width=3)
        koerper.move_to(box_center)

        v_start = box_center + UP * 0.8
        v_end = v_start + RIGHT * 1.5
        arrow_v = Arrow(v_start, v_end, buff=0, color=WHITE, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        label_v = MathTex(r"v", color=WHITE).next_to(arrow_v, UP, buff=0.1)

        kraft_laenge = 2.5
        arrow_fzug = Arrow(box_center, box_center + RIGHT * kraft_laenge, buff=0, color=YELLOW, stroke_width=4,
                           max_tip_length_to_length_ratio=0.2)
        arrow_fr = Arrow(box_center, box_center + LEFT * kraft_laenge, buff=0, color=RED, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)

        label_fzug = MathTex(r"F_{\text{Zug}}", color=YELLOW).next_to(arrow_fzug.get_end(), RIGHT)
        label_fr = MathTex(r"F_{\text{R}}", color=RED).next_to(arrow_fr.get_end(), LEFT)

        self.add(
            boden, koerper,
            arrow_v, label_v,
            arrow_fzug, label_fzug,
            arrow_fr, label_fr
        )

class RollreibungSkizze(Scene):
    def construct(self):
        wheel_radius = 0.35
        boden = Line(LEFT * 4 + DOWN * wheel_radius, RIGHT * 4 + DOWN * wheel_radius, color=WHITE, stroke_width=3)

        wheel_left = Circle(radius=wheel_radius, color=WHITE, stroke_width=3)
        wheel_left.move_to(LEFT * 0.8)
        wheel_right = Circle(radius=wheel_radius, color=WHITE, stroke_width=3)
        wheel_right.move_to(RIGHT * 0.8)

        box_width = 2.4
        box_height = 0.9
        box_center = UP * (box_height / 2.0 + 0.05)
        koerper = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.3, stroke_width=3)
        koerper.move_to(box_center)

        v_start = box_center + UP * 0.85
        v_end = v_start + RIGHT * 1.5
        arrow_v = Arrow(v_start, v_end, buff=0, color=WHITE, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        label_v = MathTex(r"v = \text{konst.}", color=WHITE).next_to(arrow_v, UP, buff=0.1)

        kraft_laenge = 2.5
        arrow_fzug = Arrow(box_center, box_center + RIGHT * kraft_laenge, buff=0, color=YELLOW, stroke_width=4,
                           max_tip_length_to_length_ratio=0.2)
        arrow_fr = Arrow(box_center, box_center + LEFT * kraft_laenge, buff=0, color=RED, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)

        label_fzug = MathTex(r"F_{\text{Zug}}", color=YELLOW).next_to(arrow_fzug.get_end(), RIGHT)
        label_fr = MathTex(r"F_{\text{R}}", color=RED).next_to(arrow_fr.get_end(), LEFT)

        self.add(
            boden, wheel_left, wheel_right, koerper,
            arrow_v, label_v,
            arrow_fzug, label_fzug,
            arrow_fr, label_fr
        )

class BestimmungMuHSkizze(Scene):
    def construct(self):
        boden = Line(LEFT * 4, RIGHT * 4, color=WHITE, stroke_width=3)

        box_width = 2.0
        box_height = 1.0
        box_center = UP * (box_height / 2.0)
        koerper = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.3, stroke_width=3)
        koerper.move_to(box_center)

        kraft_laenge = 2.5
        arrow_fzug = Arrow(box_center, box_center + RIGHT * kraft_laenge, buff=0, color=YELLOW, stroke_width=4,
                           max_tip_length_to_length_ratio=0.2)
        arrow_fhaft = Arrow(box_center, box_center + LEFT * kraft_laenge, buff=0, color=RED, stroke_width=4,
                            max_tip_length_to_length_ratio=0.2)

        label_fzug = MathTex(r"F_{\text{Zug}}", color=YELLOW).next_to(arrow_fzug.get_end(), RIGHT)
        label_fhaft = MathTex(r"F_{\text{Haft}}", color=RED).next_to(arrow_fhaft.get_end(), LEFT)

        self.add(
            boden, koerper,
            arrow_fzug, label_fzug,
            arrow_fhaft, label_fhaft
        )

class BestimmungMuHGeneigteEbene(Scene):
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

        hyp_vec = p_right_bottom - p_left_top
        unit_hyp = hyp_vec / np.linalg.norm(hyp_vec)
        normal_vec = np.array([-unit_hyp[1], unit_hyp[0], 0])

        box_width = 1.4
        box_height = 0.8
        t_param = 0.45
        box_center_ramp = p_left_top + t_param * hyp_vec
        box_center = box_center_ramp + normal_vec * (box_height / 2.0)

        koerper = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.3, stroke_width=3)
        koerper.rotate(-alpha_val)
        koerper.move_to(box_center)

        fg_scale = 2.2
        v_FN = normal_vec * (fg_scale * np.cos(alpha_val))
        v_FH = unit_hyp * (fg_scale * np.sin(alpha_val))
        v_FGN = -v_FN
        v_FHaft = -v_FH

        arrow_FN = Arrow(box_center, box_center + v_FN, buff=0, color=GREEN, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        arrow_FH = Arrow(box_center, box_center + v_FH, buff=0, color=YELLOW, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        arrow_FGN = Arrow(box_center, box_center + v_FGN, buff=0, color=ORANGE, stroke_width=4,
                          max_tip_length_to_length_ratio=0.2)
        arrow_FHaft = Arrow(box_center, box_center + v_FHaft, buff=0, color=RED, stroke_width=4,
                            max_tip_length_to_length_ratio=0.2)

        label_FN = MathTex(r"F_{\text{N}}", color=GREEN).next_to(arrow_FN.get_end(), UP + RIGHT, buff=0.1)
        label_FH = MathTex(r"F_{\text{H}}", color=YELLOW).next_to(arrow_FH.get_end(), DOWN + RIGHT, buff=0.1)
        label_FGN = MathTex(r"F_{\text{GN}}", color=ORANGE).next_to(arrow_FGN.get_end(), DOWN + LEFT, buff=0.1)
        label_FHaft = MathTex(r"F_{\text{Haft}}", color=RED).next_to(arrow_FHaft.get_end(), UP + LEFT, buff=0.1)

        self.add(
            ebene, winkel_bogen, winkel_label,
            koerper,
            arrow_FN, label_FN,
            arrow_FH, label_FH,
            arrow_FGN, label_FGN,
            arrow_FHaft, label_FHaft
        )

class FesteRolle(Scene):
    def construct(self):
        decke = Line(LEFT * 2.5 + UP * 3, RIGHT * 2.5 + UP * 3, color=WHITE, stroke_width=4)

        hatch_lines = []
        for x in np.linspace(-2.3, 2.3, 12):
            hatch_lines.append(Line(np.array([x, 3.0, 0]), np.array([x + 0.2, 3.25, 0]), color=WHITE, stroke_width=1.5))

        pulley_center = UP * 1.5
        pulley_radius = 0.8

        befestigung = Line(UP * 3, pulley_center, color=WHITE, stroke_width=3)
        rolle_outer = Circle(radius=pulley_radius, color=WHITE, stroke_width=3).move_to(pulley_center)
        rolle_inner = Dot(pulley_center, radius=0.08, color=WHITE)

        left_x = pulley_center[0] - pulley_radius
        right_x = pulley_center[0] + pulley_radius

        rope_arc = Arc(radius=pulley_radius, start_angle=PI, angle=-PI, arc_center=pulley_center, color=GRAY,
                       stroke_width=3)
        rope_left = Line(np.array([left_x, pulley_center[1], 0]), np.array([left_x, -1.0, 0]), color=GRAY,
                         stroke_width=3)
        rope_right = Line(np.array([right_x, pulley_center[1], 0]), np.array([right_x, -0.0, 0]), color=GRAY,
                          stroke_width=3)

        p_left_end = np.array([left_x, -1.0, 0])
        arrow_fzug = Arrow(p_left_end, p_left_end + DOWN * 1.8, buff=0, color=YELLOW, stroke_width=4,
                           max_tip_length_to_length_ratio=0.2)
        label_fzug = MathTex(r"F_{\text{Zug}}", color=YELLOW).next_to(arrow_fzug.get_end(), DOWN)

        arrow_szug = Arrow(p_left_end + LEFT * 0.6, p_left_end + LEFT * 0.6 + UP * 1.5, buff=0, color=BLUE,
                           stroke_width=3, max_tip_length_to_length_ratio=0.2)
        label_szug = MathTex(r"s_{\text{Zug}}", color=BLUE).next_to(arrow_szug, LEFT)

        box_side = 1.0
        box_center = np.array([right_x, -0.5, 0])
        gewicht = Square(side_length=box_side, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to(box_center)

        arrow_fhub = Arrow(box_center, box_center + UP * 1.6, buff=0, color=GREEN, stroke_width=4,
                           max_tip_length_to_length_ratio=0.2)
        label_fhub = MathTex(r"F_{\text{Hub}}", color=GREEN).next_to(arrow_fhub.get_end(), UP)

        arrow_fg = Arrow(box_center, box_center + DOWN * 1.8, buff=0, color=RED, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        label_fg = MathTex(r"F_{\text{G}}", color=RED).next_to(arrow_fg.get_end(), DOWN)

        arrow_shub = Arrow(box_center + RIGHT * 0.8, box_center + RIGHT * 0.8 + UP * 1.5, buff=0, color=TEAL,
                           stroke_width=3, max_tip_length_to_length_ratio=0.2)
        label_shub = MathTex(r"s_{\text{Hub}}", color=TEAL).next_to(arrow_shub, RIGHT)

        self.add(
            decke, *hatch_lines, befestigung,
            rolle_outer, rolle_inner,
            rope_arc, rope_left, rope_right,
            arrow_fzug, label_fzug,
            arrow_szug, label_szug,
            gewicht,
            arrow_fhub, label_fhub,
            arrow_fg, label_fg,
            arrow_shub, label_shub
        )

class LoseRolle(Scene):
    def construct(self):
        decke = Line(LEFT * 2.5 + UP * 3, RIGHT * 2.5 + UP * 3, color=WHITE, stroke_width=4)

        hatch_lines = []
        for x in np.linspace(-2.3, 2.3, 12):
            hatch_lines.append(Line(np.array([x, 3.0, 0]), np.array([x + 0.2, 3.25, 0]), color=WHITE, stroke_width=1.5))

        pulley_center = DOWN * 0.2
        pulley_radius = 0.8

        left_x = pulley_center[0] - pulley_radius
        right_x = pulley_center[0] + pulley_radius

        rolle_outer = Circle(radius=pulley_radius, color=WHITE, stroke_width=3).move_to(pulley_center)
        rolle_inner = Dot(pulley_center, radius=0.08, color=WHITE)

        befestigung_decke = Dot(np.array([right_x, 3.0, 0]), radius=0.08, color=WHITE)

        rope_right = Line(np.array([right_x, 3.0, 0]), np.array([right_x, pulley_center[1], 0]), color=GRAY,
                          stroke_width=3)
        rope_arc = Arc(radius=pulley_radius, start_angle=0, angle=-PI, arc_center=pulley_center, color=GRAY,
                       stroke_width=3)
        rope_left = Line(np.array([left_x, pulley_center[1], 0]), np.array([left_x, 2.5, 0]), color=GRAY,
                         stroke_width=3)

        p_left_arrow = np.array([left_x, pulley_center[1] + 0.4, 0])
        arrow_fzug_left = Arrow(p_left_arrow, p_left_arrow + UP * 1.5, buff=0, color=YELLOW, stroke_width=4,
                                max_tip_length_to_length_ratio=0.2)
        label_fzug_left = MathTex(r"F_{\text{Zug}}", color=YELLOW).next_to(arrow_fzug_left, LEFT, buff=0.15)

        p_right_arrow = np.array([right_x, pulley_center[1] + 0.4, 0])
        arrow_fzug_right = Arrow(p_right_arrow, p_right_arrow + UP * 1.5, buff=0, color=YELLOW, stroke_width=4,
                                 max_tip_length_to_length_ratio=0.2)
        label_fzug_right = MathTex(r"F_{\text{Zug}}", color=YELLOW).next_to(arrow_fzug_right, RIGHT, buff=0.15)

        box_center = pulley_center + DOWN * 1.7
        box_side = 1.0

        hanger = Line(pulley_center, box_center + UP * (box_side / 2.0), color=WHITE, stroke_width=3)
        gewicht = Square(side_length=box_side, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to(box_center)

        arrow_fh = Arrow(box_center, box_center + UP * 1.4, buff=0, color=GREEN, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        label_fh = MathTex(r"F_{\text{H}}", color=GREEN).next_to(arrow_fh.get_end(), RIGHT, buff=0.15)

        arrow_fg = Arrow(box_center, box_center + DOWN * 1.6, buff=0, color=RED, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        label_fg = MathTex(r"F_{\text{G}}", color=RED).next_to(arrow_fg.get_end(), DOWN, buff=0.15)

        self.add(
            decke, *hatch_lines, befestigung_decke,
            rolle_outer, rolle_inner, hanger,
            rope_right, rope_arc, rope_left,
            arrow_fzug_left, label_fzug_left,
            arrow_fzug_right, label_fzug_right,
            gewicht,
            arrow_fh, label_fh,
            arrow_fg, label_fg
        )