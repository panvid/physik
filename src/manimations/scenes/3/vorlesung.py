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

class SenkrechterWurfVTDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + UP * 0.5

        y_axis = Arrow(start=origin + DOWN * 3.5, end=origin + UP * 2.5, buff=0, color=WHITE)
        y_label = MathTex("v", font_size=28).next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin + LEFT * 0.5, end=origin + RIGHT * 7.5, buff=0, color=WHITE)
        x_label = MathTex("t", font_size=28).next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        v0_pos = origin + UP * 1.8
        v0_dot = Dot(v0_pos, radius=0.08, color=BLUE)
        v0_label = MathTex("v_0", font_size=26, color=BLUE).next_to(v0_pos, LEFT, buff=0.15)

        gerade = Line(
            start=v0_pos,
            end=origin + RIGHT * 5.0 + DOWN * 1.8,
            stroke_width=4,
            color=GREEN
        )

        p_ts_x = origin + RIGHT * 2.5
        dot_ts = Dot(p_ts_x, radius=0.08, color=YELLOW)
        label_ts = MathTex("t_s", font_size=24, color=YELLOW).next_to(p_ts_x, UP, buff=0.15)

        p_tw_x = origin + RIGHT * 5.0
        p_tw_end = p_tw_x + DOWN * 1.8
        dot_tw = Dot(p_tw_end, radius=0.08, color=RED)

        line_tw = DashedLine(p_tw_end, p_tw_x, color=GRAY, stroke_width=2)
        label_tw = MathTex("t_w", font_size=24, color=RED).next_to(p_tw_x, UP, buff=0.15)

        self.add(
            axes_group,
            gerade,
            v0_dot,
            v0_label,
            dot_ts,
            label_ts,
            dot_tw,
            line_tw,
            label_tw
        )

class BahnkurveVektorenDiagramm(Scene):
    def construct(self):
        origin = LEFT * 0.5 + DOWN * 0.8

        def proj(x, y, z):
            return origin + RIGHT * (x * 0.85 - z * 0.7) + UP * (y * 0.75 - z * 0.45)

        p_x = proj(6.0, 0, 0)
        p_y = proj(0, 4.5, 0)
        p_z = proj(0, 0, 4.2)

        x_axis = Arrow(start=origin, end=p_x, buff=0, color=WHITE)
        x_label = MathTex("x", font_size=28).next_to(p_x, DR, buff=0.1)

        y_axis = Arrow(start=origin, end=p_y, buff=0, color=WHITE)
        y_label = MathTex("y", font_size=28).next_to(p_y, UP, buff=0.1)

        z_axis = Arrow(start=origin, end=p_z, buff=0, color=WHITE, stroke_width=4)
        z_label = MathTex("z", font_size=28).next_to(p_z, DL, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, z_axis, x_label, y_label, z_label)

        def path_func(t):
            x = 0.75 * t
            y = 1.0 * np.sin(0.6 * t) + 0.3 * t + 0.6
            z = 0.4 * np.cos(0.8 * t) + 0.3 * t + 0.1
            return proj(x, y, z)

        bahnkurve = ParametricFunction(
            path_func,
            t_range=[0.2, 7.2],
            color=GRAY_B,
            stroke_width=4
        )

        t1 = 1.8
        t2 = 5.6

        p1 = path_func(t1)
        p2 = path_func(t2)

        r1_arrow = Arrow(start=origin, end=p1, buff=0, color=BLUE, stroke_width=3)
        r1_label = MathTex("\\vec{r}(t_1)", color=BLUE, font_size=26).next_to(p1, UL, buff=0.1)
        dot1 = Dot(p1, color=BLUE, radius=0.08)

        r2_arrow = Arrow(start=origin, end=p2, buff=0, color=RED, stroke_width=3)
        r2_label = MathTex("\\vec{r}(t_2)", color=RED, font_size=26).next_to(p2, UR, buff=0.1)
        dot2 = Dot(p2, color=RED, radius=0.08)

        self.add(
            axes_group,
            bahnkurve,
            r1_arrow, r1_label, dot1,
            r2_arrow, r2_label, dot2
        )

