from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
import random
import time
import matplotlib.pyplot as plt

root = Tk()
root.title("KBC")
root.geometry("1980x1080")
root.iconbitmap(bitmap="C:/Users/DEVANSH/Downloads/kbc_logo.ico")
mixer.init()
mixer.music.load("C:/Users/DEVANSH/Downloads/kbc.mp3")
mixer.music.play()
gif1 = ImageTk.PhotoImage(Image.open("C:/Users/DEVANSH/Pictures/kbc_background.jpg"))
gif2 = ImageTk.PhotoImage(Image.open("C:/Users/DEVANSH/Pictures/kbc_bg.jpg"))
temp = ImageTk.PhotoImage(Image.open("C:/Users/DEVANSH/Pictures/temp.png"))
temp1 = ImageTk.PhotoImage(Image.open("C:/Users/DEVANSH/Pictures/loss screen.png"))
life = ImageTk.PhotoImage(Image.open("C:/Users/DEVANSH/Pictures/aud.png"))

K1 = Label(root)
K1.pack()

q1 = "The 'Dalong Village' covering an area of 11.35 sq. km.\n has recently (May 2017) been declared as \
    Biodiversity Heritage Site under Section 37(1) of \nBiological Diversity Act, 2002. \n" \
     "The village is situated in the Indian State of -"
q2 = "........... is the first woman to head a public sector bank."
q3 = "World Tourism Day is celebrated on-"
q4 = "The two - day festival 'North East Calling', is organized bywhich ministry ?"
q5 = "When is the International Yoga Day celebrated ?"
q6 = "When Government of India confers the Highest Civilian Honor for Women by presenting Nari Shakti Puraskars?"
q7 = "The motif of 'Hampi with Chariot' is printed on the reverse of which currency note ?"
q8 = "Election Commission of India has decided that the voter's identification shall be mandatory \n" \
     "in the elections at the time of poll. Which of the following shall be \n" \
     "the main document of identification of a voter ?"
q9 = " The largest biotechnology meeting of India was organized in which city?"
q10 = " Should all train engines operated by coal be converted to electric engines?"
q11 = "The Insurance Regulatory and Development Authority (IRDA) is a -"
q12 = "What is the name of Indira Gandhi's Samadhi?"
q13 = "Which one of the following states of India has made unique venture of \n" \
      "putting daughter’s nameplate on the front of the house?"
q14 = "Who among the following Scientists got two Nobel prizes of which one was in Peace?"
q15 = "What is the approximate present irrigation potential, in lakh hectares, of Madhya Pradesh?"
QA = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]

def win():
    if c == 1:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 1,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10, height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()

    if c == 2:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 2,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10, height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 3:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 3,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10, height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 4:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 5,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10, height=1)
        H1.place(x=600, y=350)
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 5:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 10,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10, height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 6:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 20,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10, height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    # ------------------------------------------------------------------------------------------------------
    if c == 7:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 40,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10, height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 8:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 80,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10, height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 9:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 1,60,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10,
                   height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 10:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="!!!!!!***Rs 3,20,000***!!!", fg='Orange', bg='black', font=("Times New Roman", 40),
                   width=10, height=1)
        H1.place(x=600, y=350)
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 11:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 6,25,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10,
                   height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 12:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 12,50,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10,
                   height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()

    if c == 13:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 25,00,0000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10,
                   height=1)
        H1.place(x=600, y=350)
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 14:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="Rs 50,00,000", fg='Orange', bg='black', font=("Times New Roman", 40), width=10,
                   height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()
    if c == 15:
        canvas = Canvas(root, bg='black', width=1920, height=1080)
        canvas.create_image(765, 400, image=temp1)
        canvas.place(x=0, y=0)
        H1 = Label(canvas, text="!!!***$$$--Rs 1 CRORE--$$$***!!!", fg='Orange', bg=(255, 215, 0),
                   font=("Times New Roman", 40), width=10, height=1)
        H1.place(x=600, y=350)
        root.update()
        mixer.init()
        mixer.music.load("C:/Users/DEVANSH/Downloads/Right Answer.mp3")
        mixer.music.play()
        root.after(5000, None)
        canvas.destroy()



