class Tarefa:
    def __init__(self, id, titulo, descricao, data_vencimento, status="pendente"):
        self.id = id 
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.status = status 

    def to_dict(self): 
        return{
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data_vencimento": self.data_vencimento,
            "status": self.status
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["titulo"],
            data["descricao"],
            data["data_vencimento"],
            data["status"]
         )

import json
import os

class GerenciadorTarefas:
    def __init__(self, arquivo="tarefa.json"):
        self.arquivo = arquivo
        self.tarefas = []
        self.carregar_tarefas()

    def carregar_tarefas(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self.tarefas = [Tarefa.from_dict(t) for t in data]
                except json.JSONDecodeError:
                    self.tarefas = []
        else: 
            self.tarefas = []

    def salvar_tarefas(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tarefas], f, indent=4)

    def adicionar_tarefa(self, titulo, descricao, data_vencimento):
        novo_id = 1 if not self.tarefas else max(t.id for t in self.tarefas) + 1
        nova_tarefa = Tarefa(novo_id, titulo, descricao, data_vencimento)
        self.tarefas.append(nova_tarefa)
        self.salvar_tarefas()
        print("Tarefa adicionada com sucesso!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
            return
        for tarefa in self.tarefas:
            print("-" * 40)
            print(f"ID: {tarefa.id}")
            print(f"Título: {tarefa.titulo}")
            print(f"Descrição: {tarefa.descricao}")
            print(f"Data de vencimento: {tarefa.data_vencimento}")
            print(f"Status:{tarefa.status}")
        print("-"* 40)

    def atualizar_tarefas(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                novo_titulo = input("Novo título (Enter para manter):")
                if novo_titulo: 
                    tarefa.titulo = novo_titulo
                
                nova_descricao = input("Nova descrição (Enter para manter):")
                if nova_descricao: 
                    tarefa.descricao = nova_descricao

                nova_data = input("Nova data de vencimento (dd/mm/aaaa) (Enter para manter)")
                if nova_data:
                    tarefa.data_vencimento = nova_data

                novo_status = input("Novo status (Pendente/Concluída)(Enter para manter):")
                if novo_status:
                    tarefa.status = novo_status

                self.salvar_tarefas()
                print("Tarefa atualizada com sucesso!")
                return
        print("Tarefa não encontrada.")

    def remover_tarefa(self, id):
        for tarefa in self.tarefas: 
            if tarefa.id == id:
                self.tarefas.remove(tarefa)
                self.salvar_tarefas()
                print("Tarefa removida com sucesso!")
                return
            print("Tarefa não encontrada.")

def menu():
    gerenciador = GerenciadorTarefas()
    while True:
        print("\n--- Sistema de gerenciamento de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefa")
        print("3. Atualizar Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            data_vencimento = input("Data de vencimento (dd/mm/aaaa):")
            gerenciador.adicionar_tarefa(titulo, descricao, data_vencimento)
        elif opcao == "2":
            gerenciador.listar_tarefas()
        elif opcao == "3":
            try:
                id_atualizar = int(input("Digite o ID da tarefa a atualizar: "))
                gerenciador.atualizar_tarefas(id_atualizar)
            except ValueError:
                print("ID inválido.")
        elif opcao == "4":
            try: 
                id_remover = int(input("Digite o ID da tarefa a remover"))
                gerenciador.remover_tarefa(id_remover)
            except ValueError:
                print("ID inválido.")
        elif opcao == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
     