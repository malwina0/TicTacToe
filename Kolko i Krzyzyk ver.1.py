#!/usr/bin/env python
# coding: utf-8

# In[19]:


def wpisanie(pozycja_nr, zajety):
    """Proces dopasowywania wybranego znaku do miejsca na planszy pamiętając o sprawdzeniu czy dane miejsce nie jest już zajęte"""
    a = input('Enter position: ')
    b = input('Enter o or x: ')
    if a == '1' and zajety[0] == False:
        pozycja_nr[0] = b
        zajety[0] = True
        return pozycja_nr, zajety
    elif a =='2' and zajety[1] == False:
        pozycja_nr[1] = b
        zajety[1] = True
        return pozycja_nr, zajety
    elif a == '3' and zajety[2] == False:
        pozycja_nr[2] = b
        zajety[2] = True
        return pozycja_nr, zajety
    elif a == '4' and zajety[3] == False:
        pozycja_nr[3] = b
        zajety[3] = True
        return pozycja_nr, zajety
    elif a =='5' and zajety[4] == False:
        pozycja_nr[4] = b
        zajety[4] = True
        return pozycja_nr, zajety
    elif a == '6' and zajety[5] == False:
        pozycja_nr[5] = b
        zajety[5] = True
        return pozycja_nr, zajety
    elif a == '7' and zajety[6] == False:
        pozycja_nr[6] = b
        zajety[6] = True
        return pozycja_nr, zajety
    elif a == '8' and zajety[7] == False:
        pozycja_nr[7] = b
        zajety[7] = True
        return pozycja_nr, zajety
    elif a == '9' and zajety[8] == False:
        pozycja_nr[8] = b
        zajety[8] = True
        return pozycja_nr, zajety
    else:
        print('Nie da rady byczq')

def plansza():
    """Stworzenie planszy do gry"""
    print('|' + pozycja[0] + '|' + pozycja[1] + '|' + pozycja[2] +'|')
    print('-------')
    print('|' + pozycja[3] + '|' + pozycja[4] + '|' + pozycja[5] +'|')
    print('-------')
    print('|' + pozycja[6] + '|' + pozycja[7] + '|' + pozycja[8] +'|')
    print('-------')
    
def check_win(win, gdzie_wartosci):
    """Sprawdzenie wygranej"""
    for i in win:
        if all(j in gdzie_wartosci for j in i) == True:
            print('Wygranko')
            plansza()
            raise SystemExit(0)
    plansza()

def indeksy_o(h,f):
    """Pobranie indeksow, na ktorych miejscach stoja 'o'"""
    for index in range(len(h)):
        value=h[index]
        if value == 'o':
            f.append(index)

def indeksy_x(h,f):
    """Pobranie, na ktorych miejschach stoja 'x'"""
    for index in range(len(h)):
        value=h[index]
        if value == 'x':
            f.append(index)

exit = 0
pas=[]
pozycja = ['1','2','3','4','5','6','7','8','9']
stage = 0
wygransko = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
zajetosc = [False, False, False, False, False, False, False, False, False]

while stage <= 4:
    stage+=1
    plansza()
    wpisanie(pozycja,zajetosc)
indeksy_o(pozycja, pas)
check_win(wygransko, pas)
pas.clear()
stage+=1
while stage <= 9:
    stage+=1
    wpisanie(pozycja, zajetosc)
    if stage % 2 == 0:
        indeksy_o(pozycja, pas)
    elif stage % 2 == 1:
        indeksy_x(pozycja, pas)
    check_win(wygransko, pas)
    pas.clear()
print('REMIS')
raise SystemExit(0)

