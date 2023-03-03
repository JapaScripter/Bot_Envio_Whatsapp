#Imports
import pywhatkit as pwk

#Input de definição do número
phone_number = input("Digite seu número +5511912345678: \n")

#Enviar msg whats
pwk.sendwhatmsg_instantly(phone_number, "Oie, é só um teste tá?", 13, 50, 3)