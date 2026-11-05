from manim import *

class SprinterStartblockSkizzeAndersrum(Scene):
    def construct(self):
        ground = Line(start=LEFT * 3.5, end=RIGHT * 3.5, color=WHITE, stroke_width=3).move_to(DOWN * 1.5)

        block_angle = 22 * DEGREES
        block_length = 2.5

        block_origin = LEFT * 1.5 + DOWN * 1.5 + UP * (block_length * np.sin(block_angle))

        block_end = block_origin + np.array(
            [block_length * np.cos(block_angle), -block_length * np.sin(block_angle), 0])

        block_line = Line(
            start=block_origin,
            end=block_end,
            color=GRAY,
            stroke_width=4
        )

        wedge = Polygon(
            block_origin,
            block_end,
            np.array([block_origin[0], -1.5, 0]),
            color=GRAY,
            fill_opacity=0.2
        )

        angle_arc = Arc(
            radius=0.8,
            start_angle=-block_angle,
            angle=block_angle,
            arc_center=block_end,
            color=YELLOW
        )
        label_alpha = MathTex("\\alpha").move_to(block_end + np.array([-1.1, 0.22, 0]))

        box_width = 1.0
        box_height = 0.6
        box_center_on_block = block_origin + np.array([1.3 * np.cos(block_angle), -1.3 * np.sin(block_angle), 0])

        box = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.4)
        box.rotate(-block_angle)
        box.move_to(box_center_on_block + np.array(
            [(box_height / 2) * np.sin(block_angle), (box_height / 2) * np.cos(block_angle), 0]))

        center_pt = box.get_center()

        perp_vec = np.array([np.sin(block_angle), np.cos(block_angle), 0])

        vector_F = Arrow(
            start=center_pt,
            end=center_pt + perp_vec * 1.8,
            buff=0,
            color=GREEN
        )
        label_F = MathTex("\\vec{F}").next_to(vector_F, UP + RIGHT, buff=0.05)

        vector_F_prime = Arrow(
            start=center_pt,
            end=center_pt - perp_vec * 1.8,
            buff=0,
            color=RED
        )
        label_F_prime = MathTex("\\vec{F}'").next_to(vector_F_prime, DOWN + LEFT, buff=0.05)

        vector_FH = Arrow(
            start=center_pt,
            end=center_pt + RIGHT * 2.2,
            buff=0,
            color=YELLOW
        )
        label_FH = MathTex("\\vec{F}_H").next_to(vector_FH, RIGHT, buff=0.1)

        self.add(
            ground, wedge, block_line, angle_arc, label_alpha,
            box,
            vector_F, label_F,
            vector_F_prime, label_F_prime,
            vector_FH, label_FH
        )

class SprinterKraefteparallelogrammSkizze(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 1],
            x_length=5.0,
            y_length=3.5,
            axis_config={"include_numbers": False, "include_tip": True}
        ).move_to(DOWN * 0.5 + LEFT * 0.5)

        origin = axes.c2p(0, 0)
        pt_H = axes.c2p(3.2, 0)
        pt_V = axes.c2p(0, 1.8)
        pt_diag = axes.c2p(3.2, 1.8)

        vector_FH = Arrow(start=origin, end=pt_H, buff=0, color=YELLOW)
        label_FH = MathTex("\\vec{F}_H").next_to(vector_FH, DOWN, buff=0.15)

        vector_FV = Arrow(start=origin, end=pt_V, buff=0, color=BLUE)
        label_FV = MathTex("\\vec{F}_V").next_to(vector_FV, LEFT, buff=0.15)

        vector_F = Arrow(start=origin, end=pt_diag, buff=0, color=GREEN)
        label_F = MathTex("\\vec{F}").next_to(vector_F, UP + LEFT, buff=0.05)

        dash_top = DashedLine(start=pt_V, end=pt_diag, color=YELLOW, dash_length=0.1)
        label_top_FH = MathTex("F_H", color=YELLOW).next_to(dash_top, UP, buff=0.1)

        dash_right = DashedLine(start=pt_H, end=pt_diag, color=BLUE, dash_length=0.1)
        label_right_FV = MathTex("F_V", color=BLUE).next_to(dash_right, RIGHT, buff=0.1)

        angle_alpha = Arc(
            radius=0.9,
            start_angle=0,
            angle=np.arctan2(1.8, 3.2),
            arc_center=origin,
            color=WHITE
        )
        label_alpha = MathTex("\\alpha").move_to(origin + np.array([1.2, 0.3, 0]))

        right_angle = RightAngle(
            line1=Line(start=pt_H, end=origin),
            line2=Line(start=pt_H, end=pt_diag),
            length=0.3,
            color=WHITE
        )

        self.add(
            axes,
            vector_FH, label_FH,
            vector_FV, label_FV,
            vector_F, label_F,
            dash_top, label_top_FH,
            dash_right, label_right_FV,
            angle_alpha, label_alpha,
            right_angle
        )