# Star Compiler

Star compiler foi feito utilizando a linguagem [Python](https://python.org.br/), sendo desenvolvido na matéria de Compiladores. Sua primeira versão contém apenas o analisador léxico, sendo o sintático o próximo.

## A Linguagem

 - [Imperativa](#imperativa)
 - [Condicionais](#condicionais)
 - [Repetições](#repetições)
 - [Case Sensitive](#case-sensitive)

### Palavras reservadas
 - repeat (estrutura de repetição)
 - do (utilizado para fazer um do-while, sendo do-repeat)
 - if (execução caso a condição de if seja  verdadeira)
 - elif (execução caso a condição de if seja falsa, e a do elif corrente seja verdadeira)
 - else (execução caso as condições de if e elif sejam falsas)
 - switch (condicionais para fluxo de execução, assim como if's, elif's e else's)
 - case (caso é utilizado dentro de switch, para verificar igualdade)
 - break (parar um loop, ou sair do switch)
 - continue (pular para a proxima interação da repetição)
 - return (retorna o valor de acordo com a função)
 - import (importa outro arquivo para dentro do arquivo corrente)
 - True (valor lógico verdadeiro)
 - False (valor logico falso)
 - const (define uma constante)
 - log (imprime na tela)
 
 ## Tipos
 
 - int (ex: 1)
 - float (ex:1.2)
 - void (retorno vazio)
 - char (ex:'c')
 - string (ex:)
 - bool (ex:True ou False)

### Imperativa
Baseado em instruções e comandos, o programador diz **como** e o **quê** exatamente um programa ou rotina deve realizar. É neste paradigma que surgiram os famosos laços de repetição, estruturas condicionais, atribuição de valor à variáveis e controle de estado. Instruções como **if**, **while**, **switch** e **for** são típicas de linguagens de programação imperativas.
Fonte: [Medium](https://medium.com/@alexandre.malavasi/descomplicando-programa%C3%A7%C3%A3o-imperativa-declarativa-e-reativa-a481baa87742)
### Condicionais
Para realizar um fluxo de código utilizar as condicionais pode ser uma boa boa opção, para isso utiliza-se [if](#if),[elif](#elif) e [else](#else). Caso a condição seja verdadeira, o bloco de codigo dentro da condicional será executado.

```
if (<condição>)
{
    # se a condição do if for verdadeiro entao executa o bloco de código
}
elif(<condição>)
{
    # será executado caso a condição do if seja False
    # e a condição do elif seja verdadeiro
}
else
{
    # se as outras condições forem False o código no else é executado
}
```
Outra importante estrutura é [switch](#switch) [case](#case), assemelhando-se às condicionais anteriormente apresentadas
```
switch(<identificador>)
{
    case <num/char/string>:
        # executa caso <identificador> == <num/char/string>
        break;
    default:
        # bloco padrão
        break;
}
```
### Repetições
Para realizar uma repetição utiliza-se a palavra reservada [repeat](#repeat) e também [do](#do), funciona como for e while em linguagens como C.
```
repeat(int i = 0; i < 10; i++)
{
    #funciona como um for
}

int i = 0;
repeat(i++ < 10)
{
    # funciona como while
}

int j = 0;
do
{
    #funciona como do while
}repeat(j++<10);
```
### Case Sensitive
Star é case sensitive, o que quer dizer que:
```
int Var = 0;
int var = 0;
# var e Var são duas variáveis distintas
```
Sendo assim letras em minúsculo e maiúsculo importam neste contexto.

## Exemplo de código em Star

```
import utils

int sum(int a, int b)
{
    return a+b;
}

float mult(float a, float b)
{
    return a*b;
}
string concat(string a, string b)
{
    return a+b;
}

int main()
{
    int var1 = 2,var2 = 4;
    
    log(sum(var1,var2));
    
    #ocorre um cast implícito
    log(mult(var1,var2));
    
    log(concat("Hello"," World"));
    
    repeat(int i = 0; i < 5;i++)
    {
        repeat(int j = 0; j < i;j++)
        {
            log("*");
        }
        log("/n");
    }
    
    switch(var1)
    {
        case 2:
            log(2);
            break;
        default:
            log("Não é dois\n");
    }
    
    if(var2 == 2)
    {
        log("var2 é igual a 2\n");
    }
    elif(var2 == 3)
    {
        log("var2 é igual a 3\n");
    }
    else
    {
        log("var2 não é igual a 3 e nem 2\n");
    }
}
```
