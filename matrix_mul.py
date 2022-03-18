from multiprocessing.connection import wait
from manim import *
from ConnectDatabase import database

class MatrixExamples(Scene):
    def construct(self):
        #db = database()
        #db.connect()
        #R_M3=[[0,0,0],[0,0,0],[0,0,0]]
        #R_M3_get = db.select_last()
        
        #for i in range(3):
        #    R_M3[i] = R_M3_get[i].split(",")
        
        #建立矩陣物件集合
        Matrix_set = VGroup()
        
        M1 = Matrix([("1", "2", "3"),("1", "2", "3"),("1", "2", "3")])
        M2 = Matrix([("1", "2", "3"),("1", "2", "3"),("1", "2", "3")])
        M3 = Matrix([("1", "2", "3"),("1", "2", "3"),("1", "2", "3")])
        #M3 = Matrix([(R_M3[0][0],R_M3[0][1],R_M3[0][2]),(R_M3[1][0],R_M3[1][1],R_M3[1][2]),(R_M3[2][0],R_M3[2][1],R_M3[2][2])])

        Matrix_set.add(M1,M2,M3)

        #建立運算子物件集合
        operator_set = VGroup()

        dot = MathTex("\cdot",width=2)
        plus = MathTex("+",width=10)
        subtract = MathTex("-",width=10)
        mul = MathTex("\times",width=10)
        div = MathTex("\div",width=10)
        equal = MathTex("=",width=10)

        operator_set.add(dot,plus,subtract,mul,div,equal)

        #動畫區塊
        self.play(Write(Matrix_set[0].shift(LEFT*5)))
        self.play(AddTextLetterByLetter(operator_set[1].shift(LEFT*2.75)))
        self.play(Write(Matrix_set[1].shift(LEFT*0.5)))
        self.play(AddTextLetterByLetter(operator_set[5].shift(RIGHT*1.75)))
        self.play(Write(Matrix_set[2].shift(RIGHT*4)))

        self.wait(3)