def Q_sound():
    root.update()
    mixer.init()
    mixer.music.load("C:/Users/DEVANSH/Downloads/Kbc Option Lock Tune.mp3")
    mixer.music.play()
    time.sleep(5)
    pic()


def Q1_sound():
    over()


def over():
    canvas = Canvas(root, bg='black', width=1920, height=1080)
    canvas.create_image(765, 400, image=temp1)
    canvas.place(x=0, y=0)
    H1 = Label(canvas, text="Rs 0", fg='Orange', bg='black', font=("Times New Roman", 40), width=10, height=1)
    H1.place(x=600, y=350)
    mixer.init()
    mixer.music.load("C:/Users/DEVANSH/Downloads/Wrong Answer.mp3")
    mixer.music.play()
    root.update()
    root.after(5000, None)
    root.destroy()


t = 0
c = -1


def time1():
    time.sleep(0.9)
    root.after(2500,None)
    mixer.init()
    mixer.music.load("C:/Users/DEVANSH/Downloads/Kbc Clock.mp3")
    mixer.music.play()
    global t
    s = t + 1
    while s != 31:
        t1.configure(text=s)
        root.update()
        time.sleep(1)
        s = s + 1
        if s == 30:
            over()


def work():
    '''root.after(5000, None)
    mixer.init()
    mixer.music.load("C:/Users/DEVANSH/Downloads/kbc_Q.mp3")
    mixer.music.play()'''
    time.sleep(1)
    global key0, key1, key2, key3, c
    if str(Q_random) == q1:
        S1 = ['Manipur', 'Madhya Pradesh', 'Mizoram', 'Maharashtra ']
        random.shuffle(S1)
        op1.configure(text=S1[0])
        op2.configure(text=S1[1])
        op3.configure(text=S1[2])
        op4.configure(text=S1[3])

        def key0(event):
            if S1[0] == 'Madhya Pradesh':
                op1.configure(bg='green')
                Q_sound()

            elif S1[0] != 'Madhya Pradesh':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S1[1] == 'Madhya Pradesh':
                op2.configure(bg='green')
                Q_sound()

            elif S1[1] != 'Madhya Pradesh':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S1[2] == 'Madhya Pradesh':
                op3.configure(bg='green')
                Q_sound()

            elif S1[2] != 'Madhya Pradesh':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S1[3] == 'Madhya Pradesh':
                op4.configure(bg='green')
                Q_sound()

            elif S1[3] != 'Madhya Pradesh':
                op4.configure(bg='red')
                Q1_sound()




    elif str(Q_random) == q2:
        S2 = ['Arundhati Bhattacharya', 'Shikha Sharma', 'Chanda Kochar', 'Usha Ananthasubramanyan']
        random.shuffle(S2)
        op1.configure(text=S2[0])
        op2.configure(text=S2[1])
        op3.configure(text=S2[2])
        op4.configure(text=S2[3])

        def key0(event):

            if S2[0] == 'Arundhati Bhattacharya':
                op1.configure(bg='green')
                Q_sound()


            elif S2[0] != 'Arundhati Bhattacharya':
                op1.configure(bg='red')
                Q1_sound()


        def key1(event):
            if S2[1] == 'Arundhati Bhattacharya':
                op2.configure(bg='green')
                Q_sound()

            elif S2[1] != 'Arundhati Bhattacharya':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S2[2] == 'Arundhati Bhattacharya':
                op3.configure(bg='green')
                Q_sound()

            elif S2[2] != 'Arundhati Bhattacharya':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S2[3] == 'Arundhati Bhattacharya':
                op3.configure(bg='green')
                Q_sound()

            elif S2[3] != 'Arundhati Bhattacharya':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q3:
        S3 = ['September 12', 'September 25', 'September 27', 'September 29']
        random.shuffle(S3)
        op1.configure(text=S3[0])
        op2.configure(text=S3[1])
        op3.configure(text=S3[2])
        op4.configure(text=S3[3])

        def key0(event):
            if S3[0] == 'September 27':
                op1.configure(bg='green')
                Q_sound()

            elif S3[0] != 'September 27':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S3[1] == 'September 27':
                op2.configure(bg='green')
                Q_sound()

            elif S3[1] != 'September 27':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S3[2] == 'September 27':
                op1.configure(bg='green')
                Q_sound()

            elif S3[2] != 'September 27':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S3[3] == 'September 27':
                op3.configure(bg='green')
                Q_sound()

            elif S3[3] != 'September 27':
                op4.configure(bg='red')
                Q1_sound()
    elif str(Q_random) == q4:
        S4 = ['Ministry of Development \nof North Eastern Region (DoNER)', 'Ministry of External Affairs',
              'Ministry of Home Affairs', 'Ministry of Defence']
        random.shuffle(S4)
        op1.configure(text=S4[0])
        op2.configure(text=S4[1])
        op3.configure(text=S4[2])
        op4.configure(text=S4[3])

        def key0(event):
            if S4[0] == 'Ministry of Development \nof North Eastern Region (DoNER)':
                op1.configure(bg='green')
                Q_sound()

            elif S4[0] != 'Ministry of Development \nof North Eastern Region (DoNER)':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S4[1] == 'Ministry of Development \nof North Eastern Region (DoNER)':
                op2.configure(bg='green')
                Q_sound()

            elif S4[1] != 'Ministry of Development \nof North Eastern Region (DoNER)':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S4[2] == 'Ministry of Development \nof North Eastern Region (DoNER)':
                op3.configure(bg='green')
                Q_sound()

            elif S4[2] != 'Ministry of Development \nof North Eastern Region (DoNER)':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S4[3] == 'Ministry of Development \nof North Eastern Region (DoNER)':
                op4.configure(bg='green')
                Q_sound()

            elif S4[3] != 'Ministry of Development \nof North Eastern Region (DoNER)':
                op4.configure(bg='red')
                Q1_sound()


    elif str(Q_random) == q5:
        S5 = ['June 21', 'March 21', 'April 22', 'May 31']
        random.shuffle(S5)
        op1.configure(text=S5[0])
        op2.configure(text=S5[1])
        op3.configure(text=S5[2])
        op4.configure(text=S5[3])

        def key0(event):
            if S5[0] == 'June 21':
                op1.configure(bg='green')
                Q_sound()

            elif S5[0] != 'June 21':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S5[1] == ' June 21':
                op2.configure(bg='green')
                Q_sound()

            elif S5[1] != 'June 21':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S5[2] == 'June 21':
                op3.configure(bg='green')
                Q_sound()

            elif S5[2] != 'June 21':
                op3.configure(bg='red')
                root.update()
                Q1_sound()

        def key3(event):
            if S5[3] == 'June 21':
                op4.configure(bg='green')
                Q_sound()
            elif S5[3] != 'June 21':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q6:
        S6 = ['June 5', '8th March, every year, International Women s Day', 'June 21', ' April 7']
        random.shuffle(S6)
        op1.configure(text=S6[0])
        op2.configure(text=S6[1])
        op3.configure(text=S6[2])
        op4.configure(text=S6[3])

        def key0(event):
            if S6[0] == '8th March, every year, International Women s Day':
                op1.configure(bg='green')
                Q_sound()
            elif S6[0] != '8th March, every year, International Women s Day':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S6[1] == ' 8th March, every year, International Women s Day':
                op2.configure(bg='green')
                Q_sound()

            elif S6[1] != '8th March, every year, International Women s Day':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S6[2] == '8th March, every year, International Women s Day':
                op3.configure(bg='green')
                Q_sound()

            elif S6[2] != '8th March, every year, International Women s Day':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S6[3] == '8th March, every year, International Women s Day':
                op4.configure(bg='green')
                Q_sound()

            elif S6[3] != '8th March, every year, International Women s Day':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q7:
        S7 = ['One Rupee Note', 'Rs. 500 note', 'Rs. 50 note', 'Rs. 1000 note']
        random.shuffle(S7)
        op1.configure(text=S7[0])
        op2.configure(text=S7[1])
        op3.configure(text=S7[2])
        op4.configure(text=S7[3])

        def key0(event):
            if S7[0] == 'Rs. 50 note':
                op1.configure(bg='green')
                Q_sound()

            elif S7[0] != 'Rs. 50 note':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S7[1] == 'Rs. 50 note':
                op2.configure(bg='green')
                Q_sound()

            elif S7[1] != 'Rs. 50 note':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S7[2] == 'Rs. 50 note':
                op3.configure(bg='green')
                Q_sound()

            elif S7[2] != 'Rs. 50 note':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S7[3] == 'Rs. 50 note':
                op4.configure(bg='green')

                Q_sound()
            elif S7[3] != 'Rs. 50 note':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q8:
        S8 = ['Voter Slip', 'Electoral Photo Identity Cards (EPIC)', 'Indelible ink mark', 'Electoral rolls']
        random.shuffle(S8)
        op1.configure(text=S8[0])
        op2.configure(text=S8[1])
        op3.configure(text=S8[2])
        op4.configure(text=S8[3])

        def key0(event):
            if S8[0] == 'Electoral Photo Identity Cards (EPIC)':
                op1.configure(bg='green')
                Q_sound()

            elif S8[0] != 'Electoral Photo Identity Cards (EPIC)':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S8[1] == 'Electoral Photo Identity Cards (EPIC)':
                op2.configure(bg='green')
                Q_sound()

            elif S8[1] != 'Electoral Photo Identity Cards (EPIC)':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S8[2] == 'Electoral Photo Identity Cards (EPIC)':
                op3.configure(bg='green')
                Q_sound()

            elif S8[2] != 'Electoral Photo Identity Cards (EPIC)':
                op3.configure(bg='red')
                root.update()
                Q1_sound()

        def key3(event):
            if S8[3] == 'Electoral Photo Identity Cards (EPIC)':
                op4.configure(bg='green')
                Q_sound()

            elif S8[3] != 'Electoral Photo Identity Cards (EPIC)':
                op4.configure(bg='red')
                root.update()
                Q1_sound()

    elif str(Q_random) == q9:
        S9 = ['New Delhi', 'Manesar', 'Leh', 'Hissar']
        random.shuffle(S9)
        op1.configure(text=S9[0])
        op2.configure(text=S9[1])
        op3.configure(text=S9[2])
        op4.configure(text=S9[3])

        def key0(event):
            if S9[0] == 'New Delhi':
                op1.configure(bg='green')
                Q_sound()

            elif S9[0] != 'New Delhi':
                op1.configure(bg='red')
                root.update()
                Q1_sound()

        def key1(event):
            if S9[1] == 'New Delhi':
                op2.configure(bg='green')
                Q_sound()

            elif S9[1] != 'New Delhi':
                op2.configure(bg='red')
                root.update()
                Q1_sound()

        def key2(event):
            if S9[2] == 'New Delhi':
                op3.configure(bg='green')
                Q_sound()

            elif S9[2] != 'New Delhi':
                op3.configure(bg='red')
                root.update()
                Q1_sound()

        def key3(event):
            if S9[3] == 'New Delhi':
                op4.configure(bg='green')
                Q_sound()

            elif S9[3] != 'New Delhi':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q10:
        S10 = ['Yes, coal engines pollute the \nenvironment more than electric engines',
               'Yes, electric engines are more powerful and efficient', 'No, we do not have enough electric\n '
                                                                        'power to cater to the need of domestic use',
               'No, we have enough coals to run train engines']
        random.shuffle(S10)
        op1.configure(text=S10[0])
        op2.configure(text=S10[1])
        op3.configure(text=S10[2])
        op4.configure(text=S10[3])

        def key0(event):
            if S10[0] == 'Yes, coal engines pollute the \nenvironment more than electric engines':
                op1.configure(bg='green')
                Q_sound()

            elif S10[0] != 'Yes, coal engines pollute \nthe environment more than electric engines':
                op1.configure(bg='red')
                root.update()
                Q1_sound()

        def key1(event):
            if S10[1] == 'Yes, coal engines pollute \nthe environment more than electric engines':
                op2.configure(bg='green')
                Q_sound()

            elif S10[1] != 'Yes, coal engines pollute \nthe environment more than electric engines':
                op2.configure(bg='red')
                root.update()
                Q1_sound()

        def key2(event):
            if S10[2] == 'Yes, coal engines pollute \nthe environment more than electric engines':
                op3.configure(bg='green')
                Q_sound()

            elif S10[2] != 'Yes, coal engines pollute \nthe environment more than electric engines':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S10[3] == 'Yes, coal engines pollute \nthe environment more than electric engines':
                op4.configure(bg='green')
                Q_sound()

            elif S10[3] != 'Yes, coal engines pollute \nthe environment more than electric engines':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q11:
        S11 = ['Statutory Body', 'Constitutional Body', 'Non Governmental Organization', 'Advisory Body']
        random.shuffle(S11)
        op1.configure(text=S11[0])
        op2.configure(text=S11[1])
        op3.configure(text=S11[2])
        op4.configure(text=S11[3])

        def key0(event):
            if S11[0] == 'Statutory Body':
                op1.configure(bg='green')
                Q_sound()

            elif S11[0] != 'Statutory Body':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S11[1] == 'Statutory Body':
                op2.configure(bg='green')
                Q_sound()

            elif S11[0] != 'Statutory Body':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S11[2] == 'Statutory Body':
                op3.configure(bg='green')
                Q_sound()

            elif S11[0] != 'Statutory Body':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S11[3] == 'Statutory Body':
                op4.configure(bg='green')
                Q_sound()

            elif S11[0] != 'Statutory Body':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q12:
        S12 = ['Shanti Ghat', 'Shakti Sthal', 'Shanti Van', 'Shanti Sthal']
        random.shuffle(S12)
        op1.configure(text=S12[0])
        op2.configure(text=S12[1])
        op3.configure(text=S12[2])
        op4.configure(text=S12[3])

        def key0(event):
            if S12[0] == 'Shakti Sthal':
                op1.configure(bg='green')
                Q_sound()

            elif S12[0] != 'Shakti Sthal':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S12[1] == 'Shakti Sthal':
                op2.configure(bg='green')
                Q_sound()

            elif S12[1] != 'Shakti Sthal':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S12[2] == 'Shakti Sthal':
                op3.configure(bg='green')
                Q_sound()

            elif S12[2] != 'Shakti Sthal':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S12[3] == 'Shakti Sthal':
                op4.configure(bg='green')
                Q_sound()

            elif S12[3] != 'Shakti Sthal':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q13:
        S13 = [' Punjab', 'Haryana', 'Uttar Pradesh', 'Madhya Pradesh']
        random.shuffle(S13)
        op1.configure(text=S13[0])
        op2.configure(text=S13[1])
        op3.configure(text=S13[2])
        op4.configure(text=S13[3])

        def key0(event):
            if S13[0] == 'Haryana':
                op1.configure(bg='green')
                Q_sound()

            elif S13[0] != 'Haryana':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S13[1] == 'Haryana':
                op2.configure(bg='green')
                Q_sound()

            elif S13[1] != 'Haryana':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S13[2] == 'Haryana':
                op3.configure(bg='green')
                Q_sound()

            elif S13[2] != 'Haryana':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S13[3] == 'Haryana':
                op4.configure(bg='green')
                Q_sound()

            elif S13[3] != 'Haryana':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q14:
        S14 = ['Albert Einstein', 'H. G. Khorana', 'Linus Pauling', 'Paul Berg']
        random.shuffle(S14)
        op1.configure(text=S14[0])
        op2.configure(text=S14[1])
        op3.configure(text=S14[2])
        op4.configure(text=S14[3])

        def key0(event):
            if S14[0] == 'Linus Pauling':
                op1.configure(bg='green')
                Q_sound()

            elif S14[0] != 'Linus Pauling':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S14[1] == 'Linus Pauling':
                op2.configure(bg='green')
                Q_sound()

            elif S14[1] != 'Linus Pauling':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S14[2] == 'Linus Pauling':
                op3.configure(bg='green')
                Q_sound()

            elif S14[2] != 'Linus Pauling':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S14[3] == 'Linus Pauling':
                op4.configure(bg='green')
                Q_sound()

            elif S14[3] != 'Linus Pauling':
                op4.configure(bg='red')
                Q1_sound()

    elif str(Q_random) == q15:
        S15 = ['68.20', '44.94', '78.20', '33']
        random.shuffle(S15)
        op1.configure(text=S15[0])
        op2.configure(text=S15[1])
        op3.configure(text=S15[2])
        op4.configure(text=S15[3])

        def key0(event):
            if S15[0] == '33':
                op1.configure(bg='green')
                Q_sound()

            elif S15[0] != '33':
                op1.configure(bg='red')
                Q1_sound()

        def key1(event):
            if S15[1] == '33':
                op2.configure(bg='green')
                Q_sound()

            elif S15[1] != '33':
                op2.configure(bg='red')
                Q1_sound()

        def key2(event):
            if S15[2] == '33':
                op3.configure(bg='green')
                Q_sound()

            elif S15[2] != '33':
                op3.configure(bg='red')
                Q1_sound()

        def key3(event):
            if S15[3] == '33':
                op4.configure(bg='green')
                Q_sound()

            elif S15[3] != '33':
                op4.configure(bg='red')
                Q1_sound()

    op1.bind('<Button-1>', key0)
    op2.bind('<Button-1>', key1)
    op3.bind('<Button-1>', key2)
    op4.bind('<Button-1>', key3)
    j = QA.index(str(Q_random))
    QA.pop(j)
    if c == 1:
        l1.configure(bg='yellow')
        L1.configure(bg='yellow')
        win()
    elif c == 2:
        l2.configure(bg='yellow')
        L2.configure(bg='yellow')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 3:
        l3.configure(bg='yellow')
        L3.configure(bg='yellow')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 4:
        l4.configure(bg='yellow')
        L4.configure(bg='yellow')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 5:
        l5.configure(bg='yellow')
        L5.configure(bg='yellow')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    if c == 6:
        l6.configure(bg='yellow')
        L6.configure(bg='yellow')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 7:
        l7.configure(bg='yellow')
        L7.configure(bg='yellow')
        l6.configure(bg='black')
        L6.configure(bg='black')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 8:
        l8.configure(bg='yellow')
        L8.configure(bg='yellow')
        l7.configure(bg='black')
        L7.configure(bg='black')
        l6.configure(bg='black')
        L6.configure(bg='black')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 9:
        l9.configure(bg='yellow')
        L9.configure(bg='yellow')
        l8.configure(bg='black')
        L8.configure(bg='black')
        l7.configure(bg='black')
        L7.configure(bg='black')
        l6.configure(bg='black')
        L6.configure(bg='black')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 10:
        l10.configure(bg='yellow')
        L10.configure(bg='yellow')
        l9.configure(bg='black')
        L9.configure(bg='black')
        l8.configure(bg='black')
        L8.configure(bg='black')
        l7.configure(bg='black')
        L7.configure(bg='black')
        l6.configure(bg='black')
        L6.configure(bg='black')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 11:
        l11.configure(bg='yellow')
        L11.configure(bg='yellow')
        l10.configure(bg='black')
        L10.configure(bg='black')
        l9.configure(bg='black')
        L9.configure(bg='black')
        l8.configure(bg='black')
        L8.configure(bg='black')
        l7.configure(bg='black')
        L7.configure(bg='black')
        l6.configure(bg='black')
        L6.configure(bg='black')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 12:
        l12.configure(bg='yellow')
        L12.configure(bg='yellow')
        l11.configure(bg='black')
        L11.configure(bg='black')
        l10.configure(bg='black')
        L10.configure(bg='black')
        l9.configure(bg='black')
        L9.configure(bg='black')
        l8.configure(bg='black')
        L8.configure(bg='black')
        l7.configure(bg='black')
        L7.configure(bg='black')
        l6.configure(bg='black')
        L6.configure(bg='black')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 13:
        l13.configure(bg='yellow')
        L13.configure(bg='yellow')
        l12.configure(bg='black')
        L12.configure(bg='black')
        l11.configure(bg='black')
        L11.configure(bg='black')
        l10.configure(bg='black')
        L10.configure(bg='black')
        l9.configure(bg='black')
        L9.configure(bg='black')
        l8.configure(bg='black')
        L8.configure(bg='black')
        l7.configure(bg='black')
        L7.configure(bg='black')
        l6.configure(bg='black')
        L6.configure(bg='black')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 14:
        l14.configure(bg='yellow')
        L14.configure(bg='yellow')
        l13.configure(bg='black')
        L13.configure(bg='black')
        l12.configure(bg='black')
        L12.configure(bg='black')
        l11.configure(bg='black')
        L11.configure(bg='black')
        l10.configure(bg='black')
        L10.configure(bg='black')
        l9.configure(bg='black')
        L9.configure(bg='black')
        l8.configure(bg='black')
        L8.configure(bg='black')
        l7.configure(bg='black')
        L7.configure(bg='black')
        l6.configure(bg='black')
        L6.configure(bg='black')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    elif c == 15:
        l15.configure(bg='yellow')
        L15.configure(bg='yellow')
        l14.configure(bg='black')
        L14.configure(bg='black')
        l13.configure(bg='black')
        L13.configure(bg='black')
        l12.configure(bg='black')
        L12.configure(bg='black')
        l11.configure(bg='black')
        L11.configure(bg='black')
        l10.configure(bg='black')
        L10.configure(bg='black')
        l9.configure(bg='black')
        L9.configure(bg='black')
        l8.configure(bg='black')
        L8.configure(bg='black')
        l7.configure(bg='black')
        L7.configure(bg='black')
        l6.configure(bg='black')
        L6.configure(bg='black')
        l5.configure(bg='black')
        L5.configure(bg='black')
        l4.configure(bg='black')
        L4.configure(bg='black')
        l3.configure(bg='black')
        L3.configure(bg='black')
        l2.configure(bg='black')
        L2.configure(bg='black')
        l1.configure(bg='black')
        L1.configure(bg='black')
        win()
    time1()


