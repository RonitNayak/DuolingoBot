import pyautogui, time
#Size(width=1920, height=1080)
#print(pyautogui.position())    #just helpful to know this command
pyautogui.FAILSAFE = True

def clickContinue(x, y):
    for i in range(x): 
        pyautogui.click(1488, 992) #clicks continue
        time.sleep(y) #pauses
        
def rest(x):
    time.sleep(x)

pyautogui.click('good_morning.png')   #clicks to start Good Morning! story
clickContinue(10, 1)

#q1 - what does mon cheri mean
rest(1)
darling = pyautogui.locateOnScreen('darling.png')
pyautogui.moveTo(darling)
pyautogui.move(-60, 0)
pyautogui.click()
clickContinue(7, 1)

#q2 - select the missing phrase
rest(1)
pyautogui.click('english_exam.png')
clickContinue(11, 1)

#q3 - click on the option meaning tired
rest(1)
pyautogui.click('tired.png')
clickContinue(11, 1)

#q4 - What did Marion do
rest(1)
sugar = pyautogui.locateOnScreen('sugar.png')
pyautogui.moveTo(sugar)
pyautogui.move(-60, 0)
pyautogui.click()
clickContinue(5, 1)

#q5 - What does quoi mean
rest(1)
what = pyautogui.locateOnScreen('what.png')
pyautogui.moveTo(what)
pyautogui.move(-60, 0)
pyautogui.click()
clickContinue(6, 1)

#q6 - Marion was so tired that she
time.sleep(1)
salt = pyautogui.locateOnScreen('salt.png')
pyautogui.moveTo(salt)
pyautogui.move(-60, 0)
pyautogui.click()
clickContinue(1, 1)

option = pyautogui.locateOnScreen('jai.png')
if option is not None:
    pyautogui.click('jai.png')
    pyautogui.click('have.png')

option = pyautogui.locateOnScreen('coffee.png')
if option is not None:
    pyautogui.click('coffee.png')
    pyautogui.click('cafe.png')

option = pyautogui.locateOnScreen('pardon.png')
if option is not None:
    pyautogui.click('pardon.png')
    pyautogui.click('sorry.png')

option = pyautogui.locateOnScreen('lot.png')
if option is not None:
    pyautogui.click('lot.png')
    pyautogui.click('beaucoup.png')

option = pyautogui.locateOnScreen('am.png')
if option is not None:
    pyautogui.click('am.png')
    pyautogui.click('suis.png')

option = pyautogui.locateOnScreen('drinks.png')
if option is not None:
    pyautogui.click('drinks.png')
    pyautogui.click('boit.png')

option = pyautogui.locateOnScreen('here.png')
if option is not None:
    pyautogui.click('here.png')
    pyautogui.click('ici.png')

option = pyautogui.locateOnScreen('trav.png')
if option is not None:
    pyautogui.click('trav.png')
    pyautogui.click('work.png')

option = pyautogui.locateOnScreen('hi.png')
if option is not None:
    pyautogui.click('hi.png')
    pyautogui.click('salut.png')

option = pyautogui.locateOnScreen('his.png')
if option is not None:
    pyautogui.click('his.png')
    pyautogui.click('sa.png')

clickContinue(10, 1)

#re runs the program lol
pyautogui.click(200, 200) #clicks the python file
pyautogui.press('f5')
