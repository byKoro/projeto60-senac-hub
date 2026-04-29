import json
import os
def salvar(arquivo, lista):
  with open(f"{arquivo}.json","w") as f:
    json.dump(lista, f, indent=4)
    return True

def carregar(arquivo):
  if not os.path.exists(f"{arquivo}.json"):
    with open(f"{arquivo}.json","w") as f:
      json.dump([], f)
      return []
  else:
    with open(f"{arquivo}.json","r") as f:
        try:
            return json.load(f)
        except:
            salvar(arquivo,[])
            return []

def adicionar(arquivo,dicionario):
  informacoes = carregar(arquivo)
  informacoes.append(dicionario)
  salvar(arquivo, informacoes)
  return True

def gerar_id(arquivo):
  informacoes = carregar(arquivo)
  if not informacoes:
    return 1
  maior_id = 0
  for i in informacoes:
    if i["id"] > maior_id:
      maior_id = i["id"]
  return maior_id + 1
