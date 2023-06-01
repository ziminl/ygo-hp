import pyautogui

from python_imagesearch.imagesearch import imagesearch

import keyboard

import time

#------------------------------------------------------
#a   =
#b   =
#(c )=

#게임시작전
duel = "duel.png" #듀얼     b

first = "first.png" #선공   a
second = "second.png" #후공 b

#게임시작후
active = "active.png"#효과발동 원형       a
active2 = "active2.png"#효과발동 막대기형 a
select = select.png #선택                a
select2 = select2.png #결정 원형         b
summon1 = "summon1.png"#일반소환 원형    a
set1 = "set.png" #세트 원형               b
summon2 #특수소환 원형                   a

#cancel 원형                             b
#확인 막대기


#앞면 공격표시 원형


cancel = "cancel.png"#취소

#항복
#설정키 - 항복 

#게임끝나고
return1 = "return.png" #돌아가기
ok = "ok.png"#확인

#------------------------------------------------------
def function():
    pos = imagesearch(w_butten)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        print("clicked duel")
        pyautogui.click(x=pos[0], y=pos[1])
    else:
        print("image not found")

while True:  # making a loop
        if keyboard.is_pressed('a'):  #듀얼
            print('You Pressed a Key!')
            w_butten = duel
            function()
        if keyboard.is_pressed('s'):  #확인 
            print('You Pressed s Key!')    
            w_butten = ok
            function()


