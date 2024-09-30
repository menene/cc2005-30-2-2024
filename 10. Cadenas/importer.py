
output = "Elemento:Viga;Código:B3214;Inicio:(0.00,0.00,0.00);Fin:(10.00,0.00,3.00);Material:Acero;Altura:N/A;Área:N/A;Profundidad:N/A;Ancho:N/A|Elemento:Columna;Código:C9821;Inicio:N/A;Fin:N/A;Material:Hormigón;Altura:10.00;Área:N/A;Profundidad:N/A;Ancho:N/A|Elemento:Losa;Código:S6512;Inicio:(0.00,0.00,0.00);Fin:N/A;Material:Hormigón;Altura:N/A;Área:100.00m2;Profundidad:N/A;Ancho:N/A|Elemento:Cimentación;Código:F4356;Inicio:N/A;Fin:N/A;Material:HormigónArmado;Altura:N/A;Área:N/A;Profundidad:5.00;Ancho:3.00"


lista = output.split("|")

# print(lista)
# print(len(lista))
# print(lista[0])

for elemento in lista:
    atributos = elemento.split(";")
    
    for atributo in atributos:
        print(atributo)
    
    print()