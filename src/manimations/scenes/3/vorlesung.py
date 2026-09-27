from manim import *

class FallgesetzExperimentSkizze(Scene):
    def construct(self):
        stab_start = LEFT * 2.5 + DOWN * 2.5
        stab_end = LEFT * 2.5 + UP * 2.5

        stab = Line(start=stab_start, end=stab_end, color=GRAY, stroke_width=6)
        stab_fuss = Line(start=stab_start + LEFT * 0.5, end=stab_start + RIGHT * 0.5, color=GRAY, stroke_width=6)
        stativ = VGroup(stab, stab_fuss)

        skala_striche = VGroup()
        for i in range(11):
            y_pos = -2.5 + i * 0.5
            strich = Line(
                start=LEFT * 2.6,
                end=LEFT * 2.4,
                color=WHITE if i % 2 == 0 else GRAY,
                stroke_width=2 if i % 2 == 0 else 1
            ).shift(UP * y_pos)
            skala_striche.add(strich)

        hoehe_pfeil = DoubleArrow(
            start=LEFT * 3.2 + DOWN * 2.5,
            end=LEFT * 3.2 + UP * 2.0,
            buff=0,
            color=BLUE,
            stroke_width=3
        )
        hoehe_label = MathTex("y", color=BLUE, font_size=32).next_to(hoehe_pfeil, LEFT, buff=0.15)
        hoehe_gruppe = VGroup(hoehe_pfeil, hoehe_label)

        ball_start_pos = LEFT * 1.2 + UP * 2.0
        ball_end_pos = LEFT * 1.2 + DOWN * 2.5

        ball = Circle(radius=0.25, fill_opacity=1, color=RED).move_to(ball_start_pos)

        fall_linie = DashedLine(
            start=ball_start_pos,
            end=ball_end_pos,
            color=RED_B,
            stroke_width=2
        )

        v_arrow = Arrow(
            start=ball.get_bottom(),
            end=ball.get_bottom() + DOWN * 0.8,
            color=RED,
            buff=0.05,
            stroke_width=3
        )
        g_label = MathTex("g", color=RED, font_size=28).next_to(v_arrow, RIGHT, buff=0.1)

        klammer_t = BraceBetweenPoints(
            LEFT * 0.8 + UP * 2.0,
            LEFT * 0.8 + DOWN * 2.5,
            direction=RIGHT,
            color=YELLOW
        )
        zeit_label = MathTex("t", color=YELLOW, font_size=32).next_to(klammer_t, RIGHT, buff=0.2)
        zeit_gruppe = VGroup(klammer_t, zeit_label)

        self.add(
            stativ,
            skala_striche,
            hoehe_gruppe,
            fall_linie,
            ball,
            v_arrow,
            g_label,
            zeit_gruppe
        )

class WegZeitStroboskopSkizze(Scene):
    def construct(self):
        y_axis = Arrow(
            start=LEFT * 2.0 + DOWN * 3.2,
            end=LEFT * 2.0 + UP * 2.8,
            buff=0,
            color=WHITE
        )
        y_label = MathTex("y").next_to(y_axis.get_end(), UP, buff=0.15)

        origin_mark = Line(start=LEFT * 2.2 + UP * 2.0, end=LEFT * 1.8 + UP * 2.0, color=GRAY, stroke_width=2)
        origin_label = MathTex("y = 0", font_size=24).next_to(origin_mark, LEFT, buff=0.15)

        times = [0, 1, 2, 3, 4]
        positions = [0, 0.2, 0.8, 1.8, 3.2]

        dots_group = VGroup()
        for t, pos in zip(times, positions):
            pt = LEFT * 2.0 + (UP * 2.0 + DOWN * pos)
            dot = Dot(pt, radius=0.08, color=RED)
            t_lbl = MathTex(f"t_{t}", font_size=20, color=RED).next_to(dot, RIGHT, buff=0.2)
            dots_group.add(dot, t_lbl)

        self.add(y_axis, y_label, origin_mark, origin_label, dots_group)


