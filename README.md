# Task Manager Python

## Sobre o projeto

O Task Manager é uma aplicação de linha de comando desenvolvida em Python que permite criar, listar, concluir e remover tarefas, mantendo os dados salvos entre as execuções do programa.

Desenvolvi este projeto com o objetivo de fortalecer minha base em Python e aplicar na prática conceitos de programação e engenharia de software, me preparando para projetos mais complexos.

## Funcionalidades

- Criar novas tarefas
- Listar tarefas cadastradas
- Marcar tarefas como concluídas
- Remover tarefas
- Salvar e carregar tarefas utilizando JSON

## Tecnologias utilizadas

- **Python** — Linguagem utilizada para desenvolver a aplicação
- **JSON** — Formato utilizado para armazenar e carregar as tarefas
- **pytest** — Framework utilizado para criar e executar testes automatizados
- **Git** — Sistema utilizado para controle de versão do projeto

## Estrutura do projeto

- `main.py` — Ponto de entrada da aplicação, responsável por coordenar o fluxo principal do programa
- `tarefas.py` — Contém as operações de criação, listagem, conclusão e remoção de tarefas
- `entrada.py` — Responsável pela entrada e validação dos dados fornecidos pelo usuário
- `armazenamento.py` — Responsável pela persistência das tarefas no arquivo JSON
- `test_tarefas.py` — Contém os testes automatizados da aplicação utilizando pytest
- `tarefas.json` — Arquivo utilizado para persistir os dados das tarefas

## Como executar

Clone o repositório:

```bash
git clone https://github.com/renatocandido0/task-manager-python.git
```

Acesse a pasta do projeto:

```bash
cd task-manager-python
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python main.py
```

## Testes

Para executar os testes automatizados:

```bash
pytest -v
```