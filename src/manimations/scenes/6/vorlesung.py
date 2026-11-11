from manim import *

class NormalkraftSkizze(Scene):
    def construct(self):
        ground_y = -1.5
        ground = Line(start=LEFT * 3.5, end=RIGHT * 3.5, color=WHITE, stroke_width=3).move_to(DOWN * 1.5)

        ground_hatches = VGroup()
        for x in np.linspace(-3.3, 3.3, 18):
            line = Line(
                start=np.array([x, ground_y, 0]),
                end=np.array([x - 0.25, ground_y - 0.3, 0]),
                color=GRAY,
                stroke_width=1.5
            )
            ground_hatches.add(line)

        box_width = 2.0
        box_height = 1.2
        box_center = np.array([0, ground_y + (box_height / 2.0), 0])

        box = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.4).move_to(box_center)
        box_label = MathTex("m").move_to(box_center)
        block = VGroup(box, box_label)

        vector_FN = Arrow(
            start=box_center,
            end=box_center + UP * 1.8,
            buff=0,
            color=GREEN
        )
        label_FN = MathTex("\\vec{F}_N").next_to(vector_FN, UP, buff=0.1)

        vector_FG = Arrow(
            start=box_center + LEFT * 0.35,
            end=box_center + LEFT * 0.35 + DOWN * 1.6,
            buff=0,
            color=YELLOW
        )
        label_FG = MathTex("\\vec{F}_G").next_to(vector_FG, DOWN + LEFT, buff=0.05)

        vector_F = Arrow(
            start=box_center + RIGHT * 0.35,
            end=box_center + RIGHT * 0.35 + DOWN * 1.6,
            buff=0,
            color=RED
        )
        label_F = MathTex("\\vec{F}").next_to(vector_F, DOWN + RIGHT, buff=0.05)

        self.add(
            ground, ground_hatches, block,
            vector_FN, label_FN,
            vector_FG, label_FG,
            vector_F, label_F
        )