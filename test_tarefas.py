from tarefas import gerar_novo_id

def test_gerar_id_lista_vazia():
    tarefas = []
    resultado = gerar_novo_id(tarefas)
    assert resultado == 1

def test_gerar_id_com_ids_nao_sequenciais():
    tarefas = [
        {"id": 1},
        {"id": 3},
        {"id": 7}
    ]
    resultado = gerar_novo_id(tarefas)
    assert resultado == 8

def test_gerar_id_sequencial():
    tarefas = [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
    resultado = gerar_novo_id(tarefas)
    assert resultado == 4