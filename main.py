import pyautogui, time

print("Bot vai iniciar, pressione ok para continuar")
try:
    while True:
        time.sleep(2)

        ##Ligar auto do Archer
        positionAuto = pyautogui.locateOnScreen('auto.png', grayscale=True, confidence=0.8)
        if positionAuto:
            positionCenterAuto = pyautogui.center(positionAuto)
            pyautogui.click(positionCenterAuto.x, positionCenterAuto.y)

        ##Bonus do Archer
        positionBonus = pyautogui.locateOnScreen('bonus.png', grayscale=True, confidence=0.8)
        if positionBonus:
            positionCenterBonus = pyautogui.center(positionBonus)
            pyautogui.click(positionCenterBonus.x, positionCenterBonus.y)

        ##Segundo bonus do archer
        positionBonus2 = pyautogui.locateOnScreen('bonus2.png', grayscale=True, confidence=0.8)
        if positionBonus2:
            positionCenterBonus2 = pyautogui.center(positionBonus2)
            pyautogui.click(positionCenterBonus2.x, positionCenterBonus2.y)

        ##Cookie Close do ad do Archer
        positionClose = pyautogui.locateOnScreen('close.png', grayscale=True, confidence=0.8)
        if positionClose:
            positionCenterClose = pyautogui.center(positionClose)
            pyautogui.click(positionCenterClose.x, positionCenterClose.y)

        ##Cookie Close do ad do Archer
        positionClose2 = pyautogui.locateOnScreen('close2.png', grayscale=True, confidence=0.8)
        if positionClose2:
            positionCenterClose2 = pyautogui.center(positionClose2)
            pyautogui.click(positionCenterClose2.x, positionCenterClose2.y)

        ##Cookie Dourado
        positionDourado = pyautogui.locateOnScreen('dourado.png', grayscale=True, confidence=0.8)
        if positionDourado:
            positionCenterDourado = pyautogui.center(positionDourado)
            pyautogui.click(positionCenterDourado.x, positionCenterDourado.y)        ##Cookie Dourado

        ##Segundo Cookie Dourado
        positionDourado2 = pyautogui.locateOnScreen('dourado2.png', grayscale=True, confidence=0.8)
        if positionDourado2:
            positionCenterDourado2 = pyautogui.center(positionDourado2)
            pyautogui.click(positionCenterDourado2.x, positionCenterDourado2.y)

        ##Ligar Watch
        positionWatch = pyautogui.locateOnScreen('watch.png', grayscale=True, confidence=0.3)
        if positionWatch:
            positionCenterWatch = pyautogui.center(positionWatch)
            pyautogui.click(positionCenterWatch.x, positionCenterWatch.y)


except KeyboardInterrupt:
    print('\n')