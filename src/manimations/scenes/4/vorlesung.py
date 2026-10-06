from manim import *
import math

class WurfOrtsGeschwindigkeitBeschleunigung(Scene):
    def construct(self):
        ground_left = LEFT * 5.0 + DOWN * 2.0
        ground_right = RIGHT * 5.0 + DOWN * 2.0

        ground = Line(start=ground_left, end=ground_right, color=GRAY_A, stroke_width=4)
        ground_hatch = DashedLine(
            start=ground_left + DOWN * 0.1,
            end=ground_right + DOWN * 0.1,
            color=GRAY_C,
            stroke_width=2
        )

        start_point = LEFT * 3.5 + UP * 2.0
        h_val = 4.0
        xw_val = 6.0

        impact_point = start_point + RIGHT * xw_val + DOWN * h_val

        curve_points = [
            start_point + RIGHT * (xw_val * (t / 60.0)) + DOWN * (h_val * ((t / 60.0) ** 2))
            for t in range(61)
        ]
        parabola_smooth = VMobject(color=WHITE, stroke_width=3)
        parabola_smooth.set_points_smoothly(curve_points)
        parabola = DashedVMobject(parabola_smooth, dashed_ratio=0.5)

        start_dot = Dot(start_point, radius=0.1, color=RED_C)
        impact_dot = Dot(impact_point, radius=0.1, color=RED_C)

        v0_len = 2.2
        arrow_v0 = Arrow(
            start=start_point,
            end=start_point + RIGHT * v0_len,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.2
        )
        label_v0 = MathTex(r"\vec{v}_0", color=BLUE_C).next_to(arrow_v0.get_center(), UP, buff=0.15)

        arrow_h = DoubleArrow(
            start=start_point + LEFT * 0.8,
            end=start_point + LEFT * 0.8 + DOWN * h_val,
            buff=0,
            color=YELLOW_C,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.1
        )
        label_h = MathTex("h", color=YELLOW_C).next_to(arrow_h.get_center(), LEFT, buff=0.15)

        dashed_h_top = DashedLine(start=start_point, end=start_point + LEFT * 0.8, color=GRAY_B, stroke_width=2)
        dashed_h_bottom = DashedLine(start=start_point + DOWN * h_val, end=start_point + LEFT * 0.8 + DOWN * h_val, color=GRAY_B, stroke_width=2)

        self.add(
            ground, ground_hatch,
            parabola,
            start_dot, impact_dot,
            arrow_v0, label_v0,
            arrow_h, label_h,
            dashed_h_top, dashed_h_bottom
        )

class SchraegerWurfDiagramm(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-0.5, 7.5, 1],
            y_range=[-0.5, 4.5, 1],
            x_length=9.0,
            y_length=5.5,
            axis_config={"include_numbers": False, "color": GRAY_C},
            tips=True
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        origin = axes.c2p(0, 0)
        xw_val = 6.0
        ymax_val = 3.2

        parabola_smooth = axes.plot(
            lambda x: 4 * ymax_val * (x / xw_val) * (1 - x / xw_val),
            x_range=[0, xw_val],
            color=WHITE
        )
        parabola = DashedVMobject(parabola_smooth, dashed_ratio=0.5)

        v0_len = 2.4
        alpha_rad = math.atan(4 * ymax_val / xw_val)
        v0_end = axes.c2p(v0_len * math.cos(alpha_rad), v0_len * math.sin(alpha_rad))

        arrow_v0 = Arrow(
            start=origin,
            end=v0_end,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.18
        )
        label_v0 = MathTex(r"\vec{v}_0", color=BLUE_C).next_to(arrow_v0.get_end(), UP + RIGHT, buff=0.1)

        arc_alpha = Arc(
            radius=1.0,
            start_angle=0,
            angle=alpha_rad,
            arc_center=origin,
            color=YELLOW_C,
            stroke_width=3
        )
        label_alpha = MathTex(r"\alpha", color=YELLOW_C).move_to(
            axes.c2p(1.3 * math.cos(alpha_rad / 2), 1.3 * math.sin(alpha_rad / 2))
        )

        apex_point = axes.c2p(xw_val / 2, ymax_val)
        dot_apex = Dot(apex_point, radius=0.08, color=RED_C)

        arrow_ymax = DoubleArrow(
            start=axes.c2p(xw_val / 2, 0),
            end=apex_point,
            buff=0,
            color=YELLOW_C,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.1
        )
        label_ymax = MathTex(r"y_{\text{max}}", color=YELLOW_C).next_to(arrow_ymax.get_center(), RIGHT, buff=0.15)

        dashed_apex_x = DashedLine(start=apex_point, end=axes.c2p(xw_val / 2, 0), color=GRAY_B, stroke_width=2)

        impact_point = axes.c2p(xw_val, 0)
        dot_impact = Dot(impact_point, radius=0.08, color=RED_C)
        label_xw = MathTex(r"x_w", color=WHITE).next_to(impact_point, DOWN, buff=0.2)

        self.add(
            axes, labels,
            parabola,
            arrow_v0, label_v0,
            arc_alpha, label_alpha,
            dashed_apex_x, dot_apex, arrow_ymax, label_ymax,
            dot_impact, label_xw
        )

