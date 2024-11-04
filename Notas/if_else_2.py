n = int(input("Digite sua idade:"))

def faixa_etaria(idade):
    if 0 <= idade < 18:
        return "Menor de idade"
    elif idade in range(18, 50):
        return "Adulto"
    elif idade in range (51, 100):
        return "Tá ficando véi"
    else:
        return "Idade de vampiro"
    
print(faixa_etaria(n))