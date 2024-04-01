import pyautogui
from time import sleep

# 1- Clicar e digitar meu usuario
pyautogui.click(983,542,duration=2)
pyautogui.write('hya')
# 2- Clicar e digitar minha senha
pyautogui.click(958,568,duration=2)
pyautogui.write('123')
# 3- Clicar em entrar
pyautogui.click(878,593,duration=2)
# 4- Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
#       1- Digitar produto
        pyautogui.click(737,526,duration=2)
        pyautogui.write(produto)
#       2- Digitar quantidade
        pyautogui.click(723,556,duration=2)
        pyautogui.write(quantidade)
#       3- Digitar preço
        pyautogui.click(712,583,duration=2)
        pyautogui.write(preco)
#       4- Clickar em Registrar
        pyautogui.click(589,735,duration=1)
        sleep(1)

