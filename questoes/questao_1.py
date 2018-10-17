## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234@1, umF1#, 2w3E*, 2We3345
# Então, a saída do programa deve ser:
# ABd1234@1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    sequencia = str(input("digite uma sequencia de senhas separadas por virgula: "))
    tamseq = len(sequencia) # inicia uma variavel tamseq que vai guardar o tamanho de caracteres da sequencia
    n = int(0) # inicia uma variavel n para utilizar no while como contador
    n1 = int(0) # inicia uma variavel n1 para utilizar no segundo while como contador 
    insenha = int(0) # inicia uma variavel que vai guardar a posicao inicial da ultima senha na sequencia
    primeiravirgula = bool(False) # variavel para garantir que nao seja impressa uma virgula apos a primeira senha caso ela seja a unica senha que sera retornada
    contemaz = bool(False) 
    contem09 = bool(False)
    contemAZ = bool(False)
    contemespecial = bool(False)
    while (n < tamseq):
        if sequencia[n] == ",":
            if len(sequencia[insenha:n]) >= 6 and len(sequencia[insenha:n]) <= 12:
                n1 = insenha
                while (n1 < n):
                    if (sequencia[n1].isalpha() == True) and (sequencia[n1].islower() == True):
                        contemaz = True
                    if (sequencia[n1].isalpha() == True) and (sequencia[n1].isupper() == True):
                        contemAZ = True
                    if (sequencia[n1].isdigit() == True):
                        contem09 = True
                    if (sequencia[n1] == "@") or (sequencia[n1] == "#") or (sequencia[n1] == "$"):
                        contemespecial = True
                    n1 = n1 + 1
                if (contemaz == True) and (contem09 == True) and (contemAZ == True) and (contemespecial == True):
                    if primeiravirgula == False:
                        primeiravirgula = True
                        print(sequencia[insenha:n], end="") 
                    else:
                        print(", " + (sequencia[insenha:n]), end="")   
                insenha = n+2 # o inicio da proxima senha eh duas casas depois da virgula (que no momento eh 'n')
        contemaz = False
        contem09 = False
        contemAZ = False
        contemespecial = False        
        n = n + 1
        if n == tamseq: 
            if len(sequencia[insenha:n]) >= 6 and len(sequencia[insenha:n]) <= 12:
                n1 = insenha
                while (n1 < n):
                    if (sequencia[n1].isalpha() == True) and (sequencia[n1].islower() == True):
                        contemaz = True
                    if (sequencia[n1].isalpha() == True) and (sequencia[n1].isupper() == True):
                        contemAZ = True
                    if (sequencia[n1].isdigit() == True):
                        contem09 = True
                    if (sequencia[n1] == "@") or (sequencia[n1] == "#") or (sequencia[n1] == "$"):
                        contemespecial = True
                    n1 = n1 + 1
                if (contemaz == True) and (contem09 == True) and (contemAZ == True) and (contemespecial == True):
                    if primeiravirgula == False:
                        print(sequencia[insenha:n]) 
                    else:
                        print(", " + (sequencia[insenha:n]))  
    


if __name__ == '__main__':
    main()
