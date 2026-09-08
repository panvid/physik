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