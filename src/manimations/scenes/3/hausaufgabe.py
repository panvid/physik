from manim import *

class LampenStatikSkizze(Scene):
    def construct(self):
        wall_top = Line(start=LEFT * 5 + UP * 2.5, end=RIGHT * 4 + UP * 2.5, stroke_width=4, color=WHITE)
        wall_left = Line(start=LEFT * 5 + UP * 2.5, end=LEFT * 5 + DOWN * 2, stroke_width=4, color=WHITE)

        hatch_lines = VGroup()
        for x in np.arange(-5, 4, 0.4):
            hatch_lines.add(Line(start=[x, 2.5, 0], end=[x + 0.2, 2.8, 0], stroke_width=1.5, color=GRAY))
        for y in np.arange(-2, 2.5, 0.4):
            hatch_lines.add(Line(start=[-5, y, 0], end=[-5.3, y + 0.2, 0], stroke_width=1.5, color=GRAY))

        p_point = LEFT * 0.5 + DOWN * 0.2
        anchor_top = RIGHT * 3 + UP * 2.5
        anchor_left = LEFT * 5 + DOWN * 0.2

        rope_1 = Line(start=anchor_left, end=p_point, stroke_width=2, color=LIGHT_GRAY)
        rope_2 = Line(start=p_point, end=anchor_top, stroke_width=2, color=LIGHT_GRAY)

        point_p = Dot(p_point, radius=0.08, color=WHITE)
        label_p = MathTex("P", font_size=32).next_to(point_p, UP + RIGHT, buff=0.1)

        label_1 = MathTex("1", font_size=30).next_to(rope_1, UP, buff=0.15)
        label_2 = MathTex("2", font_size=30).next_to(rope_2, DOWN + RIGHT, buff=0.1)

        rope_2_dir = p_point - anchor_top
        alpha_angle = np.arctan2(rope_2_dir[1], rope_2_dir[0])

        alpha_arc = Arc(
            radius=0.8,
            start_angle=PI,
            angle=alpha_angle - (-PI),
            arc_center=anchor_top,
            color=WHITE
        )
        label_alpha = MathTex(r"\alpha", font_size=32).next_to(anchor_top, LEFT * 1.8 + DOWN * 0.6, buff=0)

        vec_f1 = Arrow(start=p_point, end=p_point + LEFT * 1.8, buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        label_f1 = MathTex(r"\vec{F}_1", color=RED, font_size=32).next_to(vec_f1, DOWN, buff=0.1)

        vec_f2 = Arrow(start=p_point, end=p_point + (anchor_top - p_point) * 0.55, buff=0, color=GREEN,
                       max_tip_length_to_length_ratio=0.15)
        label_f2 = MathTex(r"\vec{F}_2", color=GREEN, font_size=32).next_to(vec_f2, UP + LEFT, buff=0.1)

        vec_fg = Arrow(start=p_point, end=p_point + DOWN * 2.0, buff=0, color=BLUE, max_tip_length_to_length_ratio=0.15)
        label_fg = MathTex(r"\vec{F}_G = 400\,\text{N}", color=BLUE, font_size=32).next_to(vec_fg, RIGHT, buff=0.15)

        lamp_body = Polygon(
            p_point + DOWN * 2.0 + LEFT * 0.6,
            p_point + DOWN * 2.0 + RIGHT * 0.6,
            p_point + DOWN * 2.5 + RIGHT * 0.9,
            p_point + DOWN * 2.5 + LEFT * 0.9,
            fill_color=YELLOW,
            fill_opacity=0.8,
            stroke_color=GOLD,
            stroke_width=2
        )

        self.add(
            wall_top, wall_left, hatch_lines,
            rope_1, rope_2,
            lamp_body,
            point_p, label_p,
            label_1, label_2,
            alpha_arc, label_alpha,
            vec_f1, label_f1,
            vec_f2, label_f2,
            vec_fg, label_fg
        )

class KraefteDreieckSkizze(Scene):
    def construct(self):
        p_start = LEFT * 1.5 + DOWN * 1.5

        vec_fg_end = p_start + UP * 3.0
        vec_fg = Arrow(start=p_start, end=vec_fg_end, buff=0, color=BLUE, max_tip_length_to_length_ratio=0.15)
        label_fg = MathTex(r"\vec{F}_G", color=BLUE, font_size=32).next_to(vec_fg, LEFT, buff=0.15)

        vec_f1_end = vec_fg_end + RIGHT * 4.0
        vec_f1 = Arrow(start=vec_fg_end, end=vec_f1_end, buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        label_f1 = MathTex(r"\vec{F}_1", color=RED, font_size=32).next_to(vec_f1, UP, buff=0.15)

        vec_f2 = Arrow(start=p_start, end=vec_f1_end, buff=0, color=GREEN, max_tip_length_to_length_ratio=0.15)
        label_f2 = MathTex(r"\vec{F}_2", color=GREEN, font_size=32).next_to(vec_f2, DOWN + RIGHT, buff=0.15)

        right_angle = RightAngle(
            Line(vec_fg_end, p_start),
            Line(vec_fg_end, vec_f1_end),
            length=0.35,
            color=WHITE
        )

        f2_dir = p_start - vec_f1_end
        f2_angle = np.arctan2(f2_dir[1], f2_dir[0])

        alpha_arc = Arc(
            radius=0.8,
            start_angle=PI,
            angle=f2_angle - (-PI),
            arc_center=vec_f1_end,
            color=WHITE
        )
        label_alpha = MathTex(r"\alpha", font_size=32).move_to(vec_f1_end + LEFT * 1.2 + DOWN * 0.3)

        self.add(
            vec_fg, label_fg,
            vec_f1, label_f1,
            vec_f2, label_f2,
            right_angle,
            alpha_arc, label_alpha
        )