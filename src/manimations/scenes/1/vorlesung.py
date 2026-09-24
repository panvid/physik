from manim import *

class MassepunktWilderPfad(Scene):
    def construct(self):
        punkte = [
            np.array([-5, 2.5, 0]),
            np.array([-3, 3.2, 0]),
            np.array([-1, 1.0, 0]),
            np.array([-2.5, -0.5, 0]),
            np.array([-1.5, -2.5, 0]),
            np.array([0.5, -3.2, 0]),
            np.array([0.8, -1.8, 0]),
            np.array([-0.8, -2.0, 0]),
            np.array([-0.2, -3.0, 0]),
            np.array([2.5, -0.5, 0]),
        ]

        bahnkurve = VMobject()
        bahnkurve.set_points_smoothly(punkte)
        bahnkurve.set_color_by_gradient(BLUE, TEAL, GREEN)

        punkt_position = bahnkurve.get_end()
        massepunkt = Dot(point=punkt_position, radius=0.12, color=RED)

        massepunkt_label = Text("Massepunkt", font_size=24, color=RED)
        massepunkt_label.next_to(massepunkt, RIGHT, buff=0.4)
        massepunkt_pfeil = Arrow(
            start=massepunkt_label.get_left(),
            end=massepunkt.get_center(),
            buff=0.1,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.2,
            color=RED
        )

        bahnkurve_punkt = bahnkurve.point_from_proportion(0.15)
        bahnkurve_label = Text("Bahnkurve", font_size=24, color=TEAL)
        bahnkurve_label.next_to(bahnkurve_punkt, DL, buff=0.4)
        bahnkurve_pfeil = Arrow(
            start=bahnkurve_label.get_right(),
            end=bahnkurve_punkt,
            buff=0.1,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.2,
            color=TEAL
        )

        self.add(
            bahnkurve,
            massepunkt,
            massepunkt_label,
            massepunkt_pfeil,
            bahnkurve_label,
            bahnkurve_pfeil
        )

class Geradlinig(Scene):
    def construct(self):
        linie = Line(start=[-3, 0, 0], end=[3, 0, 0], stroke_width=4, color=BLUE)

        massepunkt = Dot(point=[1, 0, 0], radius=0.15, color=RED)

        self.add(linie, massepunkt)

class Kreisfoermig(Scene):
    def construct(self):
        kreis = Circle(radius=1.8, stroke_width=4, color=TEAL)

        punkt_pos = kreis.point_from_proportion(0.125)
        massepunkt = Dot(point=punkt_pos, radius=0.15, color=RED)

        self.add(kreis, massepunkt)

class KrummlinigChaotisch(Scene):
    def construct(self):
        punkte = [
            np.array([-3, -1.5, 0]),
            np.array([-2, 1.8, 0]),
            np.array([-0.5, -1.2, 0]),
            np.array([1, 1.5, 0]),
            np.array([1.8, -1.5, 0]),
            np.array([0.8, -0.8, 0]),
            np.array([2.8, 0.5, 0])
        ]

        pfad = VMobject()
        pfad.set_points_smoothly(punkte)
        pfad.set_stroke(width=4)
        pfad.set_color_by_gradient(BLUE, TEAL, GREEN)

        massepunkt = Dot(point=pfad.get_end(), radius=0.15, color=RED)

        self.add(pfad, massepunkt)

class Ortsvektor3D(Scene):
    def construct(self):
        origin = LEFT * 2 + DOWN * 1.5

        y_axis = Arrow(start=origin, end=origin + UP * 4.5, buff=0, color=WHITE)
        y_label = MathTex("y").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 5.5, buff=0, color=WHITE)
        x_label = MathTex("x").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        z_end = origin + DL * 1.5
        z_axis = Arrow(start=origin, end=z_end, buff=0, color=WHITE)
        z_label = MathTex("z").next_to(z_axis.get_end(), DL, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, z_axis, x_label, y_label, z_label)

        punkte = [
            origin + RIGHT * 0.8 + UP * 0.5 + DL * 0.3,
            origin + RIGHT * 1.8 + UP * 2.2 + DL * 0.8,
            origin + RIGHT * 3.2 + UP * 1.5 + DL * 0.2,
            origin + RIGHT * 4.0 + UP * 3.2 + DL * 0.5,
        ]

        kurve = VMobject()
        kurve.set_points_smoothly(punkte)
        kurve.set_stroke(width=4)
        kurve.set_color_by_gradient(BLUE, TEAL, GREEN)

        punkt_pos = kurve.get_end()
        massepunkt = Dot(point=punkt_pos, radius=0.12, color=RED)

        ortsvektor = Arrow(
            start=origin,
            end=punkt_pos,
            buff=0,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )

        r_label = MathTex(r"\vec{r}", color=YELLOW, font_size=36)
        r_label.next_to(ortsvektor.get_center(), UL, buff=0.1)

        self.add(axes_group, kurve, massepunkt, ortsvektor, r_label)

