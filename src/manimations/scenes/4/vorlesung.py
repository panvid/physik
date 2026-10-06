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