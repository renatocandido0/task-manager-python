from armazenamento import salvar_tarefas
from entrada import obter_numero, obter_texto

def gerar_novo_id(tarefas):
    if len(tarefas) == 0:
            novo_id = len(tarefas) + 1
            return novo_id
    else:
        maior_id = tarefas[0]["id"]
        for tarefa in tarefas:
            if tarefa["id"] > maior_id:
                maior_id = tarefa["id"]
        novo_id = maior_id + 1
        return novo_id

def criar_tarefa(tarefas):
    print("Criando nova tarefa...")
    titulo = obter_texto("Digite o título da tarefa: ")
    descricao = obter_texto("Digite a descrição da tarefa: ")
    novo_id = gerar_novo_id(tarefas)
    tarefa = {
                "id": novo_id,
                "titulo": titulo,
                "descricao": descricao,
                "status": "pendente"
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

def listar_tarefas(tarefas):
    print("Listando tarefas...")
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("=== TAREFAS ===")
        for tarefa in tarefas:
            print()
            print(f"Id: {tarefa["id"]}")
            print(f"Titulo: {tarefa["titulo"]}")
            print(f"Descrição: {tarefa["descricao"]}")
            print(f"Status: {tarefa["status"]}")
            print()


def concluir_tarefa(tarefas):
    encontrou = False
    tarefa_encerrar = obter_numero("Digite o id da tarefa: ")

    for tarefa in tarefas:
        if tarefa_encerrar == tarefa["id"]:
            encontrou = True
            tarefa["status"] = "concluído"
            print("Tarefa concluída com sucesso!")
            salvar_tarefas(tarefas)
            break
    if not encontrou:
        print("Tarefa não encontrada!")

def remover_tarefa(tarefas):
    encontrou = False
    tarefa_remover = obter_numero("Digite o id da tarefa: ")

    for tarefa in tarefas:
        if tarefa_remover == tarefa["id"]:
            encontrou = True
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso")
            salvar_tarefas(tarefas)
            break
    if not encontrou:
        print("Tarefa não encontrada!")