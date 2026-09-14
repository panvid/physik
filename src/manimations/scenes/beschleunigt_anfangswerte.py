from manim import *

class XTAnfangswerte(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 7, 1],
            x_length=6,
            y_length=4.5,
            axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="t", y_label="x")

        graph = ax.plot(lambda t: 0.2 * t**2 + 0.5 * t + 1.5, x_range=[0, 4.2], color=BLUE)

        x0_dot = Dot(ax.c2p(0, 1.5), color=WHITE, radius=0.06)
        x0_label = MathTex("x_0").next_to(x0_dot, LEFT, buff=0.1)

        self.add(ax, labels, graph, x0_dot, x0_label)

class VTAnfangswerte(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=4.5,
            axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="t", y_label="v")

        graph = ax.plot(lambda t: 0.8 * t + 2.0, x_range=[0, 4.5], color=GREEN)

        v0_dot = Dot(ax.c2p(0, 2.0), color=WHITE, radius=0.06)
        v0_label = MathTex("v_0").next_to(v0_dot, LEFT, buff=0.1)

        self.add(ax, labels, graph, v0_dot, v0_label)