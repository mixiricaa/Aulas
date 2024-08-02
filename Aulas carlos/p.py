import pyautogui, time

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("sp.senai.br/unidade/jundiai/")
pyautogui.press("enter")
time.sleep(2)
cursos = pyautogui.locateOnScreen('cursos.png')
surcos = pyautogui.center(cursos)
pyautogui.click(surcos.x, surcos.y)