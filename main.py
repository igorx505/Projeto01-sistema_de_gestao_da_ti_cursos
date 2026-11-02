import time

# 0 - INTRODUÇÃO DO PROGRAMA
print("="*30)
print("\n","SEJA BEM-VINDO AO PROJETO 01\n")
print("="*30)
print("Alunos: Igor Farias,Igor Muller, Ledine Costa e Thomas Tavares \n""\n""\n""\n")
time.sleep(2)
# 1 - BOOL PARA DEIXAR RODANDO
rodando = True

# 2 - WHILE PARA MANTER RODANDO AS OPÇÕES

while rodando is True:
        # 3 - PRINT DAS INFORMAÇÕES 
        print("=-="*10)
        print("PAINEL DE ATIVIDADES")
        print("=-="*10)
        print("\n","\n","INFORME O NÚMERO DA OPÇÃO ABAIXO:")
        print(
            "1 - CADASTRAR ALUNO\n"
            "2 - EDITAR ALUNO\n"
            "3 - LISTAGEM\n"
            "0 - Sair do programa\n")
        opcao = int(input("OPÇÃO -> "))

        if opcao == 1:

            print("VOCÊ ESCOLHEU 1 - CADASTRAR ALUNO")

            time.sleep(1)

            print("Iniciando fluxo de NOVO CADASTRO...")


            with open("banco_de_dados.txt", "r", encoding="utf-8") as matri:
                  line = matri.readlines()

                    
                  if line:
                        last_line = line[-1]
                        divide_id = last_line.split(" | ")[0]
                        last_id = divide_id.split(":")[1].strip()

                        new_id = str(int(last_id) + 1)
                  else:
                        new_id = 1600001


            matricula = new_id
            print("\n""\n")

            idade = int(input("Informe sua idade: "))

            while idade < 16 or idade > 86:
                print(f"Você possui {idade} anos.")
                print("REQUISITO MINIMO: 16 ANOS | MÁXIMO: 86 ANOS")
                idade = int(input("Informe sua idade novamente: "))
            print("\n""\n")

            nome_completo = str(input("Informe seu nome completo: "))
            print("\n""\n")

            time.sleep(1)

            print("Informe seu sexo\n")
            print("1 - Feminino | 2 - Masculino\n")
            sexo = int(input("->"))

            while sexo not in [1, 2]:
                 print("Informe uma das opções.\n")
                 print("1 - Feminino | 2 - Masculino\n")
                 sexo = int(input("->"))
            
            if sexo == 1:
                sexo = "1 - Feminino"
            elif sexo == 2:
                sexo = "2 - Masculino"

            print("\n""\n")

            time.sleep(1) 

            print("Informe o curso que deseja fazer:\n")
            print("1 - PHP | 2 - Java | 3 - Python\n")
            curso_1 = int(input("->"))
            print("\n""\n")
            while curso_1 not in [1, 2, 3]:
                 print("Informe uma das opções.\n")
                 print("Informe o curso que deseja fazer:\n")
                 print("1 - PHP | 2 - Java | 3 - Python\n")
                 curso_1 = int(input("->"))

            if curso_1 == 1:
                 curso_1 = "1 - PHP"
            elif curso_1 == 2:
                 curso_1 = "2 - Java"
            elif curso_1 == 3:
                 curso_1 = "3 - Python"

            print("\n""\n")

            print("Deseja adicionar mais um curso?\n" \
                  "1 - Sim | 2 - Não\n")

            novo_curso = int(input("->"))

            while novo_curso not in [1,2]:
                 print("Informe uma das opções acima\n")
                 print("Deseja adicionar mais um curso?\n" \
                  "1 - Sim | 2 - Não\n")
                 novo_curso = int(input("->"))
            print("\n""\n")
            if novo_curso == 1:

                
                if curso_1 =="1 - PHP":
                    print("Informe o curso que deseja fazer:\n")
                    print("2 - Java | 3 - Python\n")
                    
                    curso_2 = int(input("->"))
                    while curso_2 not in [2, 3]:
                         print("Informe uma das opções.\n")
                         print("2 - Java | 3 - Python\n")
                         curso_2 = int(input("->")) 
                    if curso_2 == 2:
                        curso_2 = "2 - Java"
                    elif curso_2 == 3:
                        curso_2 = "3 - Python"



                if curso_1 =="2 - Java":
                    print("Informe o curso que deseja fazer:\n")
                    print("1 - PHP | 3 - Python\n")
                    curso_2 = int(input("->"))
                    while curso_2 not in [ 1, 3]:
                         print("1 - PHP | 3 - Python\n")
                         print("Informe uma das opções acima\n")
                         curso_2 = int(input("->"))
                         
                    if curso_2 == 2:
                        curso_2 = "1 - PHP"
                    elif curso_2 == 3:
                        curso_2 = "3 - Python"
                    elif curso_2 != 2 or 3:
                        print("Informe uma das opções acima\n")



                if curso_1 =="3 - Python":
                    print("Informe o curso que deseja fazer:\n")
                    print("1 - PHP | 2 - Java\n")
                    curso_2 = int(input("->"))
                    while curso_2 not in [ 1, 2]:
                        print("Informe uma das opções.\n")
                        print("1 - PHP | 2 - Java\n")
                        curso_2 = int(input("->"))
                    if curso_2 == 2:
                        curso_2 = "1 - PHP"
                    elif curso_2 == 3:
                        curso_2 = "2 - Java"
                    elif curso_2 != 2 or 3:
                        print("Informe uma das opções acima\n")



            else:
                curso_2 = "0 - N/A"


            print("\n""\n")
            time.sleep(1)


            print("Selecione o turno\n")
            print("1 - Manhã | 2 - Noite\n")

            turno = int(input("->"))
            while turno not in [ 1, 2]:
                 print("Informe uma das opções.\n")
                 print("1 - Manhã | 2 - Noite\n")
                 turno = int(input("->"))
                 
            time.sleep(1)
            #VALOR DOS CURSOS
            print("\n""\n")
            cursos_dia = [{"1 - PHP": 210}, {"2 - Java": 320}, {"3 - Python": 290}]
            cursos_noite = [{"1 - PHP": 260}, {"2 - Java": 390}, {"3 - Python": 310}]

            mensalidade = 0
            valor_c2 = 0

            if turno == 1:
                    tabela_cursos = cursos_dia
                    turno_texto = "1 - Manha"
            else:
                 tabela_cursos = cursos_noite
                 turno_texto = "2 - Noite"

            indice_c1 = int(curso_1.split(" - ")[0]) - 1

            nome_curso, valor_c1 = next(iter(tabela_cursos[indice_c1].items()))

            mensalidade = valor_c1

            if curso_2 == "0 - N/A" or curso_2 == 0:
                pass
            else:
                 indice_c2  = int(curso_2.split(" - ")[0]) - 1
                 nome_curso, valor_c2 = next(iter(tabela_cursos[indice_c2].items()))
                 valor_c2 = int(valor_c2)
                 mensalidade += valor_c2

            desconto = 0.0


            if idade >= 45 and valor_c2 != 0:
                 desconto = mensalidade * 0.30
            elif idade >= 45:
                 desconto = mensalidade * 0.15
            elif valor_c2 > 0:
                 desconto = mensalidade * 0.30
            else:
                 pass

            if desconto >0 :
                 mensalidade = mensalidade-desconto


            novo_usuario = {
                    'matricula': matricula,
                    'nome': nome_completo,
                    'sexo': sexo,
                    'idade': idade,
                    'turno': turno_texto,
                    'curso_1': curso_1,
                    'curso_2': curso_2,
                    'mensalidade(R$)': mensalidade
            }

            for chave,valor in novo_usuario.items():
                 print(f"{chave.capitalize()}: {valor}")
            time.sleep(1)
            print("Deseja confirmar as informações?\n" \
            "1 - Sim | 2 - Não\n")
            resposta = int(input("->"))

            if resposta == 1:

                linha_para_salvar = (f"Matricula: {novo_usuario['matricula']} |"
                                         f" Nome: {novo_usuario['nome']} |"
                                         f" Sexo: {novo_usuario['sexo']} |"
                                         f" Idade: {novo_usuario['idade']} |"
                                         f" Turno: {novo_usuario['turno']} |"
                                         f" Curso(1): {novo_usuario['curso_1']} |"                                         
                                         f" Curso(2): {novo_usuario['curso_2']} |"
                                         f" Mensalidade(R$): {novo_usuario['mensalidade(R$)']}\n"
                                         ) 
                with open("banco_de_dados.txt", "a") as arquivo:
                        arquivo.write(linha_para_salvar)
                print("CADASTRO REALIZADO COM SUCESSO")
            else:
                print("\n""\n")
                print("CADASTRO CANCELADO!")
                print("\n""\n")
                time.sleep(2)

                
        elif opcao == 2:
            print("VOCÊ ESCOLHEU 2 - EDITAR ALUNO")
            time.sleep(2)
        elif opcao == 3:
            print("VOCÊ ESCOLHEU 3 - LISTAGEM")
            time.sleep(2)
        elif opcao == 0:
            print("FECHANDO... 3... 2... 1...")
            time.sleep(3)
            rodando = False
        elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 0:
            print("Opção inválida. Tente novamente.")
