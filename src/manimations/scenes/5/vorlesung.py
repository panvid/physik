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