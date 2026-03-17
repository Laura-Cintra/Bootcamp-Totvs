# input é uma função que recebe um argumento string, exibe esse argumento no terminal e espera o usuário apertar enter
nome = input("Informe o seu nome: ")
print("Olá, " + nome + "!")

# print é uma função que recebe um argumento e o exibe no terminal
nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome) # imprime o nome e o sobrenome separados por um espaço
print(nome, sobrenome, end="...\n") # imprime o nome e o sobrenome separados por reticências, e depois pula para a próxima linha
print(nome, sobrenome, sep="#") # imprime o nome e o sobrenome separados por um #, e depois pula para a próxima linhas

# Guilherme Carvalho
# Guilherme...Carvalho
# Guilherme#Carvalhos