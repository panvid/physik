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

class HookeschesGesetzSkizze(Scene):
    def construct(self):
        frame_bounds = Square(side_length=8, stroke_opacity=0).scale(1.777)

        ceiling_y = 3.2
        ceiling = Line(start=LEFT * 6, end=RIGHT * 6, stroke_width=4, color=WHITE)
        ceiling.move_to(np.array([0, ceiling_y, 0]))

        hatch_lines = VGroup()
        for x in np.arange(-6, 6, 0.4):
            hatch_lines.add(Line(start=[x, ceiling_y, 0], end=[x + 0.2, ceiling_y + 0.3, 0], stroke_width=1.5, color=GRAY))

        x_left = -2.0
        x_right = 2.0

        y_left_end = ceiling_y - 2.2
        y_right_end = ceiling_y - 4.8

        def create_spring(start_pt, length, num_coils=8, radius=0.25):
            pts = [start_pt]
            step = length / num_coils
            for i in range(num_coils):
                y_center = start_pt[1] - (i + 0.5) * step
                side = 1 if i % 2 == 0 else -1
                pts.append(np.array([start_pt[0] + side * radius, y_center, 0]))
            pts.append(np.array([start_pt[0], start_pt[1] - length, 0]))
            return VMobject(stroke_width=2, color=LIGHT_GRAY).set_points_as_corners(pts)

        spring_left = create_spring(np.array([x_left, ceiling_y, 0]), 2.2)
        spring_right = create_spring(np.array([x_right, ceiling_y, 0]), 4.8)

        p_left_end = np.array([x_left, y_left_end, 0])
        p_right_end = np.array([x_right, y_right_end, 0])

        dot_left = Dot(p_left_end, radius=0.06, color=WHITE)
        dot_right = Dot(p_right_end, radius=0.06, color=WHITE)

        dashed_top_ref = DashedLine(
            start=p_left_end,
            end=np.array([x_right, y_left_end, 0]),
            stroke_width=1.5,
            color=GRAY
        )

        dashed_bottom_ref = DashedLine(
            start=p_right_end,
            end=np.array([x_left, y_right_end, 0]),
            stroke_width=1.5,
            color=GRAY
        )

        x_arrow = 0.0
        arrow_delta_l = DoubleArrow(
            start=np.array([x_arrow, y_left_end, 0]),
            end=np.array([x_arrow, y_right_end, 0]),
            buff=0,
            stroke_width=2,
            color=WHITE,
            max_tip_length_to_length_ratio=0.12
        )
        label_delta_l = MathTex(r"\Delta l", font_size=32).next_to(arrow_delta_l, LEFT, buff=0.15)

        vec_f_feder = Arrow(start=p_right_end, end=p_right_end + UP * 1.4, buff=0, color=GREEN, max_tip_length_to_length_ratio=0.15)
        label_f_feder = MathTex(r"\vec{F}_{\text{Feder}}", color=GREEN, font_size=32).next_to(vec_f_feder, RIGHT, buff=0.15)

        vec_f = Arrow(start=p_right_end, end=p_right_end + DOWN * 1.4, buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        label_f = MathTex(r"\vec{F}", color=RED, font_size=32).next_to(vec_f, RIGHT, buff=0.15)

        self.add(
            frame_bounds,
            ceiling, hatch_lines,
            spring_left, spring_right,
            dot_left, dot_right,
            dashed_top_ref, dashed_bottom_ref,
            arrow_delta_l, label_delta_l,
            vec_f_feder, label_f_feder,
            vec_f, label_f
        )

class HookeDiagrammSkizze(Scene):
    def construct(self):
        frame_bounds = Square(side_length=8, stroke_opacity=0).scale(1.777)

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=5.5,
            y_length=4.5,
            axis_config={"color": WHITE, "include_tip": True, "tip_width": 0.2, "tip_height": 0.25},
            tips=True
        ).move_to(DOWN * 0.3 + LEFT * 0.5)

        label_x = MathTex(r"\text{Kraft } F", font_size=32).next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
        label_y = MathTex(r"\text{Dehnung } \Delta l", font_size=32).next_to(axes.y_axis.get_end(), UP, buff=0.15)

        graph = axes.plot(lambda x: 0.9 * x, x_range=[0, 4.8], color=BLUE, stroke_width=3)

        self.add(
            frame_bounds,
            axes, label_x, label_y,
            graph
        )

