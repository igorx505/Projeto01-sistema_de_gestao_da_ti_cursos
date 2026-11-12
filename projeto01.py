import time

# EDIÇÃO E REMOÇÃO DE ALUNOS (funções usadas pela opção 2 do menu)

arquivo_banco = "banco_de_dados.txt"
encoding = "utf-8"

cursos_disponiveis = {1: "PHP", 2: "Java", 3: "Python"}
sexos = {1: "1 - Feminino", 2: "2 - Masculino"}
turnos = {1: "1 - Manha", 2: "2 - Noite"}

# preços[turno][curso]
precos = {
    1: {1: 210, 2: 320, 3: 290},
    2: {1: 260, 2: 390, 3: 310},
}

campos = ["Matricula", "Nome", "Sexo", "Idade", "Turno",
          "Curso(1)", "Curso(2)", "Mensalidade(R$)"]

matricula_inicial = 1600001
max_cursos = 2



# leitura e gravação do arquivo

def ler_registros():
    try:
        with open(arquivo_banco, "r", encoding=encoding) as arq:
            linhas = arq.readlines()
    except FileNotFoundError:
        return []

    registros = []
    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        aluno = {}
        for pedaco in linha.split(" | "):
            if ":" in pedaco:
                chave, valor = pedaco.split(":", 1)
                aluno[chave.strip()] = valor.strip()
        if "Matricula" in aluno:
            registros.append(aluno)
    return registros


def formatar_linha(aluno):
    return " | ".join(f"{campo}: {aluno[campo]}" for campo in campos)


def salvar_registros(registros):
    with open(arquivo_banco, "w", encoding=encoding) as arq:
        for aluno in registros:
            arq.write(formatar_linha(aluno) + "\n")


# entrada de dados com validação
def ler_numero(mensagem, validos, aviso="Opção inválida. Tente novamente."):
    while True:
        texto = input(mensagem).strip()
        if texto.isdigit() and int(texto) in validos:
            return int(texto)
        print(aviso)


def ler_nome():
    while True:
        nome = input("Nome completo: ").strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")


def ler_cursos():
    escolhidos = []
    while True:
        livres = [c for c in cursos_disponiveis if c not in escolhidos]
        opcoes = " | ".join(f"{c} - {cursos_disponiveis[c]}" for c in livres)
        print(f"Cursos disponíveis: {opcoes}")
        escolhidos.append(ler_numero("Curso -> ", livres))

        if len(escolhidos) == max_cursos:
            break
        mais = ler_numero("Adicionar mais um curso? 1 - Sim | 2 - Não -> ", [1, 2])
        if mais == 2:
            break
    return escolhidos


# regras de negócio

def calcular_mensalidade(idade, turno, cursos):
    total = sum(precos[turno][c] for c in cursos)
    if len(cursos) > 1:
        percentual = 0.30
    elif idade >= 45:
        percentual = 0.15
    else:
        percentual = 0.0
    return round(total * (1 - percentual), 2)


def proxima_matricula(registros):
    numeros = [int(a["Matricula"]) for a in registros if a["Matricula"].isdigit()]
    return max(numeros) + 1 if numeros else matricula_inicial



# a busca e exibição
def mostrar_aluno(aluno):
    for campo in campos:
        print(f"  {campo}: {aluno[campo]}")


def escolher_aluno(registros):
    if not registros:
        print("\nNenhum aluno cadastrado.")
        return None

    termo = input("\nDigite o NOME ou a MATRÍCULA do aluno: ").strip().lower()

    achados = []
    if termo != "":
        achados = [a for a in registros if a["Matricula"] == termo]
        if not achados:
            achados = [a for a in registros if termo in a.get("Nome", "").lower()]

    if not achados:
        print("Nenhum aluno encontrado.")
        return None
    if len(achados) == 1:
        return achados[0]

    print(f"\n{len(achados)} alunos encontrados:")
    for i, aluno in enumerate(achados, start=1):
        print(f"  {i} - {aluno['Matricula']} | {aluno['Nome']}")
    escolha = ler_numero("Escolha o número do aluno (0 para cancelar) -> ",
                         range(0, len(achados) + 1))
    return None if escolha == 0 else achados[escolha - 1]



# ações do menu

