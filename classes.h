#ifndef CLASSES_H_INCLUDED
#define CLASSES_H_INCLUDED

class Veiculo { // definição da classe pai;
public:
    int vel;
    int pass;
    int rodas;
    void setTipo (int tp);
    void setVelMax (int vm);
    void imp();
private:
    int tipo;
    int velMax;
};

void Veiculo::imp (){
    std::cout <<"Tipo veiculo...........: " << tipo << std::endl;
    std::cout <<"Velocidade maxima..........: " << velMax << std::endl;
    std::cout <<"Qtde rodas.............: " << rodas << std::endl;
    std::cout <<"Qtde passageiros..............: " << pass << std::endl;
    std::cout <<"-------------------------------------" << std::endl;
}

 void Veiculo::setTipo (int tp){
    tipo=tp;
 }
void Veiculo::setVelMax (int vm){
    velMax=vm;
    }

class Moto:public Veiculo { // classe filha 'Moto' herda da classe pai 'Veiculo';
public:
        Moto ();
};

Moto::Moto (){
    vel=0;
    pass=1;
    rodas=2;
    setTipo (1);
    setVelMax(120);
}

class Carro:public Veiculo{ // classe filha 'Carro' herda da classe pai 'Veiculo';
public:
    Carro();
};

Carro::Carro(){
    vel=0;
    pass=4;
    rodas=4;
    setTipo (2);
    setVelMax(180);
}

class Caminhao:public Veiculo { // classe filha 'Caminhao' herda da classe pai 'Veiculo';
public:
        Caminhao ();
};

Caminhao::Caminhao (){
    vel=0;
    pass=1;
    rodas=12;
    setTipo (3);
    setVelMax(130);
}

class Aviao:public Veiculo { // classe filha 'Aviao' herda da classe pai 'Veiculo';
public:
        Aviao ();
};

Aviao::Aviao (){
    vel=0;
    pass=200;
    rodas=18;
    setTipo (4);
    setVelMax(850);
}

#endif // CLASSES_H_INCLUDED
