palavra = "paralelepípedo"

for letra in palavra:
    print(letra, end = " ")

print("fim")

aprovados = ["Rafaela", "Pedro", "Renato"]

for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

dias_semana = ("domingo", "segunda", "terça")

for dia in dias_semana:
    print(dia, end = " ")