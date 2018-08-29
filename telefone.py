'''
Agenda simples
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '0.0.1'
__email__ = 'caio.c3sar@outlook.com'
__status__ = 'Development'

class Telefone:
  def __init__(self, nome, telefone):
    self.__nome = nome
    self.__telefone = telefone

  def getNome(self):
    return self.__nome
  
  def getTelefone(self):
    return self.__telefone