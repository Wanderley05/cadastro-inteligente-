contatos = []

def mostrar_menu():
    print("\n=== AGENDA DE CONTATOS ===")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Editar contato")
    print("4 - Marcar/Desmarcar favorito")
    print("5 - Listar favoritos")
    print("6 - Deletar contato")
    print("0 - Sair")

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }

    contatos.append(contato)
    print("✅ Contato adicionado!")

def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    for i, c in enumerate(contatos):
        fav = "⭐" if c["favorito"] else ""
        print(f"{i} - {c['nome']} | {c['telefone']} | {c['email']} {fav}")

def editar_contato():
    listar_contatos()
    try:
        indice = int(input("Digite o índice do contato: "))
        contato = contatos[indice]

        contato["nome"] = input("Novo nome: ")
        contato["telefone"] = input("Novo telefone: ")
        contato["email"] = input("Novo email: ")

        print("✏️ Contato atualizado!")
    except:
        print("❌ Índice inválido.")

def favoritar_contato():
    listar_contatos()
    try:
        indice = int(input("Digite o índice do contato: "))
        contatos[indice]["favorito"] = not contatos[indice]["favorito"]

        status = "favorito" if contatos[indice]["favorito"] else "não favorito"
        print(f"⭐ Contato agora é {status}.")
    except:
        print("❌ Índice inválido.")

def listar_favoritos():
    favoritos = [c for c in contatos if c["favorito"]]

    if not favoritos:
        print("Nenhum favorito.")
        return

    for c in favoritos:
        print(f"{c['nome']} | {c['telefone']} | {c['email']} ⭐")

def deletar_contato():
    listar_contatos()
    try:
        indice = int(input("Digite o índice do contato: "))
        contatos.pop(indice)
        print("🗑️ Contato removido.")
    except:
        print("❌ Índice inválido.")

# LOOP PRINCIPAL
while True:
    mostrar_menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        editar_contato()
    elif opcao == "4":
        favoritar_contato()
    elif opcao == "5":
        listar_favoritos()
    elif opcao == "6":
        deletar_contato()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")