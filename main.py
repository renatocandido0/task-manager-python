from armazenamento import carregar_tarefas
from entrada import obter_numero
from tarefas import criar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa

tarefas = carregar_tarefas()

def exibir_menu():
    print("=== TASK MANAGER ===")
    print("1. Criar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")


while True:
    exibir_menu()
    opcao_escolhida = obter_numero("Escolha uma opção: ")
    if opcao_escolhida == 1:
        criar_tarefa(tarefas)
    elif opcao_escolhida == 2:
        listar_tarefas(tarefas)
    elif opcao_escolhida == 3:
        concluir_tarefa(tarefas)
    elif opcao_escolhida == 4:
        remover_tarefa(tarefas)
    elif opcao_escolhida == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")