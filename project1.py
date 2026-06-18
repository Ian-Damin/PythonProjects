#Descoberta do 10 digito de um CPF

cpf = '53560252032'

noveDigitos = cpf[:9] #nove primeiros digitos são necessários para descoberta do 1 digito
contador = 10 #contador regressivo
digito1 = 0 # onde irá ser adicionado o valor

for digito in noveDigitos:
    digito1 += int(digito) * contador #realiza multiplicação e a soma no digito1
    contador -= 1

print(digito1 * 10 % 11)
digito1 = digito1 if digito1 <=9 else 0

