import pyautogui, time
#Size(width=1920, height=1080)
#print(pyautogui.position())    #just helpful to know this command
pyautogui.FAILSAFE = True

def clickContinue(x, y):
    print('clicking continue ', x, ' times, with a ', y, ' break between them')
    for i in range(x):
        pyautogui.click(1488, 992) #clicks continue
        time.sleep(y) #pauses
        
def rest(x):
    time.sleep(x)

pyautogui.click('good_morning.png')   #clicks to start Good Morning! story
print('clicked Good Morning story')
clickContinue(10, 1)

#q1 - what does mon cheri mean
rest(1)
print('looking for darling')
darling = pyautogui.locateOnScreen('darling.png')
pyautogui.moveTo(darling)
pyautogui.move(-60, 0)
pyautogui.click()
print('clicked darling')
clickContinue(7, 1)

#q2 - select the missing phrase
rest(1)
print('looking for exam danglais')
pyautogui.click('english_exam.png')
print('clicked exam danglais')
clickContinue(11, 1)

#q3 - click on the option meaning tired
rest(1)
print('looking for fatiguee')
pyautogui.click('tired.png')
print('clicked fatiguee')
clickContinue(11, 1)

#q4 - What did Marion do
rest(1)
print('looking for sugar')
sugar = pyautogui.locateOnScreen('sugar.png')
pyautogui.moveTo(sugar)
pyautogui.move(-60, 0)
pyautogui.click()
print('clicked sugar')
clickContinue(5, 1)

#q5 - What does quoi mean
rest(1)
print('looking for what')
what = pyautogui.locateOnScreen('what.png')
pyautogui.moveTo(what)
pyautogui.move(-60, 0)
pyautogui.click()
print('clicked what')
clickContinue(6, 1)

#q6 - Marion was so tired that she
time.sleep(1)
print('looking for salt')
salt = pyautogui.locateOnScreen('salt.png')
pyautogui.moveTo(salt)
pyautogui.move(-60, 0)
pyautogui.click()
print('clicked salt')
clickContinue(1, 1)

print('looking for jai/have')
option = pyautogui.locateOnScreen('jai.png')
if option is not None:
    pyautogui.click('jai.png')
    pyautogui.click('have.png')

print('looking for coffee/cafe')
option = pyautogui.locateOnScreen('coffee.png')
if option is not None:
    pyautogui.click('coffee.png')
    pyautogui.click('cafe.png')

print('looking for pardon/sorry')
option = pyautogui.locateOnScreen('pardon.png')
if option is not None:
    pyautogui.click('pardon.png')
    pyautogui.click('sorry.png')

print('looking for lot/beaucoup')
option = pyautogui.locateOnScreen('lot.png')
if option is not None:
    pyautogui.click('lot.png')
    pyautogui.click('beaucoup.png')

print('looking for am/suis')
option = pyautogui.locateOnScreen('am.png')
if option is not None:
    pyautogui.click('am.png')
    pyautogui.click('suis.png')

print('looking for drink/boit')
option = pyautogui.locateOnScreen('drinks.png')
if option is not None:
    pyautogui.click('drinks.png')
    pyautogui.click('boit.png')

print('looking for here/ici')
option = pyautogui.locateOnScreen('here.png')
if option is not None:
    pyautogui.click('here.png')
    pyautogui.click('ici.png')

print('looking for trav/work')
option = pyautogui.locateOnScreen('trav.png')
if option is not None:
    pyautogui.click('trav.png')
    pyautogui.click('work.png')

print('looking for hi/salut')
option = pyautogui.locateOnScreen('hi.png')
if option is not None:
    pyautogui.click('hi.png')
    pyautogui.click('salut.png')

print('looking for his/sa')
option = pyautogui.locateOnScreen('his.png')
if option is not None:
    pyautogui.click('his.png')
    pyautogui.click('sa.png')

print('looking for she/elle')
option = pyautogui.locateOnScreen('she.png')
if option is not None:
    pyautogui.click('she.png')
    pyautogui.click('elle.png')

print('looking for cheri/darling')
option = pyautogui.locateOnScreen('cheri.png')
if option is not None:
    pyautogui.click('cheri.png')
    pyautogui.click('darling2.png')

print('looking for sucre/sugar')
option = pyautogui.locateOnScreen('du_sucre.png')
if option is not None:
    pyautogui.click('du_sucre.png')
    pyautogui.click('some_sugar.png')

print('looking for yuck/beurk')
option = pyautogui.locateOnScreen('beurk.png')
if option is not None:
    pyautogui.click('beurk.png')
    pyautogui.click('yuck.png')

print('looking for il/it')
option = pyautogui.locateOnScreen('il.png')
if option is not None:
    pyautogui.click('il.png')
    pyautogui.click('it.png')

print('looking for the/la')
option = pyautogui.locateOnScreen('the.png')
if option is not None:
    pyautogui.click('the.png')
    pyautogui.click('la.png')

print('looking for salt/sel')
option = pyautogui.locateOnScreen('salt2.png')
if option is not None:
    pyautogui.click('salt2.png')
    pyautogui.click('du_sel.png')

clickContinue(5, 2)

#re runs the program lol
print('re-running program')
pyautogui.click(200, 200) #clicks the python file
pyautogui.press('f5')
