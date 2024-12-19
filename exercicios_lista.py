import os 

compras: list = []
adicao: list = []
posicao: int = 0
valor: float = 0
nome: str = ''
selecionado: str = input("Selecione uma opção: \
    [i]nserir, [a]pagar [l]istar: \n").lower()

def adicionar(lista):
    os.system('cls')
    while True: 
        try: 
            nome = input("Adicione o nome do produto ou escreva 's' para sair: \n")
            if(nome == "s"):
                return
            valor = float(input("Insira o valor: "))
            break
        except ValueError:
            print("Valor inválido, insira novamente :)")
            valor = float(input("Insira o valor: "))
    lista.append((nome, valor))

def listar(lista):
    os.system('cls')
    if not lista:
        print("A lista está vazia!")
    else:
        for i, produto in enumerate(lista): 
            print(f"{i+1} - {produto[0]} - R$ {produto[1]:.2f}")
            
def deletar(lista, posicao):
    if posicao < 1 or posicao > len(lista):
        print("Posição inválida! Revise por favor")
        return
    else:
        confirme: str = input(f"Deseja excluir produto {lista[posicao-1][0]}? [s]im/[n]ão\n").lower()
        if(confirme == 's'):
            lista.pop(posicao - 1)
        else: 
            print("Sem exclusão")
            return
    os.system('cls')

def opcao():
    return input("Selecione uma opção: [i]nserir, [a]pagar, [l]istar, [s]air: \n").lower()

while(selecionado in ('i', 'a', 'l')):
    try:
        if selecionado == 'i':
            adicionar(compras)
           
        elif selecionado == 'a':
            if len(compras) == 0:
                print("Não há produtos para remover!")
            else:
                print("Insira o índice a ser removido")
                listar(compras)
                try:
                    posicao = int(input("Insira o índice a ser removido: "))
                    if posicao < 1 or posicao > len(compras):
                        print("Posição inválida! Revise por favor")
                    else:
                        deletar(compras, posicao)
                        print("Lista atualizada: ")
                        listar(compras)
                except ValueError:
                    print("Por favor, insira um número válido para o índice.")
           
        elif selecionado == 'l':
            listar(compras)
            
        selecionado = opcao()
    
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")        