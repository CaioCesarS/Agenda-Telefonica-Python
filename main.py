'''
Agenda simples
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

from controller import Controller

agenda = []

print('~'*30)
print('Bem vindo à agendar telefonica')
print('~'*30)

while True:
  print('1 - Cadastrar contato;')
  print('2 - Listar contato;')
  print('3 - Listar todos os contatos;')
  print('4 - Apagar contato;')
  print('5 - Apagar todos os contatos;')
  print('6 - Sair.')

  op = int(input('Entre com a opção desejada: '))

  if op == 1:
    nome = input('Digite o nome:')
    tel = int(input('Digite o telefone:'))
    agenda.append(Controller.inserir(nome, tel))
  elif op == 2:
    nome = input('Digite o nome para a pesquisa:')
    Controller.listarNome(agenda, nome)
  elif op == 3:
    Controller.listarAll(agenda)
  elif op == 4:
    nome = input('Digite o nome para a pesquisa:')
    print(Controller.deletarNome(agenda, nome))
  elif op == 5:
    print(Controller.deletarAll(agenda))
  elif op == 6:
    break
  else:
    print('Digite a opção correta!')

print('Obrigado por usar a agenda!!!')
print('~'*30)
