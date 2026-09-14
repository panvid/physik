from manim import *

class UeberholvorgangDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 2.5

        y_axis = Arrow(start=origin, end=origin + UP * 5.5, buff=0, color=WHITE)
        y_label = MathTex("x").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 7.5, buff=0, color=WHITE)
        x_label = MathTex("t").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        x_0F_pos = origin + UP * 2.0
        x_0F_dot = Dot(point=x_0F_pos, radius=0.06, color=WHITE)
        x_0F_label = MathTex("x_{0F}").next_to(x_0F_pos, LEFT, buff=0.15)

        schnittpunkt_pos = origin + RIGHT * 4.0 + UP * 4.5

        gerade_A = Line(
            start=origin,
            end=origin + RIGHT * 5.0 + UP * 5.625,
            stroke_width=4,
            color=BLUE
        )
        label_A = Text("A", font_size=24, color=BLUE).next_to(gerade_A.get_end(), RIGHT, buff=0.15)

        gerade_F = Line(
            start=x_0F_pos,
            end=origin + RIGHT * 6.0 + UP * 5.75,
            stroke_width=4,
            color=GREEN
        )
        label_F = Text("F", font_size=24, color=GREEN).next_to(gerade_F.get_end(), RIGHT, buff=0.15)

        schnittpunkt_dot = Dot(point=schnittpunkt_pos, radius=0.08, color=RED)

        t_schnitt_pos = np.array([schnittpunkt_pos[0], origin[1], 0])
        linie_t = DashedLine(start=schnittpunkt_pos, end=t_schnitt_pos, stroke_width=2, color=GRAY)
        label_t = Text("Zeitpunkt d. Überholens", font_size=18).next_to(t_schnitt_pos, DOWN, buff=0.2)

        x_schnitt_pos = np.array([origin[0], schnittpunkt_pos[1], 0])
        linie_x = DashedLine(start=schnittpunkt_pos, end=x_schnitt_pos, stroke_width=2, color=GRAY)
        label_x = Text("Ort d. Überholens", font_size=18).next_to(x_schnitt_pos, LEFT, buff=0.2)

        self.add(
            axes_group,
            x_0F_dot,
            x_0F_label,
            gerade_A,
            label_A,
            gerade_F,
            label_F,
            linie_t,
            linie_x,
            schnittpunkt_dot,
            label_t,
            label_x
        )