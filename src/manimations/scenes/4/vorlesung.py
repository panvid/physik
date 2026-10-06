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