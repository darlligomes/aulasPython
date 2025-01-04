tarefas, desfeito = [], []

def desfazer(lista):
    if len(lista) > 0:
        desfeito.append(lista.pop())
        print(f'{desfeito[-1]} desfeito')
        return lista
    
    if len(lista) == 0:
        print("Lista vazia")
        return lista

def adicionar(lista, item):
    print(f'{item} adicionada na lista')
    item = item.capitalize()
    lista.append(item)
    return lista 

def escolha(): 
    opcao = input("Escolha 1 - adicionar, 2 - desfazer, 3 - refazer, 4 - sair \n")
    return opcao

opcao = escolha()


while True:
    
    if opcao in ('1', '2', '3', '4'):
        if(opcao == '1'):
            acao = input("Adicione uma ação: ")
            tarefas = adicionar(tarefas, acao)
            print(tarefas)
            opcao = escolha()
            
        elif (opcao == '2'):
            tarefas = desfazer(tarefas)
            print(tarefas)
            opcao = escolha()
            
        elif (opcao == '3'):
            if (desfeito == []):
                print("Lista de refazer vazia")
            else:
                tarefas = adicionar(tarefas, desfeito.pop())
                print(tarefas)
                
                
            opcao = escolha()

    elif opcao == '4': 
        print("Encerrando!")
        break;
    
    else: 
        print("Opção inválida")
        opcao = escolha()