class GeradlinigOrtsvektor(Scene):
    def construct(self):
        origin = LEFT * 2 + DOWN * 1

        y_axis = Arrow(start=origin, end=origin + UP * 4, buff=0, color=WHITE)
        y_label = MathTex("y").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 6.5, buff=0, color=WHITE)
        x_label = MathTex("x").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        z_end = origin + DL * 1.5
        z_axis = Arrow(start=origin, end=z_end, buff=0, color=WHITE)
        z_label = MathTex("z").next_to(z_axis.get_end(), DL, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, z_axis, x_label, y_label, z_label)

        punkt_pos = origin + RIGHT * 4.5

        ortsvektor = Arrow(
            start=origin,
            end=punkt_pos,
            buff=0,
            color=YELLOW,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.12
        )

        r_label = MathTex(r"\vec{r}", color=YELLOW, font_size=36)
        r_label.next_to(ortsvektor.get_center(), UP, buff=0.15)

        massepunkt = Dot(point=punkt_pos, radius=0.12, color=RED)

        self.add(axes_group, ortsvektor, r_label, massepunkt)

class OrtZeitDiagramm(Scene):
    def construct(self):
        origin = LEFT * 2.5 + DOWN * 2

        y_axis = Arrow(start=origin, end=origin + UP * 4.5, buff=0, color=WHITE)
        y_label = Text("Ort x", font_size=24).next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 5.5, buff=0, color=WHITE)
        x_label = Text("Zeit t", font_size=24).next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        gerade = Line(
            start=origin,
            end=origin + RIGHT * 4.5 + UP * 3.5,
            stroke_width=4,
            color=BLUE
        )

        self.add(axes_group, gerade)

class GeschwindigkeitZeitDiagramm(Scene):
    def construct(self):
        origin = LEFT * 2.5 + DOWN * 2

        y_axis = Arrow(start=origin, end=origin + UP * 4.5, buff=0, color=WHITE)
        y_label = Text("Geschwindigkeit v", font_size=24).next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 5.5, buff=0, color=WHITE)
        x_label = Text("Zeit t", font_size=24).next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        v_hoehe = origin + UP * 2.5
        gerade = Line(
            start=v_hoehe,
            end=v_hoehe + RIGHT * 5.0,
            stroke_width=4,
            color=BLUE
        )

        self.add(axes_group, gerade)

class OrtZeitWellenDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3 + DOWN * 2

        y_axis = Arrow(start=origin, end=origin + UP * 4.5, buff=0, color=WHITE)
        y_label = MathTex("x").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 6.5, buff=0, color=WHITE)
        x_label = MathTex("t").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        punkte = [
            origin + RIGHT * 0.0 + UP * 0.5,
            origin + RIGHT * 1.0 + UP * 2.2,
            origin + RIGHT * 2.2 + UP * 3.5,
            origin + RIGHT * 3.5 + UP * 1.8,
            origin + RIGHT * 4.8 + UP * 0.5,
            origin + RIGHT * 5.8 + UP * 2.0,
        ]

        kurve = VMobject()
        kurve.set_points_smoothly(punkte)
        kurve.set_stroke(width=4, color=BLUE)

        zeitpunkte = [
            (0.20, "t_1"),
            (0.383, "t_3"),
            (0.65, "t_2"),
        ]

        punkte_group = VGroup()

        for prop, label_text in zeitpunkte:
            pos = kurve.point_from_proportion(prop)

            t_achsen_pos = np.array([pos[0], origin[1], 0])

            linie = DashedLine(start=pos, end=t_achsen_pos, stroke_width=2, color=GRAY)

            dot = Dot(point=pos, radius=0.08, color=RED)

            label = MathTex(label_text).next_to(t_achsen_pos, DOWN, buff=0.15)

            tangente = TangentLine(kurve, alpha=prop, length=2.2, stroke_width=3, color=YELLOW)

            punkte_group.add(linie, tangente, dot, label)

        self.add(axes_group, kurve, punkte_group)

