import re

def calculo(cpf, mascara) -> int:
    resultado: int = 0
    for numero in cpf:
        resultado += int(numero) * mascara
        mascara -= 1
    return resultado

while True:
    try:
        cpf_limpo: str = input("Insira o CPF: ").strip()
        mascara = 10

        # Limpa o CPF para que se 
        # tenha apenas numeross, removendo letras e os sinais 
        # como travessão, ponto final, etc
        cpf_limpo = re.sub(r'[^0-9]', '', cpf_limpo)
        
        if(cpf_limpo == '0'): 
            print("Encerrando checagem!...")
            break
        
        if len(cpf_limpo) < 11:
            print("CPF inválido! Certifique-se de digitar pelo menos 11 números.")
            continue
        
        if ((cpf_limpo[0] * len(cpf_limpo) == cpf_limpo)):
            print("O mesmo dado foi repetido!")
            continue;

        cpf_base = cpf_limpo[:9]
        resultado = (calculo(cpf_base, mascara) * 10) % 11
        decimo_digito = 0 if resultado >= 10 else resultado
        cpf_calculado = cpf_base + str(decimo_digito)
        mascara += 1

        resultado = (calculo(cpf_calculado, mascara) * 10) % 11
        decimoPrim_digito = 0 if resultado >= 10 else resultado
        cpf_calculado += str(decimoPrim_digito)

        cpf_inserido_formatado = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:11]}"
        cpf_calculado_formatado = f"{cpf_calculado[:3]}.{cpf_calculado[3:6]}.{cpf_calculado[6:9]}-{cpf_calculado[9:]}"

        print(f"Estado do CPF inserido: {cpf_inserido_formatado}")
        print(f"Estado do CPF calculado: {cpf_calculado_formatado}")

        if cpf_limpo == cpf_calculado:
            print("CPF válido! Aperte '0' para sair.")
            continue
        else:
            print("CPF inválido! Tente novamente.")
    except ValueError:
        print("Erro: Certifique-se de digitar apenas números.")        
    except Exception as e:
        print(f"Erro: {e}. Insira o CPF novamente.")
