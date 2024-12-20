palavra_secreta: str = input("Insira a palavra secreta: ").lower()
exibicao: str = '*' * len(palavra_secreta)
tentativas: int = 0
ganhou: bool = False

print("início do jogo! :)" \
      f"\nPalavra é: {exibicao}")

while not ganhou:
    letra = input("Insira uma letra: ").lower()
    
    if(letra.isalpha()):
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:  
                exibicao = exibicao[:i] + letra + exibicao[i+1:]

        if '*' not in exibicao:
            ganhou = True
            tentativas += 1
            print("Parabéns, você venceu!")
            
        else:
            tentativas += 1
            print(exibicao)
    else:
        print("Dígito inválido, apenas letras!")


print(f"Total de tentativas: {tentativas}")
print(f"A palavra era: {palavra_secreta}")
print("Fim do jogo!")