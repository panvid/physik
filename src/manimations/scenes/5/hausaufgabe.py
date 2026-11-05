from manim import *

class ParallelschaltungFedernSkizze(Scene):
    def construct(self):
        ceiling_y = 2.5
        ceiling = Line(start=LEFT * 3.0, end=RIGHT * 3.0, color=WHITE, stroke_width=3).move_to(UP * ceiling_y)

        ceiling_hatches = VGroup()
        for x in np.linspace(-2.8, 2.8, 15):
            line = Line(
                start=np.array([x, ceiling_y, 0]),
                end=np.array([x + 0.2, ceiling_y + 0.25, 0]),
                color=GRAY,
                stroke_width=1.5
            )
            ceiling_hatches.add(line)

        left_x = -1.2
        right_x = 1.2
        spring_top_y = ceiling_y
        spring_bottom_y = -0.5

        def create_2d_spring(x_pos, y_top, y_bottom, turns=8, radius=0.25):
            height = y_top - y_bottom
            return ParametricFunction(
                lambda t: np.array([
                    x_pos + radius * np.sin(turns * 2 * PI * t),
                    y_top - t * height,
                    0
                ]),
                t_range=[0, 1],
                color=LIGHT_GRAY,
                stroke_width=2.5
            )

        spring_left = create_2d_spring(left_x, spring_top_y, spring_bottom_y)
        spring_right = create_2d_spring(right_x, spring_top_y, spring_bottom_y)

        bar = Line(
            start=np.array([left_x - 0.2, spring_bottom_y, 0]),
            end=np.array([right_x + 0.2, spring_bottom_y, 0]),
            color=GRAY,
            stroke_width=4
        )

        box_width = 1.0
        box_height = 0.8
        box_center = np.array([0, spring_bottom_y - (box_height / 2.0) - 0.1, 0])

        connecting_rope = Line(
            start=np.array([0, spring_bottom_y, 0]),
            end=box_center + UP * (box_height / 2.0),
            color=WHITE,
            stroke_width=2
        )

        mass_box = Rectangle(width=box_width, height=box_height, color=RED, fill_opacity=0.4).move_to(box_center)
        mass_label = MathTex("m").move_to(box_center)
        mass = VGroup(mass_box, mass_label)

        vector_F1 = Arrow(
            start=np.array([left_x, spring_bottom_y, 0]),
            end=np.array([left_x, spring_bottom_y + 1.2, 0]),
            buff=0,
            color=BLUE
        )
        label_F1 = MathTex("\\vec{F}_1").next_to(vector_F1, LEFT, buff=0.1)

        vector_F2 = Arrow(
            start=np.array([right_x, spring_bottom_y, 0]),
            end=np.array([right_x, spring_bottom_y + 1.2, 0]),
            buff=0,
            color=BLUE
        )
        label_F2 = MathTex("\\vec{F}_2").next_to(vector_F2, RIGHT, buff=0.1)

        vector_FG_up = Arrow(
            start=box_center,
            end=box_center + UP * 1.5,
            buff=0,
            color=GREEN
        )
        label_FG_up = MathTex("\\vec{F}_G").next_to(vector_FG_up, LEFT, buff=0.1)

        vector_FG_down = Arrow(
            start=box_center,
            end=box_center + DOWN * 1.5,
            buff=0,
            color=YELLOW
        )
        label_FG_down = MathTex("\\vec{F}'_G").next_to(vector_FG_down, RIGHT, buff=0.1)

        self.add(
            ceiling, ceiling_hatches,
            spring_left, spring_right, bar, connecting_rope, mass,
            vector_F1, label_F1,
            vector_F2, label_F2,
            vector_FG_up, label_FG_up,
            vector_FG_down, label_FG_down
        )

class CurlingsteinKraefteSkizzeMitAlphaInnen(Scene):
    def construct(self):
        point_origin = RIGHT * 2.0 + UP * 1.5

        length_H = 3.0
        length_G = 4.0

        point_left = point_origin + LEFT * length_H
        point_down = point_origin + DOWN * length_G
        point_diag = point_origin + LEFT * length_H + DOWN * length_G

        vector_FH = Arrow(start=point_origin, end=point_left, buff=0, color=YELLOW)
        label_FH = MathTex("\\vec{F}_H").next_to(vector_FH, UP, buff=0.1)

        vector_FG = Arrow(start=point_origin, end=point_down, buff=0, color=BLUE)
        label_FG = MathTex("\\vec{F}_G").next_to(vector_FG, RIGHT, buff=0.1)

        vector_F = Arrow(start=point_origin, end=point_diag, buff=0, color=GREEN)
        label_F = MathTex("\\vec{F}").next_to(vector_F, DOWN + LEFT, buff=0.05)

        dash_bottom = DashedLine(start=point_down, end=point_diag, color=YELLOW, dash_length=0.1)
        label_bottom_FH = MathTex("F_H", color=YELLOW).next_to(dash_bottom, DOWN, buff=0.1)

        dash_left = DashedLine(start=point_left, end=point_diag, color=BLUE, dash_length=0.1)

        center_dot = Dot(point=point_origin, radius=0.12, color=WHITE)

        line_FG = Line(start=point_origin, end=point_down)
        line_F = Line(start=point_origin, end=point_diag)

        angle_alpha = Angle(
            line_F,
            line_FG,
            radius=1.2,
            other_angle=False,
            color=WHITE
        )

        label_alpha = MathTex("\\alpha").move_to(
            Angle(
                line_F,
                line_FG,
                radius=1.6,
                other_angle=False
            ).point_from_proportion(0.5)
        )

        right_angle = RightAngle(
            line1=Line(start=point_down, end=point_origin),
            line2=Line(start=point_down, end=point_diag),
            length=0.3,
            color=WHITE
        )

        self.add(
            vector_FH, label_FH,
            vector_FG, label_FG,
            vector_F, label_F,
            dash_bottom, label_bottom_FH,
            dash_left,
            center_dot,
            angle_alpha, label_alpha,
            right_angle
        )