class BeschleunigtVZeitDiagramm(Scene):
    def construct(self):
        origin = LEFT * 2.5 + DOWN * 2

        y_axis = Arrow(start=origin, end=origin + UP * 4.5, buff=0, color=WHITE)
        y_label = MathTex("v").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 5.5, buff=0, color=WHITE)
        x_label = MathTex("t").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        gerade_ende = origin + RIGHT * 4.5 + UP * 3.5
        gerade = Line(
            start=origin,
            end=gerade_ende,
            stroke_width=4,
            color=BLUE
        )

        gerade_label = Text("Ursprungsgerade", font_size=20, color=BLUE)
        gerade_label.next_to(gerade.get_center(), UL, buff=0.15)
        gerade_label.rotate(gerade.get_angle(), about_point=gerade_label.get_center())

        self.add(axes_group, gerade, gerade_label)

class BeschleunigtXZeitDiagramm(Scene):
    def construct(self):
        origin = LEFT * 2.5 + DOWN * 2

        y_axis = Arrow(start=origin, end=origin + UP * 4.5, buff=0, color=WHITE)
        y_label = MathTex("x").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 5.5, buff=0, color=WHITE)
        x_label = MathTex("t").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        # x(t) ~ t^2
        parabel = ParametricFunction(
            lambda t: origin + RIGHT * t + UP * (0.18 * t**2),
            t_range=[0, 4.5],
            stroke_width=4,
            color=BLUE
        )

        parabel_punkt = parabel.point_from_proportion(0.65)
        parabel_label = Text("Parabel", font_size=20, color=BLUE)
        parabel_label.next_to(parabel_punkt, UL, buff=0.15)

        self.add(axes_group, parabel, parabel_label)

class BeschleunigtAZeitDiagramm(Scene):
    def construct(self):
        origin = LEFT * 2.5 + DOWN * 2

        y_axis = Arrow(start=origin, end=origin + UP * 4.5, buff=0, color=WHITE)
        y_label = MathTex("a").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 5.5, buff=0, color=WHITE)
        x_label = MathTex("t").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        a_hoehe = origin + UP * 2.5
        gerade = Line(
            start=a_hoehe,
            end=a_hoehe + RIGHT * 5.0,
            stroke_width=4,
            color=BLUE
        )

        self.add(axes_group, gerade)

class AufgabenstellungSzene(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-1, 10, 1],
            y_range=[-1, 3, 1],
            x_length=12,
            y_length=4,
            axis_config={"include_tip": True, "tip_shape": StealthTip},
        )
        x_label = ax.get_x_axis_label(Tex("x"))
        self.add(ax.get_x_axis(), x_label)

        car_body = Rectangle(width=2, height=0.8, fill_opacity=1, color=BLUE)
        car_roof = Rectangle(width=1.2, height=0.5, fill_opacity=1, color=BLUE_D).next_to(car_body, UP, buff=0)
        wheel1 = Circle(radius=0.25, fill_opacity=1, color=BLACK).move_to(car_body.get_bottom() + LEFT * 0.6)
        wheel2 = Circle(radius=0.25, fill_opacity=1, color=BLACK).move_to(car_body.get_bottom() + RIGHT * 0.6)
        car = VGroup(car_body, car_roof, wheel1, wheel2)
        car.move_to(ax.c2p(1, 0) + UP * 0.65)

        cyclist_torso = Line(start=ORIGIN, end=UP * 0.8, color=GREEN_E, stroke_width=6)
        cyclist_head = Circle(radius=0.15, fill_opacity=1, color=GREEN_E).next_to(cyclist_torso, UP, buff=0)
        wheel_b = Circle(radius=0.2, color=BLACK, stroke_width=4).move_to(
            cyclist_torso.get_bottom() + LEFT * 0.3 + DOWN * 0.2)
        wheel_f = Circle(radius=0.2, color=BLACK, stroke_width=4).move_to(
            cyclist_torso.get_bottom() + RIGHT * 0.3 + DOWN * 0.2)

        frame_back = Line(wheel_b.get_center(), cyclist_torso.get_bottom(), color=GRAY, stroke_width=3)
        frame_front = Line(wheel_f.get_center(), cyclist_torso.get_bottom(), color=GRAY, stroke_width=3)
        frame_top = Line(cyclist_torso.get_bottom(), cyclist_torso.get_center(), color=GRAY, stroke_width=3)

        cyclist = VGroup(cyclist_torso, cyclist_head, wheel_f, wheel_b, frame_back, frame_front, frame_top)
        cyclist.move_to(ax.c2p(7, 0) + UP * 0.7)

        dist_line = DoubleArrow(
            start=car.get_right() + UP * 0.2,
            end=cyclist.get_left() + UP * 0.2,
            buff=0.1,
            color=RED
        )
        dist_label = MathTex("20\,m", color=RED).next_to(dist_line, UP, buff=0.1)
        distance_group = VGroup(dist_line, dist_label)

        self.add(car, cyclist, distance_group)

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

