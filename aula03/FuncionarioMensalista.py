"""
Classe FuncionarioMensalista herda Funcionario.
É uma SubClasse de Funcionario.
FuncionarioMensalista também demonstra programação por diferença.
"""

import aula03.funcionario

class FuncionarioMensalista(aula03.funcionario):
    
    _faltas = 0
    _valorFalta = 0.0
    
    def __init__(self, primeiroNome, ultimoNome, salario, valorFalta):
        super().__init__(primeiroNome, ultimoNome, salario)
        self._valorFalta = valorFalta
    
    def calcularPagamento(self):
        return (self._salario - (self._faltas * self._valorFalta))
    
    def adicionaFaltas(self, faltas):
        self._faltas += faltas
        
    def inicializarFaltas(self):
        self._faltas=0
            
    
    