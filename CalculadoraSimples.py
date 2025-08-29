import os

while 1:
    print("\033[95m=" * 120)
    print('\033[96mCalculadora py\033[0m'.center(121))
    print("\033[95m=" * 120)
    print('\n')

    print('\033[93m1- Calculadora'.center(119))
    print('\033[93m2- Manual de uso'.center(119))
    print('\033[93m3- Encerrar\033[0m'.center(119))


    r = input("\033[92mEscolha: \033[0m")

    if r.isalpha():
       print("\033[91mDigite uma opção de 1 a 3!\033[0m".center(120))
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

           if len(operacao) > 3 or len(operacao) < 3 :
              print("\033[91mVc digitou errado! Digite no modelo Operando1-Sinal-Operando2, exemplo:3+4!\033[0m".center(120))
              os.system("pause")
              os.system('cls')
              
              continue
           
           sinal = operacao[1]
           op1 = operacao[0]
           op2 = operacao[2]

         
           if not (op1.isdigit() and op2.isdigit()):
              print("\033[91mOs operandos precisam ser números!\033[0m".center(120))
              os.system("pause")
              os.system('cls')
              continue
           else:
               op1 = int(operacao[0])
               op2 = int(operacao[2])
               break

          if operacao == '-1':
               print('Saindo da calculadora...'.center(120))
               break
          

          if sinal == '+':
              print("\033[92mResposta: {}\033[0m".format(op1 + op2 ).center(20) )

          elif sinal == '-':
              print("\033[92mResposta: {}\033[0m".format(op1 - op2).center(20))

          elif sinal == '/':
              print("\033[92mResposta:{}\033[0m".format(op1 / op2).center(20))

          elif sinal == '*':
              print("\033[92mResposta:{}\033[0m".format(op1 * op2).center(20))

          elif sinal == '^':
              print("\033[92mResposta:{}\033[0m".format(op1 ** op2).center(20))

          elif sinal == '%':
              print("\033[92mResposta:{}\033[0m".format(op1 % op2).center(20))
          else:
              print('\033[91mSinal invalido!\033[0m'.center(120))
              
          os.system("pause")
          os.system('cls')
        
        os.system("pause")
        os.system('cls')


    
    elif r == '2':
     os.system('cls')
     print("=" * 20,'Manual de Uso', "=" * 20)
     print('Bem-vindo à calculadora!'.center(50))
     print('Regras para digitar corretamente as operações:'.center(50))
     print('1. Digite apenas números de 0 a 9 como operandos.'.center(50))
     print('2. Escolha apenas uma operação por vez:'.center(50))
     print('   Soma (+), Subtração (-), Multiplicação (*), Divisão (/), Resto de Divisão (%), Potência (^).'.center(50))
     print('3. Digite no formato: Operando1OperaçãoOperando2 (exemplo: 3+4).')
     print('4. Não use espaços ou caracteres especiais fora dos listados.')
     print('5. Para sair da calculadora, digite -1.'.center(50))
     print("=" * 50)
     os.system("pause")
  
    
    elif r == '3':
        print('\033[91mEncerrando a calculadora....\033[0m'.center(120))
        os.system("pause")
        break
    else:
        print('\n')
        print('\033[91mDigite uma opção de 1 a 3!\033[0m'.center(120))
        print('\n')
        os.system("pause")

    os.system('cls'.center(120))



    