class VektorDarstellungParallel(Scene):
    def construct(self):
        start = LEFT * 2.5 + DOWN * 1.5
        end = RIGHT * 2.5 + UP * 1.5

        vector = Arrow(
            start=start,
            end=end,
            buff=0,
            color=BLUE_C,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )

        label_vector = MathTex(r"\vec{a}", color=WHITE).next_to(
            vector.get_center(), UP + LEFT, buff=0.2
        )

        direction_vec = end - start
        normal_vec = np.array([direction_vec[1], -direction_vec[0], 0])
        normal_vec = normal_vec / np.linalg.norm(normal_vec)

        brace = BraceBetweenPoints(start, end, direction=normal_vec, color=GRAY_A)
        brace_text = brace.get_tex(r"\hat{=}\text{ Betrag}")
        brace_text.scale(0.8).set_color(WHITE)

        tip_point = vector.get_end()
        info_pos = tip_point + RIGHT * 2.2 + UP * 0.8

        pointer_arrow = Arrow(
            start=info_pos + LEFT * 0.4 + DOWN * 0.2,
            end=tip_point + RIGHT * 0.1 + UP * 0.1,
            buff=0.05,
            color=YELLOW_C,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )

        direction_label = Text("Richtung", font_size=28, color=YELLOW_C).next_to(
            info_pos, UP, buff=0.1
        )

        self.add(vector, label_vector, brace, brace_text, pointer_arrow, direction_label)

