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