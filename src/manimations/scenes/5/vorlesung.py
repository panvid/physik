from manim import *

class ErdeGravitationSkizze(Scene):
    def construct(self):
        earth_radius = 2.2
        earth_center = ORIGIN

        earth = Circle(radius=earth_radius, color=BLUE_B, fill_color=BLUE_E, fill_opacity=0.3, stroke_width=3)

        point_m = Dot(earth_center, radius=0.08, color=WHITE)
        label_m = MathTex("M", font_size=32).next_to(point_m, DOWN + RIGHT, buff=0.1)

        def create_stick_figure(angle_rad):
            head_center = (earth_radius + 0.6) * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
            head = Circle(radius=0.15, color=WHITE, stroke_width=2).move_to(head_center)

            torso_start = (earth_radius + 0.45) * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
            torso_end = (earth_radius + 0.15) * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
            torso = Line(torso_start, torso_end, stroke_width=2, color=WHITE)

            tangent = np.array([-np.sin(angle_rad), np.cos(angle_rad), 0])
            arms = Line(
                torso_start - 0.1 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]) - 0.2 * tangent,
                torso_start - 0.1 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]) + 0.2 * tangent,
                stroke_width=2, color=WHITE
            )

            leg_left = Line(torso_end,
                            torso_end - 0.15 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]) - 0.12 * tangent,
                            stroke_width=2, color=WHITE)
            leg_right = Line(torso_end,
                             torso_end - 0.15 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]) + 0.12 * tangent,
                             stroke_width=2, color=WHITE)

            return VGroup(head, torso, arms, leg_left, leg_right)

        figure_top = create_stick_figure(PI / 2)
        figure_left = create_stick_figure(PI)
        figure_bottom = create_stick_figure(3 * PI / 2)

        start_top = (earth_radius + 0.15) * UP
        vec_fg_top = Arrow(start=start_top, end=start_top + DOWN * 1.3, buff=0, color=RED,
                           max_tip_length_to_length_ratio=0.15)
        label_fg_top = MathTex(r"\vec{F}_G", color=RED, font_size=30).next_to(vec_fg_top, RIGHT, buff=0.1)

        start_left = (earth_radius + 0.15) * LEFT
        vec_fg_left = Arrow(start=start_left, end=start_left + RIGHT * 1.3, buff=0, color=RED,
                            max_tip_length_to_length_ratio=0.15)
        label_fg_left = MathTex(r"\vec{F}_G", color=RED, font_size=30).next_to(vec_fg_left, UP, buff=0.1)

        start_bottom = (earth_radius + 0.15) * DOWN
        vec_fg_bottom = Arrow(start=start_bottom, end=start_bottom + UP * 1.3, buff=0, color=RED,
                              max_tip_length_to_length_ratio=0.15)
        label_fg_bottom = MathTex(r"\vec{F}_G", color=RED, font_size=30).next_to(vec_fg_bottom, RIGHT, buff=0.1)

        self.add(
            earth,
            point_m, label_m,
            figure_top, figure_left, figure_bottom,
            vec_fg_top, label_fg_top,
            vec_fg_left, label_fg_left,
            vec_fg_bottom, label_fg_bottom
        )

class ErdeEllipsenSkizze(Scene):
    def construct(self):
        earth_center = ORIGIN
        radius_x = 3.2
        radius_y = 1.8

        earth = Ellipse(width=radius_x * 2, height=radius_y * 2, color=BLUE_B, fill_color=BLUE_E, fill_opacity=0.3, stroke_width=3)

        point_np = Dot(earth_center + UP * radius_y, radius=0.08, color=WHITE)
        label_np = MathTex(r"\text{NP}", font_size=32).next_to(point_np, UP, buff=0.15)

        point_sp = Dot(earth_center + DOWN * radius_y, radius=0.08, color=WHITE)
        label_sp = MathTex(r"\text{SP}", font_size=32).next_to(point_sp, DOWN, buff=0.15)

        equator = DashedLine(
            start=earth_center + LEFT * radius_x,
            end=earth_center + RIGHT * radius_x,
            stroke_width=2,
            color=WHITE,
            dash_length=0.15
        )
        label_equator = MathTex(r"\text{Äquator}", font_size=30).next_to(equator, RIGHT, buff=0.15)

        self.add(
            earth,
            equator, label_equator,
            point_np, label_np,
            point_sp, label_sp
        )

class KraefteParallelogrammRechteckSkizze(Scene):
    def construct(self):
        mass_pos = DOWN * 2.0

        side_length = 2.0

        p_f1 = mass_pos + LEFT * side_length + UP * side_length
        p_f2 = mass_pos + RIGHT * side_length + UP * side_length
        p_f = mass_pos + UP * (2 * side_length)

        vec_f1 = Arrow(start=mass_pos, end=p_f1, buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        label_f1 = MathTex(r"\vec{F}_1", color=RED, font_size=32).next_to(vec_f1, UP + LEFT, buff=0.1)

        vec_f2 = Arrow(start=mass_pos, end=p_f2, buff=0, color=GREEN, max_tip_length_to_length_ratio=0.15)
        label_f2 = MathTex(r"\vec{F}_2", color=GREEN, font_size=32).next_to(vec_f2, UP + RIGHT, buff=0.1)

        vec_f = Arrow(start=mass_pos, end=p_f, buff=0, color=TEAL, max_tip_length_to_length_ratio=0.12)
        label_f = MathTex(r"\vec{F}", color=TEAL, font_size=32).next_to(vec_f, RIGHT, buff=0.15)

        vec_fg = Arrow(start=mass_pos, end=mass_pos + DOWN * (2 * side_length), buff=0, color=BLUE, max_tip_length_to_length_ratio=0.12)
        label_fg = MathTex(r"\vec{F}_G", color=BLUE, font_size=32).next_to(vec_fg, RIGHT, buff=0.15)

        dashed_left = DashedLine(start=p_f1, end=p_f, stroke_width=1.5, color=GRAY)
        dashed_right = DashedLine(start=p_f2, end=p_f, stroke_width=1.5, color=GRAY)

        ra_bottom = RightAngle(
            Line(mass_pos, p_f1),
            Line(mass_pos, p_f2),
            length=0.35,
            color=WHITE
        )

        ra_top = RightAngle(
            Line(p_f, p_f1),
            Line(p_f, p_f2),
            length=0.35,
            color=WHITE
        )

        ra_left = RightAngle(
            Line(p_f1, p_f),
            Line(p_f1, mass_pos),
            length=0.35,
            color=WHITE
        )

        ra_right = RightAngle(
            Line(p_f2, mass_pos),
            Line(p_f2, p_f),
            length=0.35,
            color=WHITE
        )

        mass_box = Square(side_length=0.6, fill_color=GRAY_D, fill_opacity=0.9, stroke_color=WHITE, stroke_width=2).move_to(mass_pos)
        label_m = MathTex("m", font_size=28, color=WHITE).move_to(mass_pos)

        self.add(
            dashed_left, dashed_right,
            vec_f1, label_f1,
            vec_f2, label_f2,
            vec_f, label_f,
            vec_fg, label_fg,
            ra_bottom, ra_top, ra_left, ra_right,
            mass_box, label_m
        )