class VerzögerteBewegungSzene(Scene):
    def construct(self):
        boden = Line(start=LEFT * 5, end=RIGHT * 5, color=GRAY, stroke_width=3)
        boden_label = MathTex("x").next_to(boden.get_end(), RIGHT, buff=0.15)
        boden_gruppe = VGroup(boden, boden_label).shift(DOWN * 1.5)

        def create_car(color=BLUE, opacity=1.0):
            body = Rectangle(width=2.0, height=0.7, fill_opacity=opacity, color=color)
            roof = Rectangle(width=1.1, height=0.45, fill_opacity=opacity, color=color).next_to(body, UP, buff=0)
            wheel1 = Circle(radius=0.22, fill_opacity=opacity, color=BLACK).move_to(body.get_bottom() + LEFT * 0.55)
            wheel2 = Circle(radius=0.22, fill_opacity=opacity, color=BLACK).move_to(body.get_bottom() + RIGHT * 0.55)
            return VGroup(body, roof, wheel1, wheel2)

        start_pos = LEFT * 3 + DOWN * 1.05
        car_start = create_car(color=BLUE)
        car_start.move_to(start_pos)

        v0_arrow = Arrow(
            start=car_start.get_top() + UP * 0.3 + LEFT * 0.5,
            end=car_start.get_top() + UP * 0.3 + RIGHT * 0.8,
            color=YELLOW,
            buff=0
        )
        v0_label = MathTex("v_0", color=YELLOW).next_to(v0_arrow, UP, buff=0.1)
        v0_gruppe = VGroup(v0_arrow, v0_label)

        end_pos = RIGHT * 2 + DOWN * 1.05
        car_end = create_car(color=GRAY, opacity=0.4)
        car_end.move_to(end_pos)

        v_end_label = MathTex("v = 0", color=RED).next_to(car_end.get_top(), UP, buff=0.2)

        rollweg_start = np.array([car_start.get_center()[0], boden.get_y() - 0.4, 0])
        rollweg_end = np.array([car_end.get_center()[0], boden.get_y() - 0.4, 0])

        rollweg_arrow = DoubleArrow(
            start=rollweg_start,
            end=rollweg_end,
            buff=0,
            color=WHITE
        )
        rollweg_label = MathTex(r"\text{Rollweg } \Delta x = 0{,}85\,\text{m}", font_size=28).next_to(rollweg_arrow, DOWN, buff=0.15)
        rollweg_gruppe = VGroup(rollweg_arrow, rollweg_label)

        self.add(boden_gruppe, car_start, v0_gruppe, car_end, v_end_label, rollweg_gruppe)

class XTDiagramm(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="t", y_label="x")

        graph = ax.plot(lambda t: t, x_range=[0, 4.5], color=BLUE)

        self.add(ax, labels, graph)

class VTDiagramm(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="t", y_label="v")

        graph = ax.plot(lambda t: 2.5, x_range=[0, 4.5], color=GREEN)

        self.add(ax, labels, graph)

class ATDiagramm(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="t", y_label="a")

        graph = ax.plot(lambda t: 0, x_range=[0, 4.5], color=RED, stroke_width=6)

        self.add(ax, labels, graph)

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

