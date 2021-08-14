#  Introduction.py

from manim import *
import numpy as np
import sys
sys.path.insert(0, "modules")
import NAugxst as NAugxst
import Python as Python

#     _   _     _____  ___   ___   ___   _     __  _____  _   ___   _
#    | | | |\ |  | |  | |_) / / \ | | \ | | | / /`  | |  | | / / \ | |\ |
#    |_| |_| \|  |_|  |_| \ \_\_/ |_|_/ \_\_/ \_\_  |_|  |_| \_\_/ |_| \|

class Introduction(Scene):
    def construct(self):
        self.introduction()
        self.intro()
        self.answerq1()
        self.answerq2()
        self.answerq3()
        self.outro()

    def introduction(self):
        q1 = Text("1. Python คืออะไร", font="Sarabun").set_color(WHITE)
        q2 = Text("2. Python เอาไปใช้ประโยชน์อะไรได้บ้าง", font="Sarabun").set_color(WHITE)
        q3 = Text("3. Python ในระดับชั้นมัธยมศึกษาปีที่ 1 มีเรื่องอะไรบ้าง", font="Sarabun").set_color(WHITE)
        x = VGroup(q1, q2, q3).arrange(direction=DOWN, aligned_edge=LEFT).scale_in_place(0.7).move_to(ORIGIN)
        x.set_opacity(0)
        self.play(Create(x))
        self.wait(2)
        self.play(Create(x.submobjects[0].set_opacity(1)))
        self.wait(1)
        self.play(Create(x.submobjects[1].set_opacity(1)))
        self.wait(2)
        self.play(Create(x.submobjects[2].set_opacity(1)))
        self.wait(4)
        self.play(Uncreate(x))

    def intro(self):
        logo = NAugxst.NAugxstLogo()
        self.add_sound("assets/Intro_sound.wav")
        self.play(FadeIn(logo))
        self.wait(0.5)

        path = Line([0, 0, 0], [0, 1, 0])
        self.play(MoveAlongPath(logo, path))
        self.wait(0.5)

        vector_text = np.array([0, -1, 0])

        text = Tex("NAugxst")
        text.move_to(vector_text)
        self.play(Create(text))
        self.wait(1)
        self.remove(logo)
        self.remove(text)

    def answerq1(self):
        text = Text("Python คืออะไร", font="Sarabun").scale(0.7)
        line = Line(LEFT*6.5, RIGHT*6.5)
        text.to_edge(UP)
        line.next_to(text, DOWN, buff=0.1)
        self.wait(1)
        self.play(Create(text))
        self.play(Create(line))
        self.wait(1)

        logo = Python.PythonLogo(0.3)
        logo.move_to(np.array([-5, 1, 0]))
        self.play(FadeIn(logo))
        self.wait(1)

        des = Text("Python เป็นภาษาระดับสูงซึ่งสร้างโดย"
                   "\nคีโด ฟัน โรสซึม โดยเริ่มในปี พ.ศ.2533 "
                   "\nการออกแบบของ Python มุ่งเน้นให้ผู้โปรแกรมสามารถอ่าน"
                   "\nชุดคำสั่งได้โดยง่ายผ่านการใช้งานอักขระเว้นว่างจำนวนมาก "
                   "\nนอกจากนั้นการออกแบบ Python และการประยุกต์ใช้แนวคิด"
                   "\nการเขียนโปรแกรมเชิงวัตถุในตัวภาษายังช่วยให้นักเขียนโปรแกรม"
                   "\nสามารถเขียนโปรแกรมที่"
                   "\nเป็นระเบียบ อ่านง่าย มีขนาดเล็ก และง่ายต่อการบำรุง"
                   , font="Sarabun", line_spacing=1).scale(0.5)
        des.move_to(np.array([2, 0, 0]))
        self.play(Create(des), run_time=5)
        self.wait(26)

        self.remove(text, line, logo, des)

    def answerq2(self):
        text = Text("Python เอาไปใช้ประโยชน์อะไรได้บ้าง", font="Sarabun").scale(0.7)
        line = Line(LEFT*6.5, RIGHT*6.5)
        text.to_edge(UP)
        line.next_to(text, DOWN, buff=0.1)
        self.wait(1)
        self.play(Create(text))
        self.play(Create(line))
        self.wait(1)

        tex_py = Tex("Python")
        tex_py.move_to(ORIGIN)
        rect_py = Rectangle(height=tex_py.height+0.4, width=tex_py.width+0.4).move_to(tex_py)
        py = Group(tex_py, rect_py).set_color(YELLOW_C)
        self.play(FadeIn(py))

        tex_ai = Tex("AI")
        tex_ai.move_to(np.array([2, 0, 0]))
        rect_ai = Rectangle(height=tex_ai.height+0.4, width=tex_ai.width+0.4).move_to(tex_ai)
        ai = Group(tex_ai, rect_ai).set_color(WHITE)
        self.play(FadeIn(ai))
        self.wait(3)

        tex_ds = Tex("Data Science")
        tex_ds.move_to(np.array([-3, 0, 0]))
        rect_ds = Rectangle(height=tex_ds.height+0.4, width=tex_ds.width+0.4).move_to(tex_ds)
        ds = Group(tex_ds, rect_ds).set_color(GREEN_C)
        self.play(FadeIn(ds))
        self.wait(1)

        tex_iot = Tex("IoT")
        tex_iot.move_to(np.array([0, 1.5, 0]))
        rect_iot = Rectangle(height=tex_iot.height+0.4, width=tex_iot.width+0.4).move_to(tex_iot)
        iot = Group(tex_iot, rect_iot).set_color(BLUE_C)
        self.play(FadeIn(iot))
        self.wait(2)

        tex_web = Tex("Web Development")
        tex_web.move_to(np.array([0, -1.5, 0]))
        rect_web = Rectangle(height=tex_web.height+0.4, width=tex_web.width+0.4).move_to(tex_web)
        web = Group(tex_web, rect_web).set_color(RED_C)
        self.play(FadeIn(web))
        self.wait(2)

        self.remove(text, line, py, ai, ds, iot, web)

    def answerq3(self):
        text = Text("Python ในระดับชั้นมัธยมศึกษาปีที่ 1 มีเรื่องอะไรบ้าง", font="Sarabun").scale(0.7)
        line = Line(LEFT*6.5, RIGHT*6.5)
        text.to_edge(UP)
        line.next_to(text, DOWN, buff=0.1)
        self.wait(1)
        self.play(Create(text))
        self.play(Create(line))
        self.wait(4)

        c1 = Text("1. เครื่องมือพัฒนาโปรแกรมและการเขียนโปรแกรมอย่างง่าย", font="Sarabun").set_color(WHITE)
        c2 = Text("2. การเขียนโปรแกรมที่มีตัวแปรและตัวดำเนินการ", font="Sarabun").set_color(WHITE)
        c3 = Text("3. การเขียนโปรแกรมแบบวนซ้ำ", font="Sarabun").set_color(WHITE)
        c4 = Text("4. การเขียนโปรแกรมแบบมีทางเลือก", font="Sarabun").set_color(WHITE)
        c = VGroup(c1, c2, c3, c4).arrange(direction=DOWN, aligned_edge=LEFT).scale_in_place(0.7).move_to(ORIGIN)
        c.set_opacity(0)
        self.play(Create(c))
        self.play(Create(c.submobjects[0].set_opacity(1)))
        self.wait(3)
        self.play(Create(c.submobjects[1].set_opacity(1)))
        self.wait(3)
        self.play(Create(c.submobjects[2].set_opacity(1)))
        self.wait(4)
        self.play(Create(c.submobjects[3].set_opacity(1)))
        self.wait(3)

        self.play(c.submobjects[0].animate.set_color(YELLOW))
        self.wait(12)

        self.remove(text, line, c)

    def outro(self):
        youtube = ImageMobject("assets/YoutubeLogo.png").scale(15/128)
        twitter = ImageMobject("assets/TwitterLogo.png").scale(1/5)
        github = ImageMobject("assets/GithubLogo.png")
        youtube.move_to(np.array([-3, 2, 0]))
        twitter.move_to(np.array([-3, 0, 0]))
        github.move_to(np.array([-3, -2, 0]))

        youtube_text = Tex("NAugxst").next_to(youtube, RIGHT, buff=0.5)
        twitter_text = Tex("@AugxstN").next_to(twitter, RIGHT, buff=0.5)
        github_text = Tex("NAugxst").next_to(github, RIGHT, buff=0.5)

        self.wait(2)
        self.wait(9)

        self.play(FadeIn(youtube))
        self.play(FadeIn(twitter))
        self.play(FadeIn(github))

        self.play(Create(youtube_text))
        self.play(Create(twitter_text))
        self.play(Create(github_text))

        self.wait(10)

#    _____  _     _     _      ___   _       __    _   _
#     | |  | |_| | | | | |\/| | |_) | |\ |  / /\  | | | |
#     |_|  |_| | \_\_/ |_|  | |_|_) |_| \| /_/--\ |_| |_|__

class Thumbnail(Scene):
    def construct(self):
        logo = Python.PythonLogo(0.3)
        text = Tex("101")
        logo.move_to([-2, 0, 0])
        text.move_to([1, 0, 0])
        text.scale(4)
        self.add(logo, text)
