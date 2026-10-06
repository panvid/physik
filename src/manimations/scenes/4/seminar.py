from manim import *
import math

class LaterneAufgabeSkizzeExaktParallelKuerzer(Scene):
    def construct(self):
        s1_val = 1.0
        s2_val = 1.2
        cos_alpha = s1_val / s2_val
        alpha_rad = math.acos(cos_alpha)

        wall_x = -3.5
        p_x = 0.5
        p_y = 0.2
        pt_p = RIGHT * p_x + UP * p_y

        dist_s1 = p_x - wall_x
        h_s2 = dist_s1 * math.tan(alpha_rad)

        pt_wall_s1 = RIGHT * wall_x + UP * pt_p[1]
        pt_wall_s2 = RIGHT * wall_x + UP * (pt_p[1] - h_s2)

        wall_top = pt_p[1] + 1.2
        wall_bottom = pt_wall_s2[1] - 1.2

        wall_rect = Rectangle(height=wall_top - wall_bottom, width=0.8, color=GRAY_C, fill_opacity=0.3)
        wall_rect.move_to(RIGHT * (wall_x - 0.4) + UP * ((wall_top + wall_bottom) / 2))

        brick_lines = VGroup()
        for y_pos in [wall_bottom + i * 0.4 for i in range(int((wall_top - wall_bottom) / 0.4) + 1)]:
            brick_lines.add(Line(RIGHT * wall_x + UP * y_pos, RIGHT * (wall_x - 0.8) + UP * y_pos, color=GRAY_B, stroke_width=1.5))

        line_s1 = Line(pt_wall_s1, pt_p, color=WHITE, stroke_width=5)
        label_s1 = MathTex("1", color=WHITE, font_size=36).next_to(line_s1.get_center(), UP, buff=0.15)

        line_s2 = Line(pt_wall_s2, pt_p, color=WHITE, stroke_width=5)
        label_s2 = MathTex("2", color=WHITE, font_size=36).next_to(line_s2.get_center(), DOWN + RIGHT, buff=0.15)

        lantern_chain = Line(pt_p, pt_p + DOWN * 0.8, color=GRAY_A, stroke_width=3)
        lantern_body = Polygon(
            pt_p + DOWN * 0.8 + LEFT * 0.3,
            pt_p + DOWN * 0.8 + RIGHT * 0.3,
            pt_p + DOWN * 1.8 + RIGHT * 0.2,
            pt_p + DOWN * 1.8 + LEFT * 0.2,
            color=GRAY_A,
            fill_color=GRAY_D,
            fill_opacity=0.8,
            stroke_width=2
        )
        lantern_group = VGroup(lantern_chain, lantern_body)

        f_len = 2.0
        arrow_fg = Arrow(pt_p, pt_p + DOWN * f_len, buff=0, color=RED_C, stroke_width=5)
        label_fg = MathTex(r"\vec{F}_G", color=RED_C, font_size=36).next_to(arrow_fg.get_end(), DOWN, buff=0.1)

        arrow_f = Arrow(pt_p, pt_p + UP * f_len, buff=0, color=YELLOW_C, stroke_width=5)
        label_f = MathTex(r"\vec{F}", color=YELLOW_C, font_size=36).next_to(arrow_f.get_center(), LEFT, buff=0.15)

        pt_top_f = pt_p + UP * f_len
        f1_len = f_len / math.tan(alpha_rad)

        pt_f2_end = pt_top_f + RIGHT * f1_len

        arrow_f2 = Arrow(
            pt_p,
            pt_f2_end,
            buff=0,
            color=GREEN_C,
            stroke_width=5
        )
        label_f2 = MathTex(r"\vec{F}_2", color=GREEN_C, font_size=34).next_to(arrow_f2.get_center(), DOWN + RIGHT, buff=0.1)

        arrow_f1 = Arrow(
            pt_f2_end,
            pt_top_f,
            buff=0,
            color=BLUE_C,
            stroke_width=5
        )
        label_f1 = MathTex(r"\vec{F}_1", color=BLUE_C, font_size=34).next_to(arrow_f1.get_center(), UP, buff=0.15)

        dot_p = Dot(pt_p, radius=0.1, color=WHITE)
        label_p = MathTex("P", font_size=38).next_to(dot_p, DOWN + LEFT, buff=0.1)

        self.add(
            wall_rect, brick_lines,
            line_s1, label_s1,
            line_s2, label_s2,
            lantern_group,
            arrow_fg, label_fg,
            arrow_f, label_f,
            arrow_f2, label_f2,
            arrow_f1, label_f1,
            dot_p, label_p
        )

