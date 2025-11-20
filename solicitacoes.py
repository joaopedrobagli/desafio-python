solicitacoes = []

def cadastrar():
    id = input("ID: ")
    tipo = input("Tipo: ")
    descricao = input("Descrição: ")
    solicitacoes.append({
        "id": id,
        "tipo": tipo,
        "descricao": descricao,
        "status": "Pendente"
    })
    print("Cadastrado!")

def listar():
    if not solicitacoes:
        print("Nada para listar")
        return
    for s in solicitacoes:
        print(f"ID: {s['id']}, Tipo: {s['tipo']}, Status: {s['status']}")

def atualizar():
    id = input("ID para atualizar: ")
    for s in solicitacoes:
        if s["id"] == id:
            novo_status = input("Novo status: ")
            s["status"] = novo_status
            print("Atualizado!")
            return
    print("ID não encontrado")

def excluir():
    id = input("ID para excluir: ")
    for i, s in enumerate(solicitacoes):
        if s["id"] == id:
            solicitacoes.pop(i)
            print("Excluído!")
            return
    print("ID não encontrado")

while True:
    print("\n1-Cadastrar 2-Listar 3-Atualizar 4-Excluir 5-Sair")
    op = input("Opção: ")
    
    if op == "1":
        cadastrar()
    elif op == "2":
        listar()
    elif op == "3":
        atualizar()
    elif op == "4":
        excluir()
    elif op == "5":
        break
    else:
        print("Opção inválida")