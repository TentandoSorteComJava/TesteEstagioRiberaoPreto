"""5) Escreva um programa que inverta os caracteres de um string. 


IMPORTANTE: 

	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

	b) Evite usar funções prontas, como, por exemplo, reverse; """
 
#exemplo pratico
String = "Inversa"[::-1]
print(String)

#exemplo da logica de progr estruturada
def inverso(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "inversa"
print(inverso(s))