class YTDiagrammVierterQuadrant(Scene):
    def construct(self):
        origin = LEFT * 3.0 + UP * 1.5

        y_axis = Arrow(start=origin + UP * 1.0, end=origin + DOWN * 4.5, buff=0, color=WHITE)
        y_label = MathTex("y").next_to(y_axis.get_end(), DOWN, buff=0.15)

        x_axis = Arrow(start=origin + LEFT * 0.5, end=origin + RIGHT * 6.0, buff=0, color=WHITE)
        x_label = MathTex("t").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        parabel = ParametricFunction(
            lambda t: origin + RIGHT * t + DOWN * (0.2 * t**2),
            t_range=[0, 4.5],
            stroke_width=4,
            color=BLUE
        )

        self.add(axes_group, parabel)

class VTDiagrammVierterQuadrant(Scene):
    def construct(self):
        origin = LEFT * 3.0 + UP * 1.5

        y_axis = Arrow(start=origin + DOWN * 4.5, end=origin + UP * 1.0, buff=0, color=WHITE)
        y_label = MathTex("v").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin + LEFT * 0.5, end=origin + RIGHT * 6.0, buff=0, color=WHITE)
        x_label = MathTex("t").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        v0_label = MathTex("v = 0", font_size=24).next_to(origin, UL, buff=0.15)

        gerade = Line(
            start=origin,
            end=origin + RIGHT * 5.0 + DOWN * 3.75,
            stroke_width=4,
            color=GREEN
        )

        self.add(axes_group, v0_label, gerade)

class AufprallgeschwindigkeitAufbau(Scene):
    def construct(self):
        ebene = Line(start=LEFT * 3.5, end=RIGHT * 3.5, color=GRAY, stroke_width=4).shift(DOWN * 2.0)
        ebene_schraffur = VGroup(*[
            Line(
                start=ebene.point_from_proportion(i / 14) + DOWN * 0.2 + LEFT * 0.1,
                end=ebene.point_from_proportion(i / 14),
                color=GRAY,
                stroke_width=2
            )
            for i in range(15)
        ])
        boden_gruppe = VGroup(ebene, ebene_schraffur)

        y_label_bottom = MathTex("y = -2\\,\\text{m}", font_size=24, color=WHITE).next_to(ebene, RIGHT, buff=0.3)

        ball_start_pos = LEFT * 0.8 + UP * 2.0
        ball_end_pos = LEFT * 0.8 + DOWN * 1.75

        fall_linie = DashedLine(
            start=ball_start_pos,
            end=ball_end_pos,
            color=WHITE,
            stroke_width=2
        )

        ball = Circle(radius=0.25, fill_opacity=1, color=RED).move_to(ball_start_pos)
        v0_label = MathTex("v = 0", font_size=26, color=RED).next_to(ball, UP, buff=0.2)

        hoehe_pfeil = DoubleArrow(
            start=RIGHT * 0.8 + UP * 2.0,
            end=RIGHT * 0.8 + DOWN * 2.0,
            buff=0,
            color=YELLOW,
            stroke_width=3
        )
        hoehe_label = MathTex("h = 2\\,\\text{m}", font_size=28, color=YELLOW).next_to(hoehe_pfeil, RIGHT, buff=0.2)

        self.add(
            boden_gruppe,
            y_label_bottom,
            fall_linie,
            ball,
            v0_label,
            hoehe_pfeil,
            hoehe_label
        )

