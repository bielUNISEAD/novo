#include <iostream>
#include "classes.h"

using namespace std;

int main () {

    Moto *v1=new  Moto(); //criando os objetos
    Carro *v2=new Carro();
    Caminhao *v3=new Caminhao();
    Aviao *v4=new Aviao ();

    v1->imp(); //objetos chamando métodos da classe pai;
    v2->imp();
    v3->imp();
    v4->imp();

	return 0;

}
