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