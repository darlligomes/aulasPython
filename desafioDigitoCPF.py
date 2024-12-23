def calculo(cpf, mascara) -> int:
    resultado: int = 0
    for numero in cpf:
        resultado += int(numero) * mascara
        mascara -= 1
    return resultado


cpf_limpo: '34551231360'
mascara = 10

# Limpa o CPF para que se 
# tenha apenas numeross, removendo letras e os sinais 
# como travessão, ponto final, etc

cpf_base = cpf_limpo[:9]
resultado = (calculo(cpf_base, mascara) * 10) % 11
decimo_digito = 0 if resultado >= 10 else resultado
cpf_calculado = cpf_base + str(decimo_digito)
mascara += 1

resultado = (calculo(cpf_calculado, mascara) * 10) % 11
decimoPrim_digito = 0 if resultado >= 10 else resultado
cpf_calculado += str(decimoPrim_digito)

cpf_calculado_formatado = f"{cpf_calculado[:3]}.{cpf_calculado[3:6]}.{cpf_calculado[6:9]}-{cpf_calculado[9:]}"

print(f"CPF gerado:: {cpf_calculado_formatado}")

    