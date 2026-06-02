import os

def limpar_tela():
    """Limpa o terminal para manter o menu organizado."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("\n" + "="*20)
    print("      MENU")
    print("="*20)
    print("1 - Cadastrar Novo")
    print("2 - Listar Todos")
    print("3 - Sair")
    print("-" * 20)

def sistema_principal():
    banco_de_dados = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            telefone = input("Telefone: ").strip()
            
            # Criamos um dicionário para representar o registro
            pessoa = {
                "nome": nome, 
                "email": email, 
                "telefone": telefone
            }
            
            banco_de_dados.append(pessoa)
            print(f"\n✅ Registro de {nome} adicionado!")

        elif opcao == "2":
            limpar_tela()
            print("\n--- LISTA DE CONTATOS ---")
            if not banco_de_dados:
                print("Nenhum registro encontrado.")
            else:
                for i, p in enumerate(banco_de_dados, 1):
                    print(f"{i}. {p['nome'].upper()}")
                    print(f"   📧 {p['email']}")
                    print(f"   📞 {p['telefone']}")
                    print("-" * 25)
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "3":
            print("Saindo do sistema...")
            break
        
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    sistema_principal()