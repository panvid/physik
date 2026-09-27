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