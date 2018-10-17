Tomás Gueiros Souza Manzi, BCC 2018-2

# Lista de Exercícios 2 - 2018-2

===>>> Entrega: Até às 23h59 da Quarta-Feira, 17 de Outubro <<<===

Para esta lista você precisará escrever 4 programas que devem ser salvos independentemente como seu próprio arquivo ".py". O nome do arquivo que você deve usar para cada programa deve seguir este padrão:

>> questao_X.py

Onde o X no final é o número da questão.

Os arquivos que devem ser usados para a resolução de cada questão já foram criados na pasta /questoes. Cada arquivo contém um comentário com a descrição do problema a ser resolvido.
As respostas das questões devem ser desenvolvidas dentro da função main() de cada arquivo!!! Deve-se substituir o comado print existente pelo código da solução. 
IMPORTANTE: Para a correta execução do programa, a estrutura atual deve ser mantida, substituindo apenas o comando print(questão...) existente!!! 

Para testar o código cada questão separadamente, o arquivo da questão pode ser executado na sua IDE de preferência. Recomenda-se o uso do IDLE.

Para testar todas as questões de forma conjunta, o arquivo main.py pode ser executado. Na execução, siga as instruções inserindo o número da questão quando for solicitado e assim o código contido na função main() da referida questão será chamado.

Quando terminar, salve as alteraçes nos arquivos das questões. Então faça o push dessas alterações para o seu repositório no git classroom referente a esta tarefa. Este push será a submissão da sua resposta. Você pode submeter as respostas quantas vezes desejar... apenas o último push será considerado.

QUALQUER DÚVIDA SOBRE O USO DO GIT, PROCURAR OTACÍLIO MAIA.

Certifique-se de ler os problemas cuidadosamente e certifique-se de entender claramente a especificação completa de cada parte da tarefa. Faça cada parte conforme especificado.

Use nomes e comentários de variável significativos para explicar o que seu código está fazendo.

Teste seu código! Experimente diferentes conjuntos de valores de entrada para garantir que seu programa faça a coisa certa em diferentes casos.

NÃO ESQUEÇA DE MANTER A ESTRUTURA DE ARQUIVOS E PASTAS INALTERADA. ALTERE APENAS O CONTEÚDO DOS ARQUIVOS DAS QUESTÕES E SALVE COM O MESMO NOME. ISSO GARANTIRÁ A CORRETA EXECUÇÃO DOS TESTES APÓS A SUBMISSÃO. O PROFESSOR AGRADECE.

IMPORTANTE: Receba as entradas e imprima os resultados EXATAMENTE conforme solicitado. Caso os os formatos de entrada e saída não estejam conforme solicitado, os testes falharão e a nota para a questão não será computada.


-----------------------------------------------------------------------------------------------------------

## QUESTÃO 1 ##
Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
A seguir estão os critérios para verificar a senha:

1. Pelo menos uma letra entre [a-z]
2. Pelo menos 1 número entre [0-9]
3. Pelo menos uma letra entre [A-Z]
4. Pelo menos 1 caractere de [$ # @]
5. Comprimento mínimo da senha: 6
6. Comprimento máximo da senha: 12
<br/>
Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser impressas, separadas por uma vírgula.<br/>
Exemplo:<br/>
Se as seguintes senhas forem fornecidas como entrada para o programa:<br/>
 ABd1234@1, umF1#, 2w3E*, 2We3345<br/>
Então, a saída do programa deve ser:<br/>
 ABd1234@1<br/>


## QUESTÃO 2 ##
Um robô se move em um plano a partir do ponto original (0,0). O robô pode se mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:<br/>

CIMA 5\
BAIXO 3\
ESQUERDA 3\
DIREITA 2<br/>

Os números após a direção são passos. Escreva um programa para calcular a distância entre a posição atual e o ponto original após uma seqüência de movimentos. Se a distância for um float, basta imprimir o inteiro mais próximo.<br/>
Exemplo:<br/>
Se as seguintes tuplas são dadas como entrada para o programa:<br/>

CIMA 5\
BAIXO 3\
ESQUERDA 3\
DIREITA 2<br/>

Então, a saída do programa deve ser:<br/>
2<br/>
 
Dicas:<br/>
As entradas devem ser lidas do console até que um valor vazio seja digitado. A saída deve ser um inteiro que representa a distancia para o ponto original. Entradas inválidas devem ser descartadas da contagem.


## QUESTÃO 3 ##
Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.<br/>
 
A cifra de César é uma simples cifra de deslocamento que se baseia na transposição de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. A letra é deslocada para tantos valores quanto o valor da chave.<br/>

A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.<br/>

Um ROT13 no alfabeto latino seria o seguinte:<br/>
Normal: abcdefghijklmnopqrstuvwxyz\
Cifrado: nopqrstuvwxyzabcdefghijklm<br/>

Exemplos:<br/>
Entrada: ROT5 omg 
 Saída: trl<br/>
Entrada: ROT0 c 
 Saída: c<br/>
Entrada: ROT26 Cool 
 Saída: Cool<br/>
Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
 Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.<br/>
Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
 Saída: The quick brown fox jumps over the lazy dog.<br/>

Se um valor de entrada inválido for digitado, a seguinte mensagem deve ser impressa: 'Erro'. Entradas inválidas podem ser entradas que contém códigos de rotações inválidos ou mensagens contendo caracteres que não estão no alfabeto.<br/>
Exemplos:<br/>
Entrada: RARA abc Saída: Erro\
Entrada: ROT5 c99 Saída: Erro<br/>

As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.


## QUESTÃO 4 ##
 Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
 Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
 deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
 indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
 será inserida em formato numérico com três instruções de entrada separadas; 
 uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
 funciona corretamente para anos bissextos.
