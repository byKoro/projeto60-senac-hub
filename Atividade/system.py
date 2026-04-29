import utils as utils
import cores as cr

def buscar_usuario(usuario):
  informacoes = utils.carregar("usuarios")
  for i in informacoes:
    if i["usuario"] == usuario:
      return i
  return None

def logar_usuario(usuario,senha):
  informacoes = utils.carregar("usuarios")
  for i in informacoes:
    if i["usuario"] == usuario and i["senha"] == senha:
      return i

  return None

def editar_usuario():
  lista_usuarios = utils.carregar("usuarios")

  usuario = input("Qual usuário deseja alterar: ")
  while buscar_usuario(usuario) is None:
    print(cr.vermelho("O usuário não existe"))
    usuario = input("Qual usuário deseja alterar: ")
    usuario = buscar_usuario(usuario)
  usuario = buscar_usuario(usuario)

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
    while buscar_usuario(nome) is not None:
      print(cr.vermelho("Esse nome já existe!"))
      nome = input("Novo nome de usuário: ")

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
