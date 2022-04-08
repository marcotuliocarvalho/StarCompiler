import utils

float mult(float a,float b){
    # retorna a multiplicação de a e b
    return a * b;
}

int main(){

    #repeat que funciona como um for
    repeat(int count = 0;count < 10; count++)
        log(count);
    
    #repeat funciona como while
    int count = 0;
    repeat(count++<10)
        log(count)
    
    #declarando um literal
    string str = "Testando a string";

    int count = 0;
    repeat(count++ < 10)
        log(count);
    
    float _a = 1f, _b = 12., _c = 9;
    log(mult(_a,_b));
    
    return 0;
}

