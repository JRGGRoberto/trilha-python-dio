import textwrap

def menu():
  menu = """
       MENU
  [D]\tDepositar
  [S]\tSacar
  [E]\tExtrato
  [nc]\tNova Conta
  [lC]\tListar Contas
  [nu]\tNovo usuário
  [q]\tSair
  => """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    print("\n=== Depósito realizado com sucessos! ===")
  else:
    print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
  
  return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques

  if excedeu_saldo:
    print("\n@@@ Operação falhou! Saldo insuficiente. @@@")

  elif excedeu_limite:
    print("\n@@@ Operação falhou! Valor do saldo excede o limite. @@@")

  elif excedeu_saques:
    print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
  
  elif valor > 0:
    sal