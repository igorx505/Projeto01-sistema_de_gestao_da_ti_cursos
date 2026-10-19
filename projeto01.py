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

            while idade < 16:
                print(f"Você possui {idade} anos.")
                print("REQUISITO MINIMO: 16 ANOS")
                idade = int(input("Informe sua idade novamente: "))
            print("\n""\n")

            nome_completo = str(input("Informe seu nome completo: "))
            print("\n""\n")

            print("Selecione o turno\n")
            print("1 - Manhã | 2 - Noite\n")

            turno = int(input("->"))
            if turno == 1:
                turno = "1 - Manha"
            elif turno == 2:
                turno = "2 - Noite"
            print("\n""\n")

            print("Informe seu sexo\n")
            print("1 - Feminino | 2 - Masculino\n")
            sexo = int(input("->"))
            if sexo == 1:
                sexo = "1 - Feminino"
            elif sexo == 2:
                sexo = "2 - Masculino"
            elif sexo != 1 or 2:
                 print("Opção incorreta")
            print("\n""\n")
                 
            print("Informe o curso que deseja fazer:\n")
            print("1 - PHP | 2 - Java | 3 - Python\n")
            curso_1 = int(input("->"))

            if curso_1 == 1:
                 curso_1 = "1 - PHP"
            elif curso_1 == 2:
                 curso_1 = "2 - Java"
            elif curso_1 == 3:
                 curso_1 = "3 - Python"
            else:
                print("Informe uma das opções acima\n")

            print("Deseja adicionar mais um curso?\n" \
                  "1 - Sim | 2 - Não\n")

            novo_curso = int(input("->"))

            if novo_curso == 1:
                if curso_1 =="1 - PHP":
                    print("Informe o curso que deseja fazer:\n")
                    print("2 - Java | 3 - Python\n")
                    curso_2 = int(input("->"))
                    if curso_2 == 2:
                        curso_2 = "2 - Java"
                    elif curso_2 == 3:
                        curso_2 = "3 - Python"
                    elif curso_2 != 1 or 2 or 3:
                        print("Informe uma das opções acima\n")
                if curso_1 =="2 - Java":
                    print("Informe o curso que deseja fazer:\n")
                    print("1 - PHP | 3 - Python\n")
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
                    if curso_2 == 2:
                        curso_2 = "1 - PHP"
                    elif curso_2 == 3:
                        curso_2 = "2 - Java"
                    elif curso_2 != 2 or 3:
                        print("Informe uma das opções acima\n")
            else:
                curso_2 = "0 - N/A"


            novo_usuario = {
                    'matricula': matricula,
                    'nome': nome_completo,
                    'sexo': sexo,
                    'idade': idade,
                    'turno': turno,
                    'curso_1': curso_1,
                    'curso_2' : curso_2,
            }

            for chave,valor in novo_usuario.items():
                 print(f"{chave.capitalize()}: {valor}")

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
                                         f" Curso(2): {novo_usuario['curso_2']}\n"
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