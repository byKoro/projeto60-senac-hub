import utils as ut
import system as st
import cores as cr
import utils as utils
def cadastrar_usuario():
    niveis_de_acesso = "\n1 - Administrador\n2 - Recepcionista\n3 - Médico"

    usuario = input("Digite nome de Usuário: ")
    while st.buscar_usuario(usuario) is not None:
        print("Usuário já existe. Tente novamente.")
        usuario = input("Digite nome de Usuário: ")
        
        
    senha = input("Digite a senha: ")
    while len(senha) > 12:
        print(cr.vermelho("senha excedeu o limite de caracteres, máximo 11!"))
        senha = input("Digite a senha: ")
    while len(senha) < 4:
        print(cr.vermelho("senha não atingiu o mínimo de caracteres, mínimo 03!"))
        senha = input("Digite a senha: ")

    print(f"{cr.azul(f"Níveis de acesso: {niveis_de_acesso}")}")
    nivel = input("Digite seu nível de acesso: ")
    while nivel not in ["1", "2", "3"]:
        print(cr.vermelho("Nível de acesso inválido. Tente novamente."))
        nivel = input("Digite seu nível de acesso: ")
        
    if nivel == "1":
        nivel = "Administrador"
    elif nivel == "2":
        nivel = "Recepcionista"
    elif nivel == "3":
        nivel = "Médico"
            
    informacoes =  {
        "usuario": usuario, 
        "senha": senha, 
        "nivel_de_acesso": nivel, 
        "id": ut.gerar_id("usuarios")
        }
    
    ut.adicionar("usuarios", informacoes)
    return informacoes

def editar_usuario():
  lista_usuarios = utils.carregar("usuarios")

  usuario = input("Qual usuário deseja alterar: ")
  while st.buscar_usuario(usuario) is None:
    print(cr.vermelho("O usuário não existe"))
    usuario = input("Qual usuário deseja alterar: ")
    usuario = st.buscar_usuario(usuario)
  usuario = st.buscar_usuario(usuario)

  editar_usuario = {
    "usuario": usuario["usuario"],
    "senha": usuario["senha"],
    "nivel_de_acesso": usuario["nivel_de_acesso"],
    "id": usuario["id"]
  }
  nome = editar_usuario["usuario"]
  senha = editar_usuario["senha"]
  nivel = editar_usuario["nivel_de_acesso"]
  id_usuario = editar_usuario["id"]


  print(f"{cr.amarelo(f"-- Editar Usuario --")}")
  print("1.Editar nome de usuário")
  print("2.Resetar senha")
  print("3.Editar nível de acesso")
  print("4.Deletar usuario")
  opcao = input("Escolha uma opção: ")

  while opcao not in ["1","2","3","4"]:
    print(cr.vermelho("Opção inválida!"))
    opcao = input("Escolha uma opção: ")
  
  if opcao == "1": 
    nome = input("Novo nome de usuário: ")
    while st.buscar_usuario(nome) is not None:
      print(cr.vermelho("Esse nome já existe!"))
      nome = input("Novo nome de usuário: ")
    print(cr.verde("Nome alterado com sucesso! "))

  elif opcao == "2":
    senha = input("Digíte a nova senha: ")
    while len(senha) > 12:
      senha = input(f"Digíte a nova senha ({cr.vermelho("Máximo 11 caracteres") }): ")
  
  elif opcao == "3":
    nivel = print(mn.niveis_de_acesso)

  informacoes_atualizadas = {
    "usuario": nome,
    "senha": senha,
    "nivel_de_acesso": nivel,
    "id": id_usuario
  }

  for i, u in enumerate(lista_usuarios):
      if usuario == u:
          lista_usuarios[i] = informacoes_atualizadas
          break
  
  utils.salvar("usuarios", lista_usuarios)

  return informacoes_atualizadas

editar_usuario()