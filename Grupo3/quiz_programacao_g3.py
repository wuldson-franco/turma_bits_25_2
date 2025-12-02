import os

print("=== QUIZ TEP GRUPO 3: INTRODUÇÃO À PROGRAMAÇÃO E HTML/CSS ===\n")

# Dados do aluno
nome = input("Nome completo: ").strip()
matricula = input("Matrícula: ").strip()

primeiro_nome = nome.split()[0].lower()

print("\nResponda as questões selecionando A, B, C ou D.\n")

# Perguntas e alternativas
questoes = {
    1: "1. Em programação, qual é a função do comando 'print' em Python?\nA) Criar variáveis\nB) Exibir informações na tela\nC) Repetir um bloco de código\nD) Encerrar o programa",
    2: "2. Em HTML, qual tag é usada para criar um parágrafo?\nA) <div>\nB) <span>\nC) <p>\nD) <text>",
    3: "3. Em CSS, qual propriedade altera a cor do texto?\nA) background-color\nB) font-weight\nC) text-size\nD) color",
    4: "4. Em programação, o que é uma variável?\nA) Um valor fixo e imutável\nB) Um espaço na memória para armazenar valores\nC) Um tipo de função\nD) Um erro no código"
}

# Gabarito
gabarito = {
    1: "B",
    2: "C",
    3: "D",
    4: "B"
}

respostas = {}
detalhes = ""
acertos = 0

# Coleta das respostas e validação
for n, pergunta in questoes.items():
    print("\n" + pergunta)
    resposta = input("Sua resposta: ").strip().upper()

    # Armazena a resposta
    respostas[n] = resposta
    correta = gabarito[n]

    # Verifica acerto
    if resposta == correta:
        acertos += 1
        detalhes += f"Questão {n}: ✔️ Correta\n"
    else:
        detalhes += f"Questão {n}: ❌ Errada (correta: {correta})\n"

# Monta resultado final
resultado = f"""
=== RESULTADO DO QUIZ ===

Aluno: {nome}
Matrícula: {matricula}

Acertos: {acertos} de {len(questoes)} questões

DETALHAMENTO:
{detalhes}

IMPORTANTE:
- Este resultado NÃO serve como nota oficial do curso.
- Faça o commit e push deste arquivo para o seu repositório no GitHub.
"""

# Nome do arquivo: primeiro_nome + matricula
nome_arquivo = f"{primeiro_nome}_{matricula}.txt"
caminho = os.path.join(os.getcwd(), nome_arquivo)

# Salva o arquivo
with open(caminho, "w", encoding="utf-8") as f:
    f.write(resultado)

print("\n=== QUIZ FINALIZADO ===")
print(f"Arquivo salvo em: {caminho}")
print("Relaxa, esse resultado NÃO representa nota oficial, é só pra saber se tu sabe mesmo.")
print("Agora, cuida e sobe o arquivo .txt gerado pro GitHub.")
print("E PELO AMOOOORRRR, lembra dos comandos... add, commit, push")