"""André, Carlos e Pietro são grandes amigos e jogam "Dois ou Um!" a toda hora: para determinar quem será o motorista da rodada,
quem vai pagar a conta etc. Jogam tanto que resolveram fazer um aplicativo de celular para jogar.
Como não sabem programar, dividiram as tarefas entre amigos que sabem, inclusive você.

Dados os três valores escolhidos por André, Carlos e Pietro, cada valor dois ou um, escreva um algoritmo que determina se há um ganhador,
e nesse caso determina quem é o ganhador.

O algoritmo deve receber como entrada, três valores inteiros
que serão armazenados nas variáveis A, C e P indicando os valores escolhidos por André, Carlos e Pietro, respectivamente.

O algoritmo deverá produzir uma única saída, imprimindo apenas um caractere.

Se o vencedor for André, deve-se imprimir a letra “A”, na tela;
se o vencedor for Carlos, é preciso mostrar o caractere “C”, na tela;
se Pietro for o ganhador, então deve-se imprimir “P”;
por fim, se não houver vencedor, deve-se imprimir um asterisco, “X”, na tela.

Deve-se considerar que o usuário é leigo, e nem sempre irá digitar ou o número dois (2) ou o número um (1).
É preciso que o algoritmo trate as entradas que não estiverem dentro do padrão de dois ou um,
solicitando ao usuário que insira um novo valor, caso ele não insira um dado válido (número 2 ou número 1).

Considere que o usuário tem acesso apenas ao teclado numérico, sendo impossível inserir caracteres alfabéticos,
acentos ou qualquer outro dado diferente de números.

Somente após validados os dados informados pelo usuário, o algoritmo deve apresentar o resultado e,
consequentemente, quem foi vitorioso, de acordo com a seguinte tabela de exemplos de entradas e saídas:

Caso
de
Teste	Entradas	Saída Correspondente
A
(André)	C
(Carlos)	P
(Pietro)	Ganhador:
1º	1	1	1	“X”
2º	1	1	2	“P”
3º	1	2	1	“C”
4º	1	2	2	“A”
5º	2	1	1	“A”
6º	2	1	2	“C”
7º	2	2	1	“P”
8º	2	2	2	“X”
"""



op = "s"

while op == "s":


    A = int(input("Digite 1 ou 2: \n"))
    B = int(input("Digite 1 ou 2: \n"))
    C = int(input("Digite 1 ou 2: \n"))

    if A != 1 and A != 2:
        print ("Digite apenas 1 ou 2")

    elif B != 1 and B != 2:
        print ("Digite apenas 1 ou 2")

    elif C != 1 and C != 2:
        print ("Digite apenas 1 ou 2")

    elif A == B == C:
        print ("X")

    elif A != C == B:
        print ("A")

    elif A == C != B:
        print ("B")

    elif A == B != C:
        print ("C")

    op = input("Deseja executar novamente? s/n?")
