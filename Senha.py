import pywhatkit
import keyboard
import time
from datetime import datetime
# A senha que ja foi salva pelo usuario
secreta = str("ADM123")
def correta(str):
	if senha == secreta:
		print("Senha correta!")
# Duas defs preparadas com o código de comparação
def incorreta(str):
	if senha != secreta:
		print("Senha incorreta!")
	contatos = ['+5515998091511']
	while len(contatos) >= 1:
	 pywhatkit.sendwhatmsg(contatos[0], '!!Atenção!!, tentativa de acesso negado.', datetime.now().hour,datetime.now().minute + 2)
del contatos[0]
time.sleep(60)
keyboard.press_and_release('ctrl + w')
# Console esperando a senha ser digitada
senha = input("Digite sua senha: ")
# A mensagem vai depender da senha digitada pelo usuario
if senha == secreta:
	correta("Senha correta")
else:
	incorreta("Senha incorreta!")