def pic():
    global op1, op2, op3, op4
    global Q_random
    global c
    global t1, b1
    global l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15
    global L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15
    Q_random = QA[0]
    canvas = Canvas(root, bg='black', width=1920, height=1080)
    canvas.create_image(765, 400, image=temp)
    canvas.place(x=0, y=0)
    t1 = Label(canvas, fg='white', bg='blue', font=("Times New Roman", 18), width=6, height=0)
    t1.place(x=638, y=438)
    # ----------------------------------------------------------------------------------------------------------------------#
    l1 = Label(canvas, text='1', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l1.place(x=1200, y=430)
    l2 = Label(canvas, text='2', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l2.place(x=1200, y=405)
    l3 = Label(canvas, text='3', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l3.place(x=1200, y=380)
    l4 = Label(canvas, text='4', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l4.place(x=1200, y=355)
    l5 = Label(canvas, text='5', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l5.place(x=1200, y=335)
    l6 = Label(canvas, text='6', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l6.place(x=1200, y=310)
    l7 = Label(canvas, text='7', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l7.place(x=1200, y=285)
    l8 = Label(canvas, text='8', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l8.place(x=1200, y=260)
    l9 = Label(canvas, text='9', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l9.place(x=1200, y=235)
    l10 = Label(canvas, text='10', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l10.place(x=1200, y=210)
    l11 = Label(canvas, text='11', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l11.place(x=1200, y=185)
    l12 = Label(canvas, text='12', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l12.place(x=1200, y=160)
    l13 = Label(canvas, text='13', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l13.place(x=1200, y=135)
    l14 = Label(canvas, text='14', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l14.place(x=1200, y=110)
    l15 = Label(canvas, text='15', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    l15.place(x=1200, y=85)

    L1 = Label(canvas, text='1,000', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    L1.place(x=1350, y=430)
    L2 = Label(canvas, text='2,000', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    L2.place(x=1350, y=405)
    L3 = Label(canvas, text='3,000', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    L3.place(x=1350, y=380)
    L4 = Label(canvas, text='5,000', fg='orange', bg='black', font=("Times New Roman", 12), width=6, height=0)
    L4.place(x=1350, y=355)
    L5 = Label(canvas, text='10,000', fg='white', bg='black', font=("Times New Roman", 12), width=6, height=0)
    L5.place(x=1350, y=335)
    L6 = Label(canvas, text='20,000', fg='orange', bg='black', font=("Times New Roman", 12), width=7, height=0)
    L6.place(x=1350, y=310)
    L7 = Label(canvas, text='40,000', fg='orange', bg='black', font=("Times New Roman", 12), width=7, height=0)
    L7.place(x=1350, y=285)
    L8 = Label(canvas, text='80,000', fg='orange', bg='black', font=("Times New Roman", 12), width=7, height=0)
    L8.place(x=1350, y=260)
    L9 = Label(canvas, text='1,60,000', fg='orange', bg='black', font=("Times New Roman", 12), width=7, height=0)
    L9.place(x=1350, y=235)
    L10 = Label(canvas, text='3,20,000', fg='white', bg='black', font=("Times New Roman", 12), width=7, height=0)
    L10.place(x=1350, y=210)
    L11 = Label(canvas, text='6,25,000', fg='orange', bg='black', font=("Times New Roman", 12), width=8, height=0)
    L11.place(x=1350, y=185)
    L12 = Label(canvas, text='12,50,000', fg='orange', bg='black', font=("Times New Roman", 12), width=9, height=0)
    L12.place(x=1350, y=160)
    L13 = Label(canvas, text='25,00,000', fg='orange', bg='black', font=("Times New Roman", 12), width=9, height=0)
    L13.place(x=1350, y=135)
    L14 = Label(canvas, text='50,00,000', fg='white', bg='black', font=("Times New Roman", 12), width=9, height=0)
    L14.place(x=1350, y=110)
    L15 = Label(canvas, text='Rs 1 Crore', fg='white', bg='black', font=("Times New Roman", 12), width=9, height=0)
    L15.place(x=1350, y=85)
    # ----------------------------------------------------------------------------------------------------------
    Q1 = Label(canvas, text=QA[0], fg='white', bg='black', font=("Times New Roman", 20), width=93, height=3)
    Q1.place(x=69, y=487)
    op1 = Label(canvas, fg='white', bg='black', font=("Times New Roman", 18), width=40, height=2)
    op1.place(x=125, y=630)
    op2 = Label(canvas, fg='white', bg='black', font=("Times New Roman", 18), width=40, height=2)
    op2.place(x=925, y=630)
    op3 = Label(canvas, fg='white', bg='black', font=("Times New Roman", 18), width=40, height=2)
    op3.place(x=125, y=730)
    op4 = Label(canvas, fg='white', bg='black', font=("Times New Roman", 18), width=40, height=2)
    op4.place(x=925, y=730)
    # ----------------------------------------------------------------------------------------------------------
    b1 = Button(canvas, image=life, height=0,)
    b1.place(x=1405, y=0)
    c = c + 1
    print(c)
    work()


def screen_bg():
    K1.configure(image=gif2)
    root.update()
    root.after(5000, None)
    K1.configure(image=gif1)
    root.update()
    root.after(5000, K1.pack_forget())
    pic()

screen_bg()

root.mainloop()
