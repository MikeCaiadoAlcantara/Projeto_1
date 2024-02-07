# A senha que ja foi salva pelo usuario
secreta = str("ADM123")
# Console esperando a senha correta ser digitada
senha = input("Digite sua senha: ")
# Enquanto a senha não for a correta, ele vai trazer um nova chance
while senha != secreta:
 senha = input("Tente novamente! ")
# Se a senha for a correta o programa segue seu fluxo
if senha == secreta:
 print("Senha correta!")