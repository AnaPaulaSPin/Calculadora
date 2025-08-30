import os

def RegistrarHistorico(op1,sinal,op2, resultado):
    with open("historico.txt", "a") as arquivo:
     texto = "{} {} {} = {}\n".format(op1, sinal, op2,resultado)
     arquivo.write(texto)
     arquivo.close()


def validarSinal(operacao):
   i = 0
   sinais = '+-/*^%'
   # encontrar o sinal:
   while i < len(operacao):
      if operacao[i] in sinais:
         return i
      else:
         i = i+1
    
   return -1

def ValidarNumero(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def ValidarFloat(num):
    try:
        float_valor = float(num)   
        if '.' in num:              
            return True
        else:
            return False              
    except ValueError:
        return False

while 1:
    print("\033[95m=" * 120)
    print('\033[96mCalculadora Py\033[0m'.center(121))
    print("\033[95m=" * 120)
    print('\n')

    print('\033[93m1- Calculadora'.center(119))
    print('\033[93m2- Manual de uso'.center(119))
    print('\033[93m3- Historico'.center(119))
    print('\033[93m4- Encerrar\033[0m'.center(119))


    r = input("\033[92mEscolha: \033[0m")

    if r.isalpha():
       print("\033[91mDigite uma opção de 1 a 4!\033[0m".center(120))
       os.system("pause")
       os.system('cls')
       continue
    
    
    if r == '1':
        os.system('cls')

        while(1):
          # Verificar para ve se a entrada esta no modelo:
          while(1):
           print('\033[95m')
           print("\033[96m Calculadora: \033[95m".center(130,'='))
           print('\n')
           print("\033[93mOperações disponiveis:".center(130))
           print('\033[93mSoma(+), Subtração(-), Multiplicação(*)'.center(130))
           print('\033[93mDivisão(/), Resto de Devisão(%), Pontencia(^)'.center(130))
           print('\033[93mou Digite -1 para sair!\n\033[0m'.center(130))
           operacao = input("\033[97mDigite a operação(Ex:3+4): \033[0m")

           if operacao == '-1':
               break
           
           #tratando as entradas dos operando:
           operacao = operacao.replace(' ', '')
           pos = validarSinal(operacao)
           if pos == -1:
              print('\033[91mSinal não foi digitado ou é invalido!\033[0m'.center(120))
              os.system("pause")
              os.system('cls')
              continue
              
           op1 = operacao[:pos]
           op2 = operacao[pos+1:]
           sinal = operacao[pos]
           

         
           if not (ValidarNumero(op1) and ValidarNumero(op2)):
              print("\033[91mOs operandos precisam ser números!Digite no modelo: Operando sinal Operando \033[0m".center(120))
              os.system("pause")
              os.system('cls')
              continue
           
           # Validar Tipo(Inteiro ou float)
           else:
               if ValidarFloat(op1):
                  op1 = float(op1)
               else:
                  op1 = int(op1)

               if ValidarFloat(op2):
                  op2 = float(op2)
               else:
                op2 = int(op2)
            
               break

          if operacao == '-1':
               print('Saindo da calculadora...'.center(120))
               break
          

          if sinal == '+':
              print("\033[92mResposta: {}\033[0m".format(op1 + op2 ).center(20) )
              RegistrarHistorico(op1,sinal,op2,op1 + op2)

          elif sinal == '-':
              print("\033[92mResposta: {}\033[0m".format(op1 - op2).center(20))
              RegistrarHistorico(op1,sinal,op2,op1 - op2)

          elif sinal == '/':
              if op2 == 0:
                  print('\033[91mDivisão por zero não é permitida!\033[0m'.center(120))
              else:
               print("\033[92mResposta:{}\033[0m".format(op1 / op2).center(20))
               RegistrarHistorico(op1,sinal,op2,op1 / op2)

          elif sinal == '*':
              print("\033[92mResposta:{}\033[0m".format(op1 * op2).center(20))
              RegistrarHistorico(op1,sinal,op2,op1 * op2)

          elif sinal == '^':
              print("\033[92mResposta:{}\033[0m".format(op1 ** op2).center(20))
              RegistrarHistorico(op1,sinal,op2,op1 ** op2)

          elif sinal == '%':
              print("\033[92mResposta:{}\033[0m".format(op1 % op2).center(20))
              RegistrarHistorico(op1,sinal,op2,op1 % op2)
          else:
              print('\033[91mSinal invalido!\033[0m'.center(120))
              
          os.system("pause")
          os.system('cls')
        
        os.system("pause")
        os.system('cls')


    
    elif r == '2':
     os.system('cls')
     print('\033[95m')
     print('\033[94m   Manual de Uso  \033[95m'.center(130,'='))
     print('\033[92mBem-vindo(a) à Calculadora Py!'.center(130))
     print('\033[97mRegras para digitar corretamente as operações:'.center(130))
     print('\033[93m1. Digite apenas números inteiros de 0 a 9 como operandos.'.center(130))
     print('\033[93m2. Escolha apenas uma operação por vez:'.center(130))
     print('\033[93m   Soma (+), Subtração (-), Multiplicação (*), Divisão (/), Resto de Divisão (%), Potência (^).'.center(130))
     print('\033[93m3. Digite no formato: Operando1OperaçãoOperando2 (exemplo: 3+4).'.center(130))
     print('\033[93m4. Não use espaços ou caracteres especiais fora dos listados.'.center(130))
     print('\033[93m5. Para sair da calculadora, digite -1.\033[0m'.center(130))
     print("\033[95m=\033[0m" * 120)
     os.system("pause")
    
    elif r == '3':
      os.system('cls')
      print('\033[95m')
      print('\033[94m   Historico  \033[95m'.center(130,'='))

      with open("historico.txt", "r") as arquivo:
         for linha in arquivo:
           conteudo = linha.strip()
           print('\033[93m{}\033[0m'.format(conteudo).center(130))

      os.system("pause")





    
    elif r == '4':
        print('\033[91mEncerrando a calculadora....\033[0m'.center(120))
        os.system("pause")
        break
    else:
        print('\n')
        print('\033[91mDigite uma opção de 1 a 3!\033[0m'.center(120))
        print('\n')
        os.system("pause")

    os.system('cls')



    