class KraeftedreieckLaterneKorrektWinkel(Scene):
    def construct(self):
        s1_val = 1.0
        s2_val = 1.2
        cos_alpha = s1_val / s2_val
        alpha_rad = math.acos(cos_alpha)

        pt_p = LEFT * 0.5 + DOWN * 0.5
        f_len = 2.5

        pt_rod1_end = pt_p + LEFT * 3.0
        pt_rod2_end = pt_p + LEFT * 3.0 + DOWN * (3.0 * math.tan(alpha_rad))

        line_rod1 = Line(pt_p, pt_rod1_end, color=WHITE, stroke_width=4)
        label_rod1 = MathTex("1", color=WHITE, font_size=32).next_to(line_rod1.get_center(), UP, buff=0.1)

        line_rod2 = Line(pt_p, pt_rod2_end, color=WHITE, stroke_width=4)
        label_rod2 = MathTex("2", color=WHITE, font_size=32).next_to(line_rod2.get_center(), DOWN + LEFT, buff=0.1)

        arrow_fg = Arrow(pt_p, pt_p + DOWN * f_len, buff=0, color=RED_C, stroke_width=5)
        label_fg = MathTex(r"\vec{F}_G", color=RED_C, font_size=36).next_to(arrow_fg.get_end(), DOWN, buff=0.1)

        arrow_f = Arrow(pt_p, pt_p + UP * f_len, buff=0, color=YELLOW_C, stroke_width=5)
        label_f = MathTex(r"\vec{F}", color=YELLOW_C, font_size=36).next_to(arrow_f.get_center(), LEFT, buff=0.15)

        pt_top_f = pt_p + UP * f_len
        f1_len = f_len / math.tan(alpha_rad)
        pt_f2_end = pt_top_f + RIGHT * f1_len

        arrow_f2 = Arrow(
            pt_p,
            pt_f2_end,
            buff=0,
            color=GREEN_C,
            stroke_width=5
        )
        label_f2 = MathTex(r"\vec{F}_2", color=GREEN_C, font_size=34).next_to(arrow_f2.get_center(), DOWN + RIGHT, buff=0.1)

        arrow_f1 = Arrow(
            pt_f2_end,
            pt_top_f,
            buff=0,
            color=BLUE_C,
            stroke_width=5
        )
        label_f1 = MathTex(r"\vec{F}_1", color=BLUE_C, font_size=34).next_to(arrow_f1.get_center(), UP, buff=0.15)

        arc_alpha_rods = Arc(
            radius=1.0,
            start_angle=math.pi,
            angle=alpha_rad,
            arc_center=pt_p,
            color=YELLOW_C,
            stroke_width=2.5
        )
        label_alpha_rods = MathTex(r"\alpha", color=YELLOW_C, font_size=30).move_to(
            pt_p + LEFT * 0.65 + DOWN * 0.25
        )

        arc_alpha_forces = Arc(
            radius=0.9,
            start_angle=math.pi,
            angle=alpha_rad,
            arc_center=pt_f2_end,
            color=YELLOW_C,
            stroke_width=2.5
        )
        label_alpha_forces = MathTex(r"\alpha", color=YELLOW_C, font_size=30).move_to(
            pt_f2_end + LEFT * 0.6 + DOWN * 0.25
        )

        dot_p = Dot(pt_p, radius=0.1, color=WHITE)
        label_p = MathTex("P", font_size=38).next_to(dot_p, DOWN + LEFT, buff=0.1)

        self.add(
            line_rod1, label_rod1,
            line_rod2, label_rod2,
            arrow_fg, label_fg,
            arrow_f, label_f,
            arrow_f2, label_f2,
            arrow_f1, label_f1,
            arc_alpha_rods, label_alpha_rods,
            arc_alpha_forces, label_alpha_forces,
            dot_p, label_p
        )

class KraeftedreieckMinimal(Scene):
    def construct(self):
        s1_val = 1.0
        s2_val = 1.2
        cos_alpha = s1_val / s2_val
        alpha_rad = math.acos(cos_alpha)

        origin = LEFT * 1.0 + DOWN * 1.5
        f_len = 3.0

        f1_len = f_len / math.tan(alpha_rad)

        pt_top_f = origin + UP * f_len
        pt_f1_end = pt_top_f + RIGHT * f1_len

        arrow_f = Arrow(origin, pt_top_f, buff=0, color=YELLOW_C, stroke_width=6)
        label_f = MathTex(r"\vec{F}", color=YELLOW_C, font_size=40).next_to(arrow_f.get_center(), LEFT, buff=0.15)

        arrow_f1 = Arrow(pt_top_f, pt_f1_end, buff=0, color=BLUE_C, stroke_width=6)
        label_f1 = MathTex(r"\vec{F}_1", color=BLUE_C, font_size=40).next_to(arrow_f1.get_center(), UP, buff=0.15)

        arrow_f2 = Arrow(pt_f1_end, origin, buff=0, color=GREEN_C, stroke_width=6)
        label_f2 = MathTex(r"\vec{F}_2", color=GREEN_C, font_size=40).next_to(arrow_f2.get_center(), DOWN + RIGHT, buff=0.15)

        arc_alpha = Arc(
            radius=1.0,
            start_angle=math.pi,
            angle=alpha_rad,
            arc_center=pt_f1_end,
            color=YELLOW_C,
            stroke_width=3
        )
        label_alpha = MathTex(r"\alpha", color=YELLOW_C, font_size=34).move_to(
            pt_f1_end + LEFT * 0.65 + DOWN * 0.25
        )

        dot_origin = Dot(origin, radius=0.08, color=WHITE)
        dot_top = Dot(pt_top_f, radius=0.08, color=WHITE)
        dot_right = Dot(pt_f1_end, radius=0.08, color=WHITE)

        self.add(
            arrow_f, label_f,
            arrow_f1, label_f1,
            arrow_f2, label_f2,
            arc_alpha, label_alpha,
            dot_origin, dot_top, dot_right
        )