class FederKopplungSkizze(Scene):
    def construct(self):
        frame_bounds = Square(side_length=8, stroke_opacity=0).scale(1.777)

        ceiling_y = 2.7
        ceiling = Line(start=LEFT * 6, end=RIGHT * 6, stroke_width=4, color=WHITE)
        ceiling.move_to(np.array([0, ceiling_y, 0]))

        hatch_lines = VGroup()
        for x in np.arange(-6, 6, 0.4):
            hatch_lines.add(Line(start=[x, ceiling_y, 0], end=[x + 0.2, ceiling_y + 0.3, 0], stroke_width=1.5, color=GRAY))

        x_left = -2.5
        x_right = 2.0

        len_s1_unloaded = 1.1
        len_s2_unloaded = 1.1

        len_s1_loaded = 1.7
        len_s2_loaded = 1.7

        y_unloaded_mid = ceiling_y - len_s1_unloaded
        y_unloaded_end = ceiling_y - (len_s1_unloaded + len_s2_unloaded)

        y_loaded_mid = ceiling_y - len_s1_loaded
        y_loaded_end = ceiling_y - (len_s1_loaded + len_s2_loaded)

        def create_spring(start_pt, length, num_coils=6, radius=0.25):
            pts = [start_pt]
            step = length / num_coils
            for i in range(num_coils):
                y_center = start_pt[1] - (i + 0.5) * step
                side = 1 if i % 2 == 0 else -1
                pts.append(np.array([start_pt[0] + side * radius, y_center, 0]))
            pts.append(np.array([start_pt[0], start_pt[1] - length, 0]))
            return VMobject(stroke_width=2, color=LIGHT_GRAY).set_points_as_corners(pts)

        spring_left_1 = create_spring(np.array([x_left, ceiling_y, 0]), len_s1_unloaded)
        spring_left_2 = create_spring(np.array([x_left, y_unloaded_mid, 0]), len_s2_unloaded)

        label_d1_left = MathTex(r"D_1", font_size=32).next_to(spring_left_1, LEFT, buff=0.2)
        label_d2_left = MathTex(r"D_2", font_size=32).next_to(spring_left_2, LEFT, buff=0.2)

        spring_right_1 = create_spring(np.array([x_right, ceiling_y, 0]), len_s1_loaded)
        spring_right_2 = create_spring(np.array([x_right, y_loaded_mid, 0]), len_s2_loaded)

        p_mass_center = np.array([x_right, y_loaded_end - 0.4, 0])
        mass_box = Square(side_length=0.8, fill_color=GRAY_D, fill_opacity=0.9, stroke_color=WHITE, stroke_width=2).move_to(p_mass_center)
        label_m = MathTex("m", font_size=32, color=WHITE).next_to(mass_box, RIGHT, buff=0.2)

        vec_ff = Arrow(start=p_mass_center, end=p_mass_center + UP * 1.3, buff=0, color=GREEN, max_tip_length_to_length_ratio=0.15)
        label_ff = MathTex(r"\vec{F}_F", color=GREEN, font_size=32).next_to(vec_ff, LEFT, buff=0.15)

        vec_fg = Arrow(start=p_mass_center, end=p_mass_center + DOWN * 1.3, buff=0, color=BLUE, max_tip_length_to_length_ratio=0.15)
        label_fg = MathTex(r"\vec{F}_G", color=BLUE, font_size=32).next_to(vec_fg, RIGHT, buff=0.15)

        dashed_ref_unloaded = DashedLine(
            start=np.array([x_left, y_unloaded_end, 0]),
            end=np.array([x_right + 0.8, y_unloaded_end, 0]),
            stroke_width=1.5,
            color=GRAY
        )

        dashed_ref_loaded = DashedLine(
            start=np.array([x_right, y_loaded_end, 0]),
            end=np.array([x_left - 0.8, y_loaded_end, 0]),
            stroke_width=1.5,
            color=GRAY
        )

        x_arrow = (x_left + x_right) / 2
        arrow_delta_l = DoubleArrow(
            start=np.array([x_arrow, y_unloaded_end, 0]),
            end=np.array([x_arrow, y_loaded_end, 0]),
            buff=0,
            stroke_width=2,
            color=WHITE,
            max_tip_length_to_length_ratio=0.12
        )
        label_delta_l = MathTex(r"\Delta l", font_size=32).next_to(arrow_delta_l, LEFT, buff=0.15)

        self.add(
            frame_bounds,
            ceiling, hatch_lines,
            spring_left_1, spring_left_2, label_d1_left, label_d2_left,
            spring_right_1, spring_right_2,
            mass_box, label_m,
            vec_ff, label_ff,
            vec_fg, label_fg,
            dashed_ref_unloaded, dashed_ref_loaded,
            arrow_delta_l, label_delta_l
        )