class GeschwindigkeitsZerlegung(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 5, 1],
            x_length=8.0,
            y_length=6.0,
            axis_config={"include_numbers": False, "color": GRAY_C},
            tips=True
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        origin = axes.c2p(0, 0)
        vx_val = 4.5
        vy_val = 3.2

        point_v = axes.c2p(vx_val, vy_val)
        point_vx = axes.c2p(vx_val, 0)
        point_vy = axes.c2p(0, vy_val)

        arrow_v = Arrow(
            start=origin,
            end=point_v,
            buff=0,
            color=RED_C,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        label_v = MathTex(r"\vec{v}", color=RED_C).next_to(arrow_v.get_center(), UP + LEFT, buff=0.15)

        arrow_vx = Arrow(
            start=origin,
            end=point_vx,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )
        label_vx = MathTex(r"v_{x0}", color=BLUE_C).next_to(arrow_vx.get_center(), DOWN, buff=0.15)

        arrow_vy = Arrow(
            start=origin,
            end=point_vy,
            buff=0,
            color=GREEN_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )
        label_vy = MathTex(r"v_{y0}", color=GREEN_C).next_to(arrow_vy.get_center(), LEFT, buff=0.15)

        dashed_x = DashedLine(start=point_v, end=point_vx, color=GRAY_B, stroke_width=2)
        dashed_y = DashedLine(start=point_v, end=point_vy, color=GRAY_B, stroke_width=2)

        alpha_rad = math.atan(vy_val / vx_val)
        arc_alpha = Arc(
            radius=1.2,
            start_angle=0,
            angle=alpha_rad,
            arc_center=origin,
            color=YELLOW_C,
            stroke_width=3
        )
        label_alpha = MathTex(r"\alpha", color=YELLOW_C).move_to(
            axes.c2p(1.6 * math.cos(alpha_rad / 2), 1.6 * math.sin(alpha_rad / 2))
        )

        self.add(
            axes, labels,
            dashed_x, dashed_y,
            arrow_vx, label_vx,
            arrow_vy, label_vy,
            arrow_v, label_v,
            arc_alpha, label_alpha
        )

class WilhelmTellKomplettSichtbar(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 28, 5],
            y_range=[-3, 4.5, 1],
            x_length=11.5,
            y_length=5.8,
            axis_config={"include_numbers": False, "color": GRAY_C},
            tips=True
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        origin = axes.c2p(0, 0)
        x_target_val = 25.0
        y_target_val = -1.0
        v0_val = 30.0
        g_val = 9.81

        v0_len = 2.8
        term_val = (g_val * (x_target_val ** 2)) / (v0_val ** 2)
        alpha_rad = math.atan(
            (x_target_val - math.sqrt(x_target_val ** 2 - 2 * y_target_val * term_val - term_val ** 2)) / term_val
        )

        v0_end = axes.c2p(v0_len * math.cos(alpha_rad), v0_len * math.sin(alpha_rad))

        arrow_v0 = Arrow(
            start=origin,
            end=v0_end,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.18
        )
        label_v0 = MathTex(r"\vec{v}_0 = 30\text{ m/s}", color=BLUE_C).next_to(arrow_v0.get_end(), UP + RIGHT, buff=0.1)

        arc_alpha = Arc(
            radius=1.1,
            start_angle=0,
            angle=alpha_rad,
            arc_center=origin,
            color=YELLOW_C,
            stroke_width=3
        )
        label_alpha = MathTex(r"\alpha", color=YELLOW_C).move_to(
            axes.c2p(1.5 * math.cos(alpha_rad / 2), 1.5 * math.sin(alpha_rad / 2))
        )

        parabola_smooth = axes.plot(
            lambda x: math.tan(alpha_rad) * x - (g_val / (2 * (v0_val * math.cos(alpha_rad)) ** 2)) * (x ** 2),
            x_range=[0, x_target_val],
            color=WHITE
        )
        parabola = DashedVMobject(parabola_smooth, dashed_ratio=0.5)

        def make_stickman(color=WHITE):
            head = Circle(radius=0.2, color=color)
            body = Line(head.get_bottom(), head.get_bottom() + DOWN * 0.5, color=color)
            left_leg = Line(body.get_end(), body.get_end() + DOWN * 0.4 + LEFT * 0.2, color=color)
            right_leg = Line(body.get_end(), body.get_end() + DOWN * 0.4 + RIGHT * 0.2, color=color)
            left_arm = Line(body.get_center(), body.get_center() + UP * 0.1 + LEFT * 0.3, color=color)
            right_arm = Line(body.get_center(), body.get_center() + UP * 0.1 + RIGHT * 0.3, color=color)
            return VGroup(head, body, left_leg, right_leg, left_arm, right_arm)

        tell = make_stickman(color=GREEN_C)
        tell.scale(0.7).move_to(axes.c2p(-1.5, -0.6))
        label_armbrust = Text("Armbrust", font_size=18, color=GREEN_C).next_to(tell, DOWN + LEFT, buff=0.1)

        target_point = axes.c2p(x_target_val, y_target_val)
        target_person = make_stickman(color=RED_C)
        target_person.scale(0.7)
        target_person.move_to(target_point + DOWN * target_person.height / 2)

        head_center_target = target_point + DOWN * 0.14
        dot_target = Dot(head_center_target, radius=0.08, color=RED_C)
        label_target = MathTex(r"A = (25\text{m}; -1\text{m})", font_size=24, color=RED_C).next_to(
            head_center_target, UP + RIGHT, buff=0.15
        )

        dist_arrow = DoubleArrow(
            start=axes.c2p(0, -2.2),
            end=axes.c2p(x_target_val, -2.2),
            buff=0,
            color=YELLOW_C,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.08
        )
        label_dist = MathTex(r"25\text{ m}", color=YELLOW_C).next_to(dist_arrow.get_center(), UP, buff=0.1)

        dashed_x_proj = DashedLine(start=target_point, end=axes.c2p(x_target_val, -2.2), color=GRAY_B, stroke_width=2)
        dashed_origin_proj = DashedLine(start=origin, end=axes.c2p(0, -2.2), color=GRAY_B, stroke_width=2)

        self.add(
            axes, labels,
            parabola,
            arrow_v0, label_v0,
            arc_alpha, label_alpha,
            tell, label_armbrust,
            target_person, dot_target, label_target,
            dist_arrow, label_dist,
            dashed_x_proj, dashed_origin_proj
        )

class EinheitskreisVierQuadranten(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1.4, 1.4, 0.5],
            y_range=[-1.4, 1.4, 0.5],
            x_length=6.5,
            y_length=6.5,
            axis_config={"include_numbers": False, "color": GRAY_C},
            tips=True
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        origin = axes.c2p(0, 0)

        circle = Circle(
            radius=axes.c2p(1, 0)[0] - origin[0],
            color=GRAY_A,
            stroke_width=2
        ).move_to(origin)

        alpha_deg = 35
        alpha_rad = math.radians(alpha_deg)

        cos_val = math.cos(alpha_rad)
        sin_val = math.sin(alpha_rad)

        pt_cos = axes.c2p(cos_val, 0)
        pt_circle = axes.c2p(cos_val, sin_val)

        line_hypotenuse = Line(start=origin, end=pt_circle, color=WHITE, stroke_width=4)
        label_hypotenuse = MathTex("1", color=WHITE).next_to(line_hypotenuse.get_center(), UP + LEFT, buff=0.1)

        line_cos = Line(start=origin, end=pt_cos, color=BLUE_C, stroke_width=4)
        label_cos = MathTex(r"\cos(\alpha)", color=BLUE_C).next_to(line_cos.get_center(), DOWN, buff=0.15)

        line_sin = Line(start=pt_cos, end=pt_circle, color=GREEN_C, stroke_width=4)
        label_sin = MathTex(r"\sin(\alpha)", color=GREEN_C).next_to(line_sin.get_center(), RIGHT, buff=0.15)

        arc_alpha = Arc(
            radius=0.7,
            start_angle=0,
            angle=alpha_rad,
            arc_center=origin,
            color=YELLOW_C,
            stroke_width=3
        )
        label_alpha = MathTex(r"\alpha", color=YELLOW_C).move_to(
            axes.c2p(0.25 * math.cos(alpha_rad / 2), 0.25 * math.sin(alpha_rad / 2))
        )

        right_angle = RightAngle(
            line_cos,
            line_sin,
            length=0.25,
            color=GRAY_A,
            stroke_width=2
        )

        dot_origin = Dot(origin, radius=0.06, color=WHITE)
        dot_circle = Dot(pt_circle, radius=0.06, color=WHITE)

        self.add(
            axes, labels,
            circle,
            line_cos, label_cos,
            line_sin, label_sin,
            line_hypotenuse, label_hypotenuse,
            arc_alpha, label_alpha,
            right_angle,
            dot_origin, dot_circle
        )

class WilhelmTellZweiParabeln(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 29, 5],
            y_range=[-3, 4.5, 1],
            x_length=11.5,
            y_length=5.8,
            axis_config={"include_numbers": False, "color": GRAY_C},
            tips=True
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        origin = axes.c2p(0, 0)
        x_target_val = 25.0
        y_target_val = -1.0
        v0_val = 30.0
        g_val = 9.81

        term_val = (g_val * (x_target_val ** 2)) / (v0_val ** 2)

        alpha1_rad = math.atan(
            (x_target_val + math.sqrt(x_target_val ** 2 - 2 * y_target_val * term_val - term_val ** 2)) / term_val
        )
        alpha2_rad = math.atan(
            (x_target_val - math.sqrt(x_target_val ** 2 - 2 * y_target_val * term_val - term_val ** 2)) / term_val
        )

        parabola_flat_smooth = axes.plot(
            lambda x: math.tan(alpha2_rad) * x - (g_val / (2 * (v0_val * math.cos(alpha2_rad)) ** 2)) * (x ** 2),
            x_range=[0, x_target_val],
            color=BLUE_C
        )
        parabola_flat = DashedVMobject(parabola_flat_smooth, dashed_ratio=0.5)

        parabola_high_smooth = axes.plot(
            lambda x: math.tan(alpha1_rad) * x - (g_val / (2 * (v0_val * math.cos(alpha1_rad)) ** 2)) * (x ** 2),
            x_range=[0, x_target_val],
            color=RED_C
        )
        parabola_high = DashedVMobject(parabola_high_smooth, dashed_ratio=0.5)

        arc_alpha2 = Arc(
            radius=1.3,
            start_angle=0,
            angle=alpha2_rad,
            arc_center=origin,
            color=YELLOW_C,
            stroke_width=3
        )
        label_alpha2 = MathTex(r"\alpha_2", color=YELLOW_C).move_to(
            axes.c2p(1.7 * math.cos(alpha2_rad / 2), 1.7 * math.sin(alpha2_rad / 2))
        )

        def make_stickman(color=WHITE):
            head = Circle(radius=0.2, color=color)
            body = Line(head.get_bottom(), head.get_bottom() + DOWN * 0.5, color=color)
            left_leg = Line(body.get_end(), body.get_end() + DOWN * 0.4 + LEFT * 0.2, color=color)
            right_leg = Line(body.get_end(), body.get_end() + DOWN * 0.4 + RIGHT * 0.2, color=color)
            left_arm = Line(body.get_center(), body.get_center() + UP * 0.1 + LEFT * 0.3, color=color)
            right_arm = Line(body.get_center(), body.get_center() + UP * 0.1 + RIGHT * 0.3, color=color)
            return VGroup(head, body, left_leg, right_leg, left_arm, right_arm)

        tell = make_stickman(color=GREEN_C)
        tell.scale(0.7).move_to(axes.c2p(-1.5, -0.6))

        target_point = axes.c2p(x_target_val, y_target_val)
        target_person = make_stickman(color=RED_C)
        target_person.scale(0.7)
        target_person.move_to(target_point + DOWN * target_person.height / 2)

        head_center_target = target_point + DOWN * 0.14
        dot_target = Dot(head_center_target, radius=0.08, color=RED_C)

        self.add(
            axes, labels,
            parabola_high, parabola_flat,
            arc_alpha2, label_alpha2,
            tell, target_person, dot_target
        )

class AffenschussDritterQuadrant(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 25, 5],
            y_range=[-4, 10, 2],
            x_length=11.5,
            y_length=6.0,
            axis_config={"include_numbers": False, "color": GRAY_C},
            tips=True
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        x_gun = -3.0
        y_gun = -2.0
        pt_gun = axes.c2p(x_gun, y_gun)

        x_monkey = 20.0
        y_monkey_start = 8.0
        v0_val = 28.0
        g_val = 9.81

        dx = x_monkey - x_gun
        dy = y_monkey_start - y_gun
        alpha_rad = math.atan(dy / dx)

        v0_len = 2.8
        v0_end = axes.c2p(
            x_gun + v0_len * math.cos(alpha_rad),
            y_gun + v0_len * math.sin(alpha_rad)
        )

        arrow_v0 = Arrow(
            start=pt_gun,
            end=v0_end,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.18
        )
        label_v0 = MathTex(r"\vec{v}_0", color=BLUE_C).next_to(arrow_v0.get_end(), UP + LEFT, buff=0.1)

        arc_alpha = Arc(
            radius=1.0,
            start_angle=0,
            angle=alpha_rad,
            arc_center=pt_gun,
            color=YELLOW_C,
            stroke_width=3
        )
        label_alpha = MathTex(r"\alpha", color=YELLOW_C).move_to(
            axes.c2p(x_gun + 1.4 * math.cos(alpha_rad / 2), y_gun + 1.4 * math.sin(alpha_rad / 2))
        )

        line_of_sight = DashedLine(
            start=pt_gun,
            end=axes.c2p(x_monkey, y_monkey_start),
            color=GRAY_B,
            stroke_width=1.5
        )

        t_hit = dx / (v0_val * math.cos(alpha_rad))

        parabola_smooth = axes.plot(
            lambda x: y_gun + math.tan(alpha_rad) * (x - x_gun) - (g_val / (2 * (v0_val * math.cos(alpha_rad)) ** 2)) * ((x - x_gun) ** 2),
            x_range=[x_gun, x_monkey],
            color=WHITE
        )
        parabola = DashedVMobject(parabola_smooth, dashed_ratio=0.5)

        monkey_t_vals = [0.0, 0.3, 0.55, 0.78, 1.0]
        monkey_dots = []

        for t_ratio in monkey_t_vals:
            t_curr = t_ratio * t_hit
            y_curr = y_monkey_start - 0.5 * g_val * (t_curr ** 2)
            pt = axes.c2p(x_monkey, y_curr)
            dot = Dot(pt, radius=0.08, color=RED_C)
            monkey_dots.append(dot)

        label_monkey = MathTex(r"A\ \text{(Affe)}", color=RED_C, font_size=26).next_to(
            monkey_dots[0], UP + RIGHT, buff=0.15
        )

        arrow_h = DoubleArrow(
            start=axes.c2p(x_monkey + 1.8, 0),
            end=axes.c2p(x_monkey + 1.8, y_monkey_start),
            buff=0,
            color=YELLOW_C,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.08
        )
        label_h = MathTex("h", color=YELLOW_C).next_to(arrow_h.get_center(), RIGHT, buff=0.15)

        dashed_h_bottom = DashedLine(
            start=axes.c2p(x_monkey, 0),
            end=axes.c2p(x_monkey + 1.8, 0),
            color=GRAY_B,
            stroke_width=2
        )
        dashed_h_top = DashedLine(
            start=axes.c2p(x_monkey, y_monkey_start),
            end=axes.c2p(x_monkey + 1.8, y_monkey_start),
            color=GRAY_B,
            stroke_width=2
        )

        def make_gun():
            barrel = Rectangle(height=0.15, width=0.8, color=GREEN_C, fill_opacity=0.8)
            stock = Line(barrel.get_bottom() + LEFT * 0.2, barrel.get_bottom() + LEFT * 0.4 + DOWN * 0.3, color=GREEN_C, stroke_width=4)
            gun_grp = VGroup(barrel, stock)
            gun_grp.rotate(alpha_rad, about_point=gun_grp.get_left())
            gun_grp.move_to(pt_gun, aligned_edge=LEFT)
            return gun_grp

        gun = make_gun()

        dot_gun_start = Dot(pt_gun, radius=0.08, color=GREEN_C)

        self.add(
            axes, labels,
            line_of_sight,
            parabola,
            arrow_v0, label_v0,
            arc_alpha, label_alpha,
            gun, dot_gun_start,
            *monkey_dots, label_monkey,
            arrow_h, label_h,
            dashed_h_bottom, dashed_h_top
        )

class AffenschussSuperposition(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 7, 1],
            x_length=11.5,
            y_length=6.0,
            axis_config={"include_numbers": False, "color": GRAY_C},
            tips=True
        )

        x_max = 8.5
        y_target = 6.0
        g_factor = 4.5

        line_of_sight = DashedLine(
            start=axes.c2p(0, 0),
            end=axes.c2p(x_max, y_target),
            color=GRAY_B,
            stroke_width=2
        )

        parabola_smooth = axes.plot(
            lambda x: (y_target / x_max) * x - (g_factor / (x_max ** 2)) * (x ** 2),
            x_range=[0, x_max],
            color=WHITE
        )
        parabola = DashedVMobject(parabola_smooth, dashed_ratio=0.5)

        t_vals = [0.0, 0.25, 0.5, 0.75, 1.0]

        vertical_lines = []
        dots_linear = []
        dots_parabola = []

        for t in t_vals:
            x_val = x_max * t
            y_lin = y_target * t
            y_par = y_lin - g_factor * (t ** 2)

            pt_lin = axes.c2p(x_val, y_lin)
            pt_par = axes.c2p(x_val, y_par)

            if t > 0:
                vert_line = DashedLine(
                    start=pt_lin,
                    end=pt_par,
                    color=RED_C,
                    stroke_width=2,
                    dash_length=0.08
                )
                vertical_lines.append(vert_line)

            dot_lin = Dot(pt_lin, radius=0.07, color=BLUE_C)
            dot_par = Dot(pt_par, radius=0.07, color=YELLOW_C)

            dots_linear.append(dot_lin)
            dots_parabola.append(dot_par)

        monkey_fall_dots = []
        for t in t_vals:
            y_pos = y_target - g_factor * (t ** 2)
            pt = axes.c2p(x_max, y_pos)
            dot = Dot(pt, radius=0.08, color=RED_C)
            monkey_fall_dots.append(dot)

        label_linear = Text("Ungestörte Visierlinie", font_size=20, color=BLUE_C).next_to(
            dots_linear[-2], UP + LEFT, buff=0.1
        )
        label_parabola = Text("Tatsächliche Schussbahn", font_size=20, color=YELLOW_C).next_to(
            dots_parabola[2], DOWN + RIGHT, buff=0.1
        )
        label_monkey = Text("Affe (freier Fall)", font_size=20, color=RED_C).next_to(
            monkey_fall_dots[0], UP + LEFT, buff=0.15
        )

        self.add(
            axes,
            line_of_sight,
            parabola,
            *vertical_lines,
            *dots_linear,
            *dots_parabola,
            *monkey_fall_dots,
            label_linear,
            label_parabola,
            label_monkey
        )

