solicitacoes = []

def cadastro():
    id = input("Informe o ID: ")
    tipo = input("Informe o Tipo: ")
    descricao = input("Informe a Descrição: ")

    solicitacoes.append({
        "id": id,
        "tipo": tipo,
        "descricao": descricao,
        "status": "OK"
    })
    print("O item foi Cadastrado")

def atualizarItem():
    id = input("Qual o ID para atualizar: ")
    for s in solicitacoes:

        if s["id"] == id:
            novo_status = input("Novo status: ")
            s["status"] = novo_status
            print("O item foi Atualizado")
            return
    print("O ID não encontrado")

def listarItem():
    if not solicitacoes:
        print("Não existe nenhum cadastro")
        return
    for s in solicitacoes:
        print(f"ID: {s['id']}, Tipo: {s['tipo']}, Status: {s['status']}")

def excluirItem():
    id = input("Qual o ID para excluir: ")
    for i, s in enumerate(solicitacoes):
        
        if s["id"] == id:
            solicitacoes.pop(i)
            print("O item foi Excluído")
            return
    print("O ID não encontrado")

while True:
    print("\n1-Cadastrar 2-Atualizar 3-Listar 4-Excluir 5-Sair")
    opcao = input("Opção: ")
    
    if opcao == "1":
        cadastro()
    elif opcao == "2":
        atualizarItem()
    elif opcao == "3":
        listarItem()
    elif opcao == "4":
        excluirItem()
    elif opcao == "5":
        break
    else:
        print("Essa opção não existe")