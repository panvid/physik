from manim import *

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