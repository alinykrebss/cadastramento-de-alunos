'''
Crie uma aplicação Python que tera uma lista de alunos, com as notas de b1 e b2, um menu para selecionar a opção

1 - adicionar aluno
2 - listar aluno
3 - remover aluno
4 - procurar aluno
5 - aprovados
6 - reprovados
7 - Procurar pelo nome do aluno
8 - Média da turma B1
9 - Média da turma B2
10 - Média da turma GERAL
11 - Diário da turma
0 - sair

para o item 11 deve:Deve imprimir na tela neste padrão exatamente, com os alinhamentos igual ao exemplo abaixo:
Total linha: 56 colunas
RA: 5 CARACTERES
Nome: 27 CARACTERES
B1, B2, Média: 5 CARACTERES CADA
DICA: var.ljust(QTD, CHAR) | var.rjust(QTD, CHAR)

--------------------------------------------------------
                   Diario da turma
--------------------------------------------------------
RA    Nome                      Nota B1  Nota B2   Média
--------------------------------------------------------
00001 Aluno fulano de tal         10.00    10.00   10.00
00001 Aluno fulano de tal         10.00    10.00   10.00
00001 Aluno fulano de tal         10.00    10.00   10.00
00001 Aluno fulano de tal         10.00    10.00   10.00
--------------------------------------------------------
                  Médias da Turma 10.00    10.00   10.00
--------------------------------------------------------

'''
alunos = {}

def menu():
    print("1 - adicionar aluno")
    print("2 - listar aluno")
    print("3 - remover aluno")
    print("4 - procurar aluno")
    print("5 - aprovados")
    print("6 - reprovados")
    print("7 - procurar pelo nome do aluno")
    print("8 - media da turma B1")
    print("9 - media da turma B2")
    print("10 - media GERAL")
    print("11 - diario da turma")
    print("0 - sair")
    try:
        opt = int(input("selecione a opção: "))
        return opt

    #except KeyboardInterrupt:
     #   print("deu pau no teclado")
    
    #except ValueError:
       # print("numero digitado errado, burro")

    except Exception as e:
        print("inválido: {e} ")
        return 9
    #finally:
     #   print("mostra isso!")

def add_aluno():
    try:
        ra = input("digite o RA do aluno: ")
        nome = input("informe o nome: ")
        notab1 = float(input("informe a nota da B1: "))
        notab2 = float(input("informe a nota da B2: "))
        dados = {"nome": nome, "b1": notab1, "b2": notab2}
        alunos[ra] = dados
    except Exception as e:
        print("algo foi digitado errado {e}")

def listar_aluno():
    for ra, dados in alunos.items():
        print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2:{dados['b2']}")
    input("fecha os olhos e clica em qualquer lugar, para continuar ")

def remover_aluno():
    ra = input("digite o RA do aluno: ")
    if ra in alunos:
        aluno = alunos.pop(ra)
        print(f"o aluno:{aluno['nome']} foi removido")
    else:
        print("o aluno não foi en contrado")
    input("fecha os olhos e clica em qualquer lugar, para continuar ")    

def procurar_aluno():
   ra = input('digite o RA do aluno: ')
   if ra in alunos:
      dados = alunos[ra]
      print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2:{dados['b2']}")
   else:
      print('aluno não encontrado')
      input('fecha os olhos e clica em qualquer lugar, para continuar ')

def aprovados():
    for ra, dados in alunos.items():
       if ((dados['b1'] + dados['b2']) / 2) >= 7.0:
            aluno = f'RA: {ra} - '
            aluno += f"Nome: {dados['nome']} - "
            aluno += f"B1: {dados['b1']} - "
            aluno += f"B2: {dados['b2']}"
            print(aluno)
    input("fecha os olhos e clica em qualquer lugar, para continuar ")

def reprovados():
    for ra, dados in alunos.items():
        if ((dados['b1'] + dados['b2']) / 2) < 7.0:
            aluno = f'RA: {ra} - '
            aluno += f"Nome: {dados['nome']} - "
            aluno += f"B1: {dados['b1']} - "
            aluno += f"B2: {dados['b2']}"
            print(aluno)
    input("fecha os olhos e clica em qualquer lugar, para continuar ")

def procurar_nome():
  nome = input('digite o nome do aluno')
  nome = nome.upper
  for ra, dados in alunos.items():
     if (dados['nome'].upper() == nome):
      aluno = f"RA: {ra} - "
      aluno += f"Nome: {dados['nome']}"
      aluno += f"B1: {dados['b1']}"
      aluno += f"B2: {dados['b2']}"
      print(aluno)
      break
     input('pressione qualquer tecla para continuar: ')

def media_turma_b1():
    if alunos:
        soma = 0
        contador = 0
        for dados in alunos.values():
            soma += dados['b1']
            contador += 1
        media = soma / contador
        print(f"Média da turma em B1: {media:.2f}")# para formatar 2 casas decimais 
    
    input("fecha os olhos e clica em qualquer lugar, para continuar")

def media_turma_B2():
    if alunos:
        soma = 0
        contador = 0
        for dados in alunos.values():
            soma += dados['b2']
            contador += 1
        media = soma / contador
        print(f"Média da turma em B2: {media:.2f}")
    
    input("fecha os olhos e clica em qualquer lugar, para continuar")

def media_geral():
    if alunos:
        soma = 0
        contador = 0
        for dados in alunos.values():
            soma += (dados['b1'] + dados['b2']) / 2
            contador += 1
        media = soma / contador
        print(f"Média geral da turma: {media:.2f}")
    
    input("fecha os olhos e clica em qualquer lugar, para continuar")

def diario_da_turma():
    c1 =("-") 
    print(c1.ljust(56, "-"))
    print("                  Diário da turma")
    print(c1.ljust(56, "-"))
    print("RA    Nome                      Nota B1  Nota B2  Média")
    print(c1.ljust(56, "-"))
    
    soma_b1 = soma_b2 = soma_geral = 0
    contador = 0
    
    for ra, dados in alunos.items():
        media = (dados['b1'] + dados['b2']) / 2
        soma_b1 += dados['b1']
        soma_b2 += dados['b2']
        soma_geral += media
        contador += 1
        print(f"{ra.ljust(5)} {dados['nome'].ljust(27)} {str(dados['b1']).rjust(5)}  {str(dados['b2']).rjust(5)}   {str(media).rjust(5)}")
    
    if contador > 0:
        media_b1 = soma_b1 / contador
        media_b2 = soma_b2 / contador
        media_geral = soma_geral / contador
    else:
        media_b1 = media_b2 = media_geral = 0
    
    print(c1.ljust(56, "-"))
    print(f"{'Médias da Turma'.ljust(32)}  {str(media_b1).rjust(5)}  {str(media_b2).rjust(5)}   {str(media_geral).rjust(5)}")
    print(c1.ljust(56, "-"))
    input("fecha os olhos e clica em qualquer lugar, para continuar ") 


if __name__ == '__main__':
    while True:
        match menu():
            case 1:
                add_aluno()
            case 2:
                listar_aluno()
            case 3:
                remover_aluno()
            case 4:
                procurar_aluno()
            case 5:
                aprovados()
            case 6:
                reprovados()
            case 7:
                procurar_nome() 
            case 8:
                media_turma_b1()       
            case 9:
                media_turma_B2()
            case 10:
                media_geral()
            case 11:
                diario_da_turma()
            case 0:
                break
