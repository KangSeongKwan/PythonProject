from turtle import *
from tkinter import *
from random import randint
from playsound import *

money = 0
total = 10000
game_count = 0
boostcount = 0
loan_date  = 0
loan_money = 0

#대출 거북이
LT = Turtle()
LT.hideturtle()
LT.penup()
LT.goto(0,-250)
    

t0 = Turtle()
t0.shape("turtle")
t0.hideturtle()
t0.color("orange")
t0.speed(0)
t0.penup()
t0.goto(-200,200)
flag = True


    
# 경기장 세팅

for step in range(20):
    t0.rt(90)
    t0.fd(10)
    t0.pendown()
    t0.fd(130)
    t0.penup()
    t0.bk(140)
    t0.lt(90)
    t0.fd(25)

t0.goto(0,-55)
t0.pendown()
t0.fd(50)
t0.lt(90)
t0.fd(20)
t0.lt(90)
t0.fd(100)
t0.lt(90)
t0.fd(20)
t0.lt(90)
t0.fd(50)

# 경기 시작
def startrace():
    global game_count
    game_count+=1
    global total
    global boostcount
    global flag
    global LT

    #게임 횟수 표시 거북이
    GC = Turtle()
    GC.hideturtle()
    GC.penup()
    GC.goto(0,-300)
    GC.write("게임 횟수 :" + str(game_count),font = ('맑은 고딕',18,'bold'),align = "center")
    
    #금액 표시 거북이
    TC = Turtle()
    TC.hideturtle()
    TC.penup()
    TC.goto(0,-200)
    TC.write("총액:" + str(total),font = ('맑은 고딕',18,'bold'),align = "center")
    
    a = Turtle()
    screen=Screen()
    screen.addshape("mouse.gif")
    a.shape("mouse.gif")
    a.penup()
    a.goto(0, 250)

    # 경주할 거북이 세팅
        
    t1=Turtle()
    t1.color('red')
    t1.shape('turtle')
    t1.penup()
    t1.goto(-220,170)
    t1.pendown()
    t1.write("1  ", True, align= "right",font = ('맑은 고딕',18,'bold'))
    st1 = t1.xcor()

    t2=Turtle()
    t2.color('yellow')
    t2.shape('turtle')
    t2.penup()
    t2.goto(-220,140)
    t2.pendown()
    t2.write("2  ", True, align= "right",font = ('맑은 고딕',18,'bold'))
    st2 = t2.xcor()
    
    t3=Turtle()
    t3.color('blue')
    t3.shape('turtle')
    t3.penup()
    t3.goto(-220,110)
    t3.pendown()
    t3.write("3  ", True, align= "right",font = ('맑은 고딕',18,'bold'))
    st3 = t3.xcor()

    t4=Turtle()
    t4.color('green')
    t4.shape('turtle')
    t4.penup()
    t4.goto(-220, 80)
    t4.pendown()
    t4.write("4  ", True, align= "right",font = ('맑은 고딕',18,'bold'))
    st4 = t4.xcor()

    #도박 중계사 거북이 추가
    WL = Turtle()
    WL.color('purple')
    WL.hideturtle()
    WL.shape('turtle')
    WL.penup()
    WL.goto(-320, -100)
    WL.pendown()

    ad1=0 
    ad2=0
    ad3=0
    ad4=0
    
    #   거북이 경주에 사행성을 추가
    n = textinput("선택", "응원할 거북이를 선택해주세요")
    while(1):
        if n == '1' or n == '2' or n == '3' or n == '4':
            break
        else:
           n = textinput("선택", "1, 2, 3, 4번중 다시 선택해주세요")
            
    money = textinput("투입","얼마를 거시겠어요?")
    while(1):
        if total < int(money):
            money = textinput("투입", "총액보다 크지 않게 다시 입력하세요")
        else:
            break
    a.write(n+"번 이겨라",True, align= "right",font = ('맑은 고딕',18,'bold'))

    # 부스터 기능
    def booster():
        global total
        total -= int(money)/2
        TC.clear()
        
        if n == '1':
            t1.fd(10)
        elif n == '2':
            t2.fd(10)
        elif n == '3':
            t3.fd(10)
        elif n == '4':
            t4.fd(10)

    #돈 대출 함수
    def loan():
        global flag
        global loan_money
        global loan_date
        global LT
        while(flag):
            global total
            loan_money = total*2.1
            total *= 2
            loan_date  = game_count+2
            LT.write("돈을 대출 하셨습니다."+"게임 횟수:"+str(loan_date)+"회 때"+ str(loan_money)+ "만큼 상환합니다.",
                 True, align= "center",font = ('맑은 고딕',18,'bold'))
            flag = False
        
        
    #부스터, 대출 버튼 추
    root = Tk()
    b1 = Button(root, text = "부스터",command = booster)
    b2 = Button(root, text = "대출",command = loan)
    b1.pack(side=LEFT)
    b2.pack(side=RIGHT)

    #   경기 진행
    while(1):
        TC.undo()
        TC.write("총액:" + str(total),font = ('맑은 고딕',18,'bold'),align = "center")
        r1=randint(1,5)
        r2=randint(1,5)
        r3=randint(1,5)
        r4=randint(1,5)
        t1.fd(r1)
        t2.fd(r2)
        t3.fd(r3)
        t4.fd(r4)
        ad1 = t1.xcor()
        ad2 = t2.xcor()
        ad3 = t3.xcor()
        ad4 = t4.xcor()
        #거북이 임의로 위치 초기화
        death = randint(1,100)
        if(death == 44):
            num = randint(1,4)
            if(num == 1):
                t1.clear()
                t1.penup()
                t1.goto(-220,170)
                t1.pendown()
                t1.write("1  ", True, align= "right",font = ('맑은 고딕',18,'bold'))
            elif(num == 2):
                t2.clear()
                t2.penup()
                t2.goto(-220,140)
                t2.pendown()
                t2.write("2  ", True, align= "right",font = ('맑은 고딕',18,'bold'))
            elif(num == 3):
                t3.clear()
                t3.penup()
                t3.goto(-220,110)
                t3.pendown()
                t3.write("3  ", True, align= "right",font = ('맑은 고딕',18,'bold'))
            elif(num == 4):
                t4.clear()
                t4.penup()
                t4.goto(-220,80)
                t4.pendown()
                t4.write("4  ", True, align= "right",font = ('맑은 고딕',18,'bold'))
        screen.addshape("reward.gif")

        
        # 경기 후 결과
        if (ad1-st1)>=500:
            rank = [ad1,ad2,ad3,ad4]
            rank.sort(reverse=True)
            t1.write(rank.index(ad1)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t2.write(rank.index(ad2)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t3.write(rank.index(ad3)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t4.write(rank.index(ad4)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            
            t1.penup()
            t1.goto(0,10)
            t1.shape("reward.gif")
            t1.write("      1번 거북이 우승!")
            if n == '1':
                incmoney = int(money) * 4
                WL.write("당신은 " + str(incmoney) + " 원 만큼 이익을 얻으셨습니다!")
                playsound("Happy.mp3")
                TC.undo()
                total = total+incmoney
                TC.write("총액:"+str(total),font = ('맑은 고딕',18,'bold'),align = "center")
            else:
                losmoney = int(money)
                WL.write("당신은 " + str(losmoney) + " 원 만큼 잃으셨습니다.")
                playsound("fail.mp3")
                TC.undo()
                total = total-losmoney
                TC.write("총액:"+str(total),font = ('맑은 고딕',18,'bold'),align = "center")
            break

        elif (ad2-st2)>=500:
            rank = [ad1,ad2,ad3,ad4]
            rank.sort(reverse=True)
            t1.write(rank.index(ad1)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t2.write(rank.index(ad2)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t3.write(rank.index(ad3)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t4.write(rank.index(ad4)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))

            t2.penup()
            t2.goto(0,10)
            t2.shape("reward.gif")
            t2.write("      2번 거북이 우승!")
            if n == '2':
                incmoney = int(money) * 4
                WL.write("당신은 " + str(incmoney) + " 원 만큼 이익을 얻으셨습니다!")
                playsound("Happy.mp3")
                TC.undo()
                total = total+incmoney
                TC.write("총액:"+str(total),font = ('맑은 고딕',18,'bold'),align = "center")
            else:
                losmoney = int(money)
                WL.write("당신은 " + str(losmoney) + " 원 만큼 잃으셨습니다.")
                playsound("fail.mp3")
                TC.undo()
                total = total-losmoney
                TC.write("총액:"+str(total),font = ('맑은 고딕',18,'bold'),align = "center")
            break
        
        elif (ad3-st3)>=500:
            rank = [ad1,ad2,ad3,ad4]
            rank.sort(reverse=True)
            t1.write(rank.index(ad1)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t2.write(rank.index(ad2)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t3.write(rank.index(ad3)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t4.write(rank.index(ad4)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            
            t3.penup()
            t3.goto(0,10)
            t3.shape("reward.gif")
            t3.write("      3번 거북이 우승!")
            if n == '3':
                incmoney = int(money) * 4
                WL.write("당신은 " + str(incmoney) + " 원 만큼 이익을 얻으셨습니다!")
                playsound("Happy.mp3")
                TC.undo()
                total = total+incmoney
                TC.write("총액:"+str(total),font = ('맑은 고딕',18,'bold'),align = "center")
            else:
                losmoney = int(money)
                WL.write("당신은 " + str(losmoney) + " 원 만큼 잃으셨습니다.")
                playsound("fail.mp3")
                TC.undo()
                total = total-losmoney
                TC.write("총액:"+str(total),font = ('맑은 고딕',18,'bold'),align = "center")
            break
        
        elif (ad4-st4)>=500:
            rank = [ad1,ad2,ad3,ad4]
            rank.sort(reverse=True)
            t1.write(rank.index(ad1)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t2.write(rank.index(ad2)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t3.write(rank.index(ad3)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            t4.write(rank.index(ad4)+1, True, align= "right",font = ('맑은 고딕',18,'bold'))
            
            t4.penup()
            t4.goto(0,10)
            t4.shape("reward.gif")
            t4.write("      4번 거북이 우승!")
            if n == '4':
                incmoney = int(money) * 4
                WL.write("당신은 " + str(incmoney) + " 원 만큼 이익을 얻으셨습니다!")
                playsound("Happy.mp3")
                TC.undo()
                total = total + incmoney
                TC.write("총액:"+str(total),font = ('맑은 고딕',18,'bold'),align = "center")
            else:
                losmoney = int(money)
                WL.write("당신은 " + str(losmoney) + " 원 만큼 잃으셨습니다.")
                playsound("fail.mp3")
                TC.undo()
                total = total - losmoney
                TC.write("총액:"+str(total),font = ('맑은 고딕',18,'bold'),align = "center")
            break
    root.destroy()

    #대출 후 돈 갚는 경우
    if loan_date == game_count:
        total -= loan_money
        TC.undo()
        TC.write("총액:"+str(total),font = ('맑은 고딕',18,'bold'),align = "center")
        LT.undo()
        flag = True

    #보유 금액 탕진 시
    if total <= 0:
        TC.undo()
        TC.write("돈을 탕진했습니다",font = ('맑은 고딕',18,'bold'),align = "center")
        exit(0)

    #게임 재시작
    while(1):
        b = textinput('거북이 경주를 계속 하시겠습니까?','예,아니오')
        if b == '예':
        
            t1.shape('turtle')
            t2.shape('turtle')
            t3.shape('turtle')
            t4.shape('turtle')

            TC.hideturtle()
            t1.hideturtle()
            t2.hideturtle()
            t3.hideturtle()
            t4.hideturtle()
            a.hideturtle()
            WL.hideturtle()
        
            TC.clear()
            t1.clear()
            t2.clear()
            t3.clear()
            t4.clear()
            a.clear()
            WL.clear()
            GC.clear()
        
            startrace()
        elif b == '아니오':
            exit(0)
    

startrace()