def editar_aluno():
    print("\n--- EDITAR ALUNO ---")
    registros = ler_registros()
    aluno = escolher_aluno(registros)
    if aluno is None:
        return

    print("\nDados atuais:")
    mostrar_aluno(aluno)
    print("\nInforme os novos dados:\n")

    manter = ler_numero("Manter o número de matrícula? 1 - Sim | 2 - Não -> ", [1, 2])
    if manter == 1:
        matricula = aluno["Matricula"]
    else:
        matricula = str(proxima_matricula(registros))
        print(f"Nova matrícula gerada: {matricula}")

    idade = ler_numero("Idade (16 a 86): ", range(16, 87),
                       "Idade inválida. Requisito: mínimo 16 anos e máximo 86 anos.")

    nome = ler_nome()

    print("Sexo: 1 - Feminino | 2 - Masculino")
    sexo = ler_numero("-> ", sexos)

    cursos = ler_cursos()

    print("Turno: 1 - Manhã | 2 - Noite")
    turno = ler_numero("-> ", turnos)

    novo = {
        "Matricula": matricula,
        "Nome": nome,
        "Sexo": sexos[sexo],
        "Idade": str(idade),
        "Turno": turnos[turno],
        "Curso(1)": f"{cursos[0]} - {cursos_disponiveis[cursos[0]]}",
        "Curso(2)": f"{cursos[1]} - {cursos_disponiveis[cursos[1]]}" if len(cursos) > 1 else "0 - N/A",
        "Mensalidade(R$)": calcular_mensalidade(idade, turno, cursos),
    }

    print("\nNovos dados:")
    mostrar_aluno(novo)
    confirma = ler_numero("\nConfirmar alteração? 1 - Sim | 2 - Não -> ", [1, 2])
    if confirma == 2:
        print("Edição cancelada. Nada foi alterado.")
        return

    posicao = next(i for i, a in enumerate(registros) if a is aluno)
    if matricula == aluno["Matricula"]:
        registros[posicao] = novo
    else:
        # nova matrícula vai pro final do banco
        registros.pop(posicao)
        registros.append(novo)

    salvar_registros(registros)
    print("ALUNO EDITADO COM SUCESSO!")


def remover_aluno():
    print("\n--- REMOVER ALUNO ---")
    registros = ler_registros()
    aluno = escolher_aluno(registros)
    if aluno is None:
        return

    print("\nAluno encontrado:")
    mostrar_aluno(aluno)
    confirma = ler_numero("\nDeseja realmente REMOVER este aluno? 1 - Sim | 2 - Não -> ", [1, 2])
    if confirma == 2:
        print("Remoção cancelada. Nada foi alterado.")
        return

    registros = [a for a in registros if a is not aluno]
    salvar_registros(registros)
    print("ALUNO REMOVIDO COM SUCESSO!")


def menu_edicao():
    """Submenu: 1 - Editar | 2 - Remover | 3 - Voltar ao menu inicial."""
    while True:
        print("\n" + "=" * 40)
        print("   EDIÇÃO E REMOÇÃO DE ALUNOS")
        print("=" * 40)
        print("1 - Editar aluno")
        print("2 - Remover aluno")
        print("3 - Voltar ao menu inicial\n")

        opcao = ler_numero("OPÇÃO -> ", [1, 2, 3])

        if opcao == 1:
            editar_aluno()
        elif opcao == 2:
            remover_aluno()
        else:
            print("Voltando ao menu inicial...")
            return





print("="*30)
print("\n","SEJA BEM-VINDO AO PROJETO 01\n")
print("="*30)
print("Alunos: Igor Farias,Igor Muller, Ledine Lira e Thomas Tavares \n""\n""\n""\n")
time.sleep(2)

rodando = True
while rodando is True:

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
            menu_edicao()


        elif opcao == 3:
            print("VOCÊ ESCOLHEU 3 - LISTAGEM")

            time.sleep(1)
            print("Carregando lista de alunos...\n")
            time.sleep(1)

            try:
                with open("banco_de_dados.txt", "r", encoding="utf-8") as arquivo:
                    linhas = arquivo.readlines()

                    if not linhas:
                        print("Nenhum aluno cadastrado.\n")
                    else:
                        print("=" * 40)
                        print("     LISTA DE ALUNOS CADASTRADOS")
                        print("=" * 40)

                    for linha in linhas:
                        linha = linha.strip()
                        if linha != "":
                                 print(f" • {linha}")
                                 print("-" * 40)

            except FileNotFoundError:
                print("Arquivo de banco de dados ainda não foi criado.\n")
            print("\n")
            input("Pressione ENTER para voltar ao menu...")

            print("\n""\n")

            time.sleep(2)
        elif opcao == 0:
            print("FECHANDO... 3... 2... 1...")
            time.sleep(3)
            rodando = False
        elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 0:
            print("Opção inválida. Tente novamente.")