class VektorKonstellationen(Scene):
    def construct(self):
        a_start = LEFT * 4 + UP * 2.2
        a_end = LEFT * 1.5 + UP * 2.8
        vector_a = Arrow(start=a_start, end=a_end, buff=0, color=BLUE_C, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        label_a = MathTex(r"\vec{a}", color=WHITE).next_to(vector_a.get_center(), UP, buff=0.15)

        shift_vec = RIGHT * 3.0 + DOWN * 0.6
        b_start = a_start + shift_vec
        b_end = a_end + shift_vec
        vector_b = Arrow(start=b_start, end=b_end, buff=0, color=BLUE_C, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        label_b = MathTex(r"\vec{b}", color=WHITE).next_to(vector_b.get_center(), DOWN, buff=0.15)

        v_start = LEFT * 4 + DOWN * 0.1
        v_end = LEFT * 1.5 + UP * 0.5
        vector_v = Arrow(start=v_start, end=v_end, buff=0, color=GREEN_C, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        label_v = MathTex(r"\vec{v}", color=WHITE).next_to(vector_v.get_center(), UP, buff=0.15)

        w_start = RIGHT * 3.5 + UP * 0.1
        w_end = RIGHT * 1.0 + DOWN * 0.5
        vector_w = Arrow(start=w_start, end=w_end, buff=0, color=GREEN_C, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        label_w = MathTex(r"\vec{w}", color=WHITE).next_to(vector_w.get_center(), DOWN, buff=0.15)

        e_start = LEFT * 4 + DOWN * 2.5
        e_end = LEFT * 1.8 + DOWN * 1.8
        vector_e = Arrow(start=e_start, end=e_end, buff=0, color=ORANGE, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        label_e = MathTex(r"\vec{e}", color=WHITE).next_to(vector_e.get_center(), UP, buff=0.15)

        f_start = RIGHT * 0.5 + DOWN * 1.8
        f_end = RIGHT * 2.5 + DOWN * 2.7
        vector_f = Arrow(start=f_start, end=f_end, buff=0, color=ORANGE, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        label_f = MathTex(r"\vec{f}", color=WHITE).next_to(vector_f.get_center(), DOWN, buff=0.15)

        self.add(
            vector_a, label_a, vector_b, label_b,
            vector_v, label_v, vector_w, label_w,
            vector_e, label_e, vector_f, label_f
        )

class VektorenImKoordinatensystem(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-3, 4, 1],
            x_length=8.5,
            y_length=7.0,
            axis_config={"include_numbers": True, "color": GRAY_C},
            tips=True
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        origin = axes.c2p(0, 0)
        point_a = axes.c2p(5, 3)
        point_b = axes.c2p(2, -2)

        vector_a = Arrow(
            start=origin,
            end=point_a,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        label_a = MathTex(r"\vec{a}", color=BLUE_C).next_to(
            vector_a.get_corner(UP + RIGHT), UP + RIGHT, buff=0.1
        )

        vector_b = Arrow(
            start=origin,
            end=point_b,
            buff=0,
            color=GREEN_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        label_b = MathTex(r"\vec{b}", color=GREEN_C).next_to(
            vector_b.get_corner(DOWN + RIGHT), DOWN + RIGHT, buff=0.1
        )

        self.add(axes, labels, vector_a, label_a, vector_b, label_b)

class VektorAddition(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 8, 1],
            y_range=[-1, 4, 1],
            x_length=9.0,
            y_length=5.0,
            axis_config={"include_numbers": True, "color": GRAY_C},
            tips=True
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        origin = axes.c2p(0, 0)
        point_a = axes.c2p(5, 3)
        point_c = axes.c2p(7, 1)

        vector_a = Arrow(
            start=origin,
            end=point_a,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        label_a = MathTex(r"\vec{a}", color=BLUE_C).next_to(
            vector_a.get_center(), UP + LEFT, buff=0.15
        )

        vector_c = Arrow(
            start=origin,
            end=point_c,
            buff=0,
            color=RED_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        label_c = MathTex(r"\vec{c}", color=RED_C).next_to(
            vector_c.get_center(), DOWN + RIGHT, buff=0.15
        )

        vector_b = Arrow(
            start=point_a,
            end=point_c,
            buff=0,
            color=GREEN_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        label_b = MathTex(r"\vec{b}", color=GREEN_C).next_to(
            vector_b.get_center(), UP + RIGHT, buff=0.15
        )

        self.add(axes, labels, vector_a, label_a, vector_c, label_c, vector_b, label_b)

class VektorParallelogramm(Scene):
    def construct(self):
        origin = LEFT * 2.5 + DOWN * 1.5
        vec_a_coords = RIGHT * 4.5 + UP * 0.5
        vec_b_coords = RIGHT * 1.5 + UP * 2.5
        vec_c_coords = vec_a_coords + vec_b_coords

        point_a = origin + vec_a_coords
        point_b = origin + vec_b_coords
        point_c = origin + vec_c_coords

        vector_a = Arrow(
            start=origin, end=point_a, buff=0, color=BLUE_C, stroke_width=5, max_tip_length_to_length_ratio=0.15
        )
        label_a = MathTex(r"\vec{a}", color=BLUE_C).next_to(vector_a.get_center(), DOWN, buff=0.15)

        vector_b = Arrow(
            start=origin, end=point_b, buff=0, color=GREEN_C, stroke_width=5, max_tip_length_to_length_ratio=0.15
        )
        label_b = MathTex(r"\vec{b}", color=GREEN_C).next_to(vector_b.get_center(), LEFT, buff=0.15)

        vector_c = Arrow(
            start=origin, end=point_c, buff=0, color=RED_C, stroke_width=5, max_tip_length_to_length_ratio=0.15
        )
        label_c = MathTex(r"\vec{c}", color=RED_C).next_to(vector_c.get_center(), UP + LEFT, buff=0.1)

        vector_a_prime = DashedLine(
            start=point_b, end=point_c, color=BLUE_C, stroke_width=3
        )
        tip_a_prime = Arrow(
            start=point_c - (vec_a_coords * 0.1), end=point_c, buff=0, color=BLUE_C, stroke_width=3, max_tip_length_to_length_ratio=0.5
        )
        vector_a_prime_group = VGroup(vector_a_prime, tip_a_prime)
        label_a_prime = MathTex(r"\vec{a}", color=BLUE_C).next_to(vector_a_prime.get_center(), UP, buff=0.15)

        vector_b_prime = DashedLine(
            start=point_a, end=point_c, color=GREEN_C, stroke_width=3
        )
        tip_b_prime = Arrow(
            start=point_c - (vec_b_coords * 0.1), end=point_c, buff=0, color=GREEN_C, stroke_width=3, max_tip_length_to_length_ratio=0.5
        )
        vector_b_prime_group = VGroup(vector_b_prime, tip_b_prime)
        label_b_prime = MathTex(r"\vec{b}", color=GREEN_C).next_to(vector_b_prime.get_center(), RIGHT, buff=0.15)

        self.add(
            vector_a, label_a,
            vector_b, label_b,
            vector_c, label_c,
            vector_a_prime_group, label_a_prime,
            vector_b_prime_group, label_b_prime
        )

class Skalarmultiplikation(Scene):
    def construct(self):
        base_dir = RIGHT * 1.2 + UP * 0.9

        pos_a = LEFT * 5.0 + DOWN * 0.5
        vector_a = Arrow(
            start=pos_a,
            end=pos_a + base_dir,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.2
        )
        label_a = MathTex(r"\vec{a}", color=WHITE).next_to(vector_a.get_center(), UP + LEFT, buff=0.15)

        pos_2a = LEFT * 2.2 + DOWN * 1.0
        vector_2a = Arrow(
            start=pos_2a,
            end=pos_2a + 2.0 * base_dir,
            buff=0,
            color=GREEN_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.12
        )
        label_2a = MathTex(r"2\vec{a}", color=WHITE).next_to(vector_2a.get_center(), UP + LEFT, buff=0.15)

        pos_half_a = RIGHT * 1.8 + DOWN * 0.25
        vector_half_a = Arrow(
            start=pos_half_a,
            end=pos_half_a + 0.5 * base_dir,
            buff=0,
            color=YELLOW_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.35
        )
        label_half_a = MathTex(r"0{,}5\vec{a}", color=WHITE).next_to(vector_half_a.get_center(), UP + LEFT, buff=0.15)

        pos_neg_a = RIGHT * 4.8 + UP * 0.5
        vector_neg_a = Arrow(
            start=pos_neg_a,
            end=pos_neg_a - base_dir,
            buff=0,
            color=RED_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.2
        )
        label_neg_a = MathTex(r"-\vec{a}", color=WHITE).next_to(vector_neg_a.get_center(), UP + RIGHT, buff=0.15)

        self.add(
            vector_a, label_a,
            vector_2a, label_2a,
            vector_half_a, label_half_a,
            vector_neg_a, label_neg_a
        )

class VektorBetragKomponenten(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-0.5, 6, 1],
            y_range=[-0.5, 5, 1],
            x_length=8.0,
            y_length=6.0,
            axis_config={"include_numbers": True, "color": GRAY_C},
            tips=True
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        origin = axes.c2p(0, 0)
        ax_val, ay_val = 4.5, 3.5
        point_a = axes.c2p(ax_val, ay_val)
        point_ax = axes.c2p(ax_val, 0)
        point_ay = axes.c2p(0, ay_val)

        vector_a = Arrow(
            start=origin,
            end=point_a,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )
        label_a = MathTex(r"\vec{a}", color=BLUE_C).next_to(
            vector_a.get_center(), UP + LEFT, buff=0.15
        )

        dashed_x = DashedLine(start=point_a, end=point_ax, color=GRAY_A, stroke_width=3)
        dashed_y = DashedLine(start=point_a, end=point_ay, color=GRAY_A, stroke_width=3)

        arrow_ax = DoubleArrow(
            start=axes.c2p(0, -0.2),
            end=axes.c2p(ax_val, -0.2),
            buff=0,
            color=YELLOW_C,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.1
        )
        label_ax = MathTex(r"a_x", color=YELLOW_C).next_to(arrow_ax.get_center(), DOWN, buff=0.1)

        arrow_ay = DoubleArrow(
            start=axes.c2p(-0.2, 0),
            end=axes.c2p(-0.2, ay_val),
            buff=0,
            color=YELLOW_C,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.1
        )
        label_ay = MathTex(r"a_y", color=YELLOW_C).next_to(arrow_ay.get_center(), LEFT, buff=0.1)

        self.add(
            axes, labels,
            vector_a, label_a,
            dashed_x, dashed_y,
            arrow_ax, label_ax,
            arrow_ay, label_ay
        )


class VektorZerlegung(Scene):
    def construct(self):
        origin = LEFT * 2.5 + DOWN * 1.5

        dir_b = RIGHT * 4.2 + UP * 0.7
        dir_c = RIGHT * 1.2 + UP * 2.8

        point_a = origin + dir_b + dir_c
        point_b = origin + dir_b
        point_c = origin + dir_c

        vector_a = Arrow(
            start=origin, end=point_a, buff=0, color=RED_C, stroke_width=6, max_tip_length_to_length_ratio=0.12
        )
        label_a = MathTex(r"\vec{a}", color=RED_C).next_to(vector_a.get_center(), UP + LEFT, buff=0.1)

        vector_b = Arrow(
            start=origin, end=point_b, buff=0, color=BLUE_C, stroke_width=5, max_tip_length_to_length_ratio=0.15
        )
        label_b = MathTex(r"\vec{b}", color=BLUE_C).next_to(vector_b.get_center(), DOWN, buff=0.15)

        vector_c = Arrow(
            start=origin, end=point_c, buff=0, color=GREEN_C, stroke_width=5, max_tip_length_to_length_ratio=0.15
        )
        label_c = MathTex(r"\vec{c}", color=GREEN_C).next_to(vector_c.get_center(), LEFT, buff=0.15)

        dashed_b_parallel = DashedLine(
            start=point_c, end=point_a, color=BLUE_B, stroke_width=3
        )

        dashed_c_parallel = DashedLine(
            start=point_b, end=point_a, color=GREEN_B, stroke_width=3
        )

        line_b_extension = DashedLine(
            start=point_b, end=point_b + (dir_b * 0.3), color=GRAY_B, stroke_width=2
        )
        line_c_extension = DashedLine(
            start=point_c, end=point_c + (dir_c * 0.3), color=GRAY_B, stroke_width=2
        )

        self.add(
            vector_b, label_b,
            vector_c, label_c,
            vector_a, label_a,
            dashed_b_parallel, dashed_c_parallel,
            line_b_extension, line_c_extension
        )

class BewegungImRaum(Scene):
    def construct(self):
        def proj(x, y, z):
            return np.array([
                0.85 * x - 0.70 * z,
                0.75 * y - 0.45 * z,
                0.0
            ])

        o = proj(0, 0, 0)
        x_axis_end = proj(4.5, 0, 0)
        y_axis_end = proj(0, 4.0, 0)
        z_axis_end = proj(0, 0, 4.5)

        axis_x = Arrow(o, x_axis_end, buff=0, color=GRAY_B, stroke_width=3, max_tip_length_to_length_ratio=0.1)
        axis_y = Arrow(o, y_axis_end, buff=0, color=GRAY_B, stroke_width=3, max_tip_length_to_length_ratio=0.1)
        axis_z = Arrow(o, z_axis_end, buff=0, color=GRAY_B, stroke_width=3, max_tip_length_to_length_ratio=0.1)

        label_x = MathTex("x", color=GRAY_A).next_to(x_axis_end, RIGHT, buff=0.1)
        label_y = MathTex("y", color=GRAY_A).next_to(y_axis_end, UP, buff=0.1)
        label_z = MathTex("z", color=GRAY_A).next_to(z_axis_end, DOWN + LEFT, buff=0.1)

        t_vals = np.linspace(0, 1, 100)
        curve_points = []
        for t in t_vals:
            cx = 0.5 + 3.0 * t
            cy = 0.8 + 2.8 * (t ** 0.8) + 0.5 * np.sin(np.pi * t)
            cz = 0.3 + 1.8 * (t ** 1.5)
            curve_points.append(proj(cx, cy, cz))

        curve = VMobject(color=WHITE, stroke_width=4)
        curve.set_points_smoothly(curve_points)

        t1, t2 = 0.25, 0.75

        p1_3d = (0.5 + 3.0 * t1, 0.8 + 2.8 * (t1 ** 0.8) + 0.5 * np.sin(np.pi * t1), 0.3 + 1.8 * (t1 ** 1.5))
        p2_3d = (0.5 + 3.0 * t2, 0.8 + 2.8 * (t2 ** 0.8) + 0.5 * np.sin(np.pi * t2), 0.3 + 1.8 * (t2 ** 1.5))

        pos1 = proj(*p1_3d)
        pos2 = proj(*p2_3d)

        vector_a = Arrow(o, pos1, buff=0, color=BLUE_C, stroke_width=5, max_tip_length_to_length_ratio=0.15)
        label_a = MathTex(r"\vec{a}", color=BLUE_C).next_to(vector_a.get_center(), LEFT, buff=0.15)

        vector_b = Arrow(o, pos2, buff=0, color=GREEN_C, stroke_width=5, max_tip_length_to_length_ratio=0.15)
        label_b = MathTex(r"\vec{b}", color=GREEN_C).next_to(vector_b.get_center(), RIGHT, buff=0.15)

        vector_delta_r = Arrow(pos1, pos2, buff=0, color=RED_C, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        label_delta_r = MathTex(r"\Delta \vec{r}", color=RED_C).next_to(vector_delta_r.get_center(), UP, buff=0.15)

        dot_p1 = Dot(pos1, radius=0.08, color=WHITE)
        dot_p2 = Dot(pos2, radius=0.08, color=WHITE)

        label_p1 = MathTex(r"P_1\ (\text{Zeitpunkt } t_1)", font_size=28, color=WHITE).next_to(pos1, UP + LEFT, buff=0.15)
        label_p2 = MathTex(r"P_2\ (\text{Zeitpunkt } t_2)", font_size=28, color=WHITE).next_to(pos2, UP + RIGHT, buff=0.15)

        self.add(
            axis_x, axis_y, axis_z,
            label_x, label_y, label_z,
            curve,
            vector_a, label_a,
            vector_b, label_b,
            vector_delta_r, label_delta_r,
            dot_p1, dot_p2,
            label_p1, label_p2
        )