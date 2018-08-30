'''
Agenda simples
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

from telefone import Telefone

class Controller():
  def inserir(nome, telefone):
    return Telefone(nome, telefone)

  def listarAll(listaTelefone):
    for tel in listaTelefone:
      print('{} | {}'.format(tel.getNome(), tel.getTelefone()))

  def listarNome(listaTelefone, nome):
    cont = 0
    for tel in listaTelefone:
      if tel.getNome() == nome:
        print('{} | {}'.format(tel.getNome(), tel.getTelefone()))
        break
      cont += 1

  def deletarAll(listaTelefone):
    if len(listaTelefone) != 0:
      listaTelefone.clear()
      return 'Todos os contatos foram removidos!'
    else:
      return 'A lista telefonica está vazia!'

  def deletarNome(listaTelefone, nome):
    if len(listaTelefone) != 0:
      cont = 0
      for tel in listaTelefone:
        if tel.getNome() == nome:
          listaTelefone.pop(cont)
          return 'Contado {} removido com sucesso!'.format(nome)
        else:
          return 'Nome não encontrado!'
    else:
      return 'Lista está vazia!'
