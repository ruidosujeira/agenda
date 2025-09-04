def exibir_menu():
    """Exibe o menu principal da aplicação"""
    print("\n" + "="*50)
    print("           AGENDA DE CONTATOS")
    print("="*50)
    print("1. Adicionar contato")
    print("2. Visualizar todos os contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar como favorito")
    print("5. Ver contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")
    print("="*50)

def adicionar_contato():
    """Adiciona um novo contato à agenda"""
    print("\n--- ADICIONAR CONTATO ---")
    
    nome = input("Digite o nome: ").strip()
    if not nome:
        print("❌ Nome não pode estar vazio!")
        return
    
    telefone = input("Digite o telefone: ").strip()
    email = input("Digite o email: ").strip()
    
    # Pergunta se é favorito
    favorito_input = input("Marcar como favorito? (s/n): ").strip().lower()
    favorito = favorito_input in ['s', 'sim', 'y', 'yes']
    
    # Cria o contato
    contato = {
        'id': len(contatos) + 1,
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'favorito': favorito
    }
    
    contatos.append(contato)
    print(f"✅ Contato '{nome}' adicionado com sucesso!")

def visualizar_contatos():
    """Exibe todos os contatos cadastrados"""
    print("\n--- TODOS OS CONTATOS ---")
    
    if not contatos:
        print("📭 Nenhum contato cadastrado.")
        return
    
    for contato in contatos:
        favorito_icon = "⭐" if contato['favorito'] else "  "
        print(f"{favorito_icon} ID: {contato['id']} | Nome: {contato['nome']} | Tel: {contato['telefone']} | Email: {contato['email']}")

def editar_contato():
    """Edita um contato existente"""
    print("\n--- EDITAR CONTATO ---")
    
    if not contatos:
        print("📭 Nenhum contato cadastrado.")
        return
    
    # Mostra lista de contatos para escolha
    visualizar_contatos()
    
    try:
        id_contato = int(input("\nDigite o ID do contato que deseja editar: "))
        
        # Procura o contato pelo ID
        contato_encontrado = None
        for contato in contatos:
            if contato['id'] == id_contato:
                contato_encontrado = contato
                break
        
        if not contato_encontrado:
            print("❌ Contato não encontrado!")
            return
        
        print(f"\nEditando contato: {contato_encontrado['nome']}")
        
        # Permite editar cada campo
        novo_nome = input(f"Nome atual: {contato_encontrado['nome']}\nNovo nome (ou Enter para manter): ").strip()
        if novo_nome:
            contato_encontrado['nome'] = novo_nome
        
        novo_telefone = input(f"Telefone atual: {contato_encontrado['telefone']}\nNovo telefone (ou Enter para manter): ").strip()
        if novo_telefone:
            contato_encontrado['telefone'] = novo_telefone
        
        novo_email = input(f"Email atual: {contato_encontrado['email']}\nNovo email (ou Enter para manter): ").strip()
        if novo_email:
            contato_encontrado['email'] = novo_email
        
        print("✅ Contato editado com sucesso!")
        
    except ValueError:
        print("❌ ID deve ser um número!")

def alternar_favorito():
    """Marca ou desmarca um contato como favorito"""
    print("\n--- MARCAR/DESMARCAR FAVORITO ---")
    
    if not contatos:
        print("📭 Nenhum contato cadastrado.")
        return
    
    # Mostra lista de contatos para escolha
    visualizar_contatos()
    
    try:
        id_contato = int(input("\nDigite o ID do contato: "))
        
        # Procura o contato pelo ID
        contato_encontrado = None
        for contato in contatos:
            if contato['id'] == id_contato:
                contato_encontrado = contato
                break
        
        if not contato_encontrado:
            print("❌ Contato não encontrado!")
            return
        
        # Alterna o status de favorito
        contato_encontrado['favorito'] = not contato_encontrado['favorito']
        
        status = "marcado como favorito" if contato_encontrado['favorito'] else "desmarcado como favorito"
        print(f"✅ Contato '{contato_encontrado['nome']}' {status}!")
        
    except ValueError:
        print("❌ ID deve ser um número!")

def ver_favoritos():
    """Exibe apenas os contatos marcados como favoritos"""
    print("\n--- CONTATOS FAVORITOS ---")
    
    favoritos = [contato for contato in contatos if contato['favorito']]
    
    if not favoritos:
        print("⭐ Nenhum contato favorito.")
        return
    
    for contato in favoritos:
        print(f"⭐ ID: {contato['id']} | Nome: {contato['nome']} | Tel: {contato['telefone']} | Email: {contato['email']}")

def apagar_contato():
    """Remove um contato da agenda"""
    print("\n--- APAGAR CONTATO ---")
    
    if not contatos:
        print("📭 Nenhum contato cadastrado.")
        return
    
    # Mostra lista de contatos para escolha
    visualizar_contatos()
    
    try:
        id_contato = int(input("\nDigite o ID do contato que deseja apagar: "))
        
        # Procura o contato pelo ID
        contato_encontrado = None
        for i, contato in enumerate(contatos):
            if contato['id'] == id_contato:
                contato_encontrado = contato
                indice = i
                break
        
        if not contato_encontrado:
            print("❌ Contato não encontrado!")
            return
        
        # Confirma a exclusão
        confirmacao = input(f"Tem certeza que deseja apagar '{contato_encontrado['nome']}'? (s/n): ").strip().lower()
        
        if confirmacao in ['s', 'sim', 'y', 'yes']:
            contatos.pop(indice)
            print(f"✅ Contato '{contato_encontrado['nome']}' apagado com sucesso!")
        else:
            print("❌ Operação cancelada.")
        
    except ValueError:
        print("❌ ID deve ser um número!")

def main():
    """Função principal que controla o fluxo da aplicação"""
    print("🎉 Bem-vindo à Agenda de Contatos!")
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nEscolha uma opção (1-7): ").strip()
            
            if opcao == '1':
                adicionar_contato()
            elif opcao == '2':
                visualizar_contatos()
            elif opcao == '3':
                editar_contato()
            elif opcao == '4':
                alternar_favorito()
            elif opcao == '5':
                ver_favoritos()
            elif opcao == '6':
                apagar_contato()
            elif opcao == '7':
                print("\n👋 Obrigado por usar a Agenda de Contatos! Até logo!")
                break
            else:
                print("❌ Opção inválida! Escolha um número de 1 a 7.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

# Executa o programa apenas se este arquivo for executado diretamente
if __name__ == "__main__":
    main()