class KraftpfeilDynamikExaktParallel(Scene):
    def construct(self):
        start_pt = LEFT * 2.5 + UP * 1.5
        length_val = 5.0
        angle_rad = math.radians(-35)

        end_pt = start_pt + RIGHT * (length_val * math.cos(angle_rad)) + UP * (length_val * math.sin(angle_rad))

        arrow_f = Arrow(
            start=start_pt,
            end=end_pt,
            buff=0,
            color=RED_C,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        label_f = MathTex(r"\vec{F}", color=RED_C, font_size=42).next_to(arrow_f.get_start(), UP + LEFT, buff=0.15)

        label_direction = Text("Richtung", font_size=24, color=WHITE).next_to(arrow_f.get_end(), DOWN + RIGHT, buff=0.15)

        ref_line = Line(start_pt, end_pt)
        brace_f = Brace(ref_line, direction=DOWN, buff=0.25, color=YELLOW_C)
        brace_f.rotate(angle_rad, about_point=ref_line.get_center())

        label_magnitude = Text("Betrag", font_size=24, color=YELLOW_C)
        label_magnitude.next_to(brace_f, DOWN, buff=0.15)
        label_magnitude.rotate(angle_rad, about_point=label_magnitude.get_center())

        dot_start = Dot(start_pt, radius=0.09, color=WHITE)

        self.add(
            arrow_f,
            label_f,
            label_direction,
            brace_f,
            label_magnitude,
            dot_start
        )