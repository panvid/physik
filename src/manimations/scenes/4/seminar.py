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