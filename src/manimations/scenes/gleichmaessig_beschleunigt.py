from manim import *

class XTDiagrammBeschleunigt(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="t", y_label="x")

        graph = ax.plot(lambda t: 0.25 * t ** 2, x_range=[0, 4.4], color=BLUE)

        self.add(ax, labels, graph)

class VTDiagrammBeschleunigt(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="t", y_label="v")

        graph = ax.plot(lambda t: t, x_range=[0, 4.5], color=GREEN)

        self.add(ax, labels, graph)

class ATDiagrammBeschleunigt(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="t", y_label="a")

        graph = ax.plot(lambda t: 2.5, x_range=[0, 4.5], color=RED)

        self.add(ax, labels, graph)