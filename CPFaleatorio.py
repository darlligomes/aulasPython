import random

def calculo(cpf, mascara) -> int:
    resultado: int = 0
    for numero in cpf:
        resultado += int(numero) * mascara
        mascara -= 1
    return resultado


qtd_cpfs = int(input("Quantos CPFs deseja gerar? "))
print("CPF gerado:" )
for k in range(qtd_cpfs):
    nove_digitos: str = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))
        
    cpf_limpo = nove_digitos
    mascara = 10

    cpf_base = cpf_limpo[:9]
    resultado = (calculo(cpf_base, mascara) * 10) % 11
    decimo_digito = 0 if resultado >= 10 else resultado
    cpf_calculado = cpf_base + str(decimo_digito)
    mascara += 1

    resultado = (calculo(cpf_calculado, mascara) * 10) % 11
    decimoPrim_digito = 0 if resultado >= 10 else resultado
    cpf_calculado += str(decimoPrim_digito)

    cpf_calculado_formatado = f"{cpf_calculado[:3]}.{cpf_calculado[3:6]}.{cpf_calculado[6:9]}-{cpf_calculado[9:]}"

    print(f"{cpf_calculado_formatado}")