class ZugUndPersonSzene(Scene):
    def construct(self):
        boden = Line(start=LEFT * 6, end=RIGHT * 6, color=GRAY, stroke_width=3)
        boden_label = MathTex("x").next_to(boden.get_end(), RIGHT, buff=0.15)
        boden_gruppe = VGroup(boden, boden_label).shift(DOWN * 1.5)

        zug_body = Rectangle(width=5.0, height=1.2, fill_opacity=1, color=BLUE_D)

        fenster_gruppe = VGroup(*[
            Square(side_length=0.4, fill_opacity=1, color=LIGHT_GRAY)
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.4).move_to(zug_body.get_center() + UP * 0.1)

        raeder = VGroup(*[
            Circle(radius=0.2, fill_opacity=1, color=BLACK)
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.8).move_to(zug_body.get_bottom() + DOWN * 0.1)

        zug = VGroup(zug_body, fenster_gruppe, raeder)
        zug.move_to(LEFT * 2.5 + DOWN * 0.8)

        a2_label = MathTex("a_2 = 0{,}4\\,\\text{m/s}^2", color=BLUE_B, font_size=32)
        a2_label.next_to(zug, UP, buff=0.2)

        person_head = Circle(radius=0.12, fill_opacity=1, color=ORANGE)
        person_body = Line(start=ORIGIN, end=DOWN * 0.5, color=ORANGE, stroke_width=4)
        person_head.next_to(person_body, UP, buff=0)
        person = VGroup(person_head, person_body)

        person.move_to(zug.get_right() + RIGHT * 0.15 + DOWN * 0.5)

        v1_arrow = Arrow(
            start=person.get_top() + RIGHT * 0.1,
            end=person.get_top() + RIGHT * 1.5,
            color=YELLOW,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        v1_label = MathTex("v_1 = 4\\,\\text{km/h}", color=YELLOW, font_size=28).next_to(v1_arrow, UP, buff=0.1)
        v1_gruppe = VGroup(v1_arrow, v1_label)

        self.add(boden_gruppe, zug, a2_label, person, v1_gruppe)

class ZugPersonXTDiagramm(Scene):
    def construct(self):
        origin = LEFT * 3.5 + DOWN * 2.5

        y_axis = Arrow(start=origin, end=origin + UP * 5.5, buff=0, color=WHITE)
        y_label = MathTex("x").next_to(y_axis.get_end(), UP, buff=0.15)

        x_axis = Arrow(start=origin, end=origin + RIGHT * 7.5, buff=0, color=WHITE)
        x_label = MathTex("t").next_to(x_axis.get_end(), RIGHT, buff=0.15)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)

        schnittpunkt_pos = origin + RIGHT * 4.0 + UP * 3.5

        gerade_person = Line(
            start=origin,
            end=origin + RIGHT * 5.5 + UP * 4.8125,
            stroke_width=4,
            color=YELLOW
        )
        label_person = MathTex("x_1\\text{ (Person)}", color=YELLOW, font_size=28)
        label_person.next_to(gerade_person.get_end(), RIGHT, buff=0.15)

        parabel_zug = ParametricFunction(
            lambda t: origin + RIGHT * t + UP * (0.21875 * t**2),
            t_range=[0, 4.8],
            stroke_width=4,
            color=BLUE
        )
        label_zug = MathTex("x_2\\text{ (Zug)}", color=BLUE, font_size=28)
        label_zug.next_to(parabel_zug.point_from_proportion(0.95), UL, buff=0.15)

        schnittpunkt_dot = Dot(point=schnittpunkt_pos, radius=0.08, color=RED)

        ueberholt_label = Text("Zug überholt Person", font_size=18, color=RED)
        ueberholt_label.next_to(schnittpunkt_pos, UL, buff=0.15)

        t_schnitt_pos = np.array([schnittpunkt_pos[0], origin[1], 0])
        linie_t = DashedLine(start=schnittpunkt_pos, end=t_schnitt_pos, stroke_width=2, color=GRAY)
        label_t = MathTex("t_{\\ddot{u}}").next_to(t_schnitt_pos, DOWN, buff=0.15)

        x_schnitt_pos = np.array([origin[0], schnittpunkt_pos[1], 0])
        linie_x = DashedLine(start=schnittpunkt_pos, end=x_schnitt_pos, stroke_width=2, color=GRAY)
        label_x = MathTex("x_{\\ddot{u}}").next_to(x_schnitt_pos, LEFT, buff=0.15)

        self.add(
            axes_group,
            gerade_person,
            label_person,
            parabel_zug,
            label_zug,
            linie_t,
            linie_x,
            schnittpunkt_dot,
            ueberholt_label,
            label_t,
            label_x
        )