class SenkrechterWurfSkizze(Scene):
    def construct(self):
        ebene = Line(start=LEFT * 3.5, end=RIGHT * 3.5, color=GRAY, stroke_width=4).shift(DOWN * 2.5)
        ebene_schraffur = VGroup(*[
            Line(
                start=ebene.point_from_proportion(i / 14) + DOWN * 0.2 + LEFT * 0.1,
                end=ebene.point_from_proportion(i / 14),
                color=GRAY,
                stroke_width=2
            )
            for i in range(15)
        ])
        boden_gruppe = VGroup(ebene, ebene_schraffur)

        y_null_label = MathTex("y = 0", font_size=24, color=WHITE).next_to(ebene, LEFT, buff=0.3)

        y_axis = Arrow(start=LEFT * 2.5 + DOWN * 2.5, end=LEFT * 2.5 + UP * 3.0, buff=0, color=WHITE)
        y_label = MathTex("y", font_size=28).next_to(y_axis.get_end(), UP, buff=0.15)
        axis_group = VGroup(y_axis, y_label)

        up_positions = [-2.2, -1.5, -0.5, 0.8, 1.8, 2.2]
        up_dots = VGroup()
        for pos in up_positions:
            dot = Dot(LEFT * 1.0 + UP * pos, radius=0.06, color=BLUE)
            up_dots.add(dot)

        v0_arrow = Arrow(
            start=LEFT * 1.0 + DOWN * 2.2,
            end=LEFT * 1.0 + DOWN * 1.2,
            color=BLUE,
            buff=0,
            stroke_width=3
        )
        v0_label = MathTex("v_0", font_size=26, color=BLUE).next_to(v0_arrow, LEFT, buff=0.15)

        down_positions = [2.2, 1.8, 0.8, -0.5, -1.5, -2.2]
        down_dots = VGroup()
        for pos in down_positions:
            dot = Dot(RIGHT * 0.2 + UP * pos, radius=0.06, color=RED)
            down_dots.add(dot)

        peak_dot = Dot(LEFT * 0.4 + UP * 2.3, radius=0.08, color=YELLOW)

        ymax_line = DashedLine(
            start=LEFT * 0.4 + UP * 2.3,
            end=RIGHT * 1.8 + UP * 2.3,
            color=GRAY,
            stroke_width=2
        )
        ymax_arrow = DoubleArrow(
            start=RIGHT * 1.8 + DOWN * 2.5,
            end=RIGHT * 1.8 + UP * 2.3,
            buff=0,
            color=YELLOW,
            stroke_width=3
        )
        ymax_label = MathTex("y_{\\text{max}}", font_size=28, color=YELLOW).next_to(ymax_arrow, RIGHT, buff=0.15)
        ymax_group = VGroup(ymax_line, ymax_arrow, ymax_label)

        self.add(
            boden_gruppe,
            y_null_label,
            axis_group,
            up_dots,
            v0_arrow,
            v0_label,
            down_dots,
            peak_dot,
            ymax_group
        )

class SenkrechterWurfYTDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 2.0

        y_axis = Arrow(start=origin + DOWN * 0.5, end=origin + UP * 5.0, buff=0, color=WHITE)
        y_label = MathTex("y", font_size=28).next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin + LEFT * 0.5, end=origin + RIGHT * 7.5, buff=0, color=WHITE)
        x_label = MathTex("t", font_size=28).next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        parabel = ParametricFunction(
            lambda t: origin + RIGHT * (t * 1.1) + UP * (3.0 * t - 0.6 * t**2),
            t_range=[0, 5.0],
            stroke_width=4,
            color=BLUE
        )

        p_peak = origin + RIGHT * (2.5 * 1.1) + UP * 3.75
        dot_peak = Dot(p_peak, radius=0.08, color=YELLOW)
        v0_peak_label = MathTex("v = 0", font_size=24, color=YELLOW).next_to(p_peak, UP, buff=0.15)

        p_ts_x = np.array([p_peak[0], origin[1], 0])
        line_ts = DashedLine(p_peak, p_ts_x, color=GRAY, stroke_width=2)
        label_ts = MathTex("t_s", font_size=24).next_to(p_ts_x, DOWN, buff=0.15)

        p_ymax_y = np.array([origin[0], p_peak[1], 0])
        line_ymax = DashedLine(p_peak, p_ymax_y, color=GRAY, stroke_width=2)
        label_ymax = MathTex("y_{\\text{max}}", font_size=24).next_to(p_ymax_y, LEFT, buff=0.15)

        p_tw = origin + RIGHT * (5.0 * 1.1)
        dot_tw = Dot(p_tw, radius=0.08, color=RED)
        label_tw = MathTex("t_w", font_size=24).next_to(p_tw, DOWN, buff=0.15)

        self.add(
            axes_group,
            parabel,
            dot_peak,
            v0_peak_label,
            line_ts,
            label_ts,
            line_ymax,
            label_ymax,
            dot_tw,
            label_tw
        )