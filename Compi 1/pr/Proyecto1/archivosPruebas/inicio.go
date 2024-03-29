inicio
/////inicio de la traduccion

ingresar _variable1_ como Numero con_valor 5;
ingresar _v1_, _v2_, _v3_ como Cadena "esta es una cadena";

_v1_ -> "esta es la cadena numero 1";
_v2_, _v3_ -> "estas cadenas deben ser diferentes";

imprimir_nl (_v3);

si _v1_ es_igual _v2_ entonces
	imprimir_nl "Al parecer no funciona la asignacion";
	mientras not _variable1_ mayor_o_igual 5*5+8/2 hacer
		imprimir _variable1_;
		_variable1_ -> _variable1_ + 1;
	fin_mientras
fin_si


ingresar _varB_ como Boolean con_valor falso; //tomar como "falso" o "verdadero" los valores booleanos

if _varB_ entonces
	imprimir_nl "Estas definiendo bien los valores";
	ingresar _varaux_ como Numero con_valor _variable1_ % 2;
	segun _varaux_ hacer
		0 entonces
			imprimir "el valor es mayor a 0 y menos a 2";
		2 entonces
			imprimir "el valor es mayor a 2";
	fin_segun
fin_si

ejecutar _metodo_1_();

/*Ahora empezamos con las funciones y procedimientos*/

metodo _potenciaManual_ con_parametros (_base_ Numero, _exponenete_ Numero)
	ingresar _i_ como Numero con_valor 0;
	ingresar _acumulado_ como Numero con_valor 0;
	para _i_->0 hasta _exponente_-1 hacer
		_acumulado_ -> _acumulado_ + _acumulado_;
	fin_para	
	imprimir _acumulado_;
	imprimir_nl " Esta es la potencia Manual";	
fin_metodo

funcion _potenciaFuncion_ Numero con_parametros (_base_ Numero, _exponente_ Numero) 
	ingresar _potencia_ como Numero con_valor _base_ potencia _exponente_;
	retornar _potencia_;
fin_funcion

metodo _metodo_1_
	imprimir_nl "estamos entrando al metodo 1";	
	ejecutar _potenciaManual_(3*1+4/2, 3+2);
	imprimir ejecutar _potenciaFuncion_(3*1+4/2, 3+2);
	imprimit_nl " Esta es la potencia Funcion";
fin_metodo

fin

/*
//////SALIDA EN GOLANG

package main

import (
	"fmt"
	"math"
)

/////inicio de la traduccion

func main() {

	var _variable1_ int = 5
	var _v1_, _v2_, _v3_ string = "esta es una cadena", "esta es una cadena", "esta es una cadena"

	_v1_ = "esta es la cadena numero 1"
	_v2_, _v3_ = "estas cadenas deben ser diferentes", "estas cadenas deben ser diferentes"
	fmt.Println((_v3_))
	if _v1_ == _v2_ {
		fmt.Println("Al parecer no funciona la asignacion")
		for true {
			if !(!(_variable1_ >= 5*5+8/2)) {
				break
			}
			fmt.Println(_variable1_)
			_variable1_ = _variable1_ + 1
		}
	}

	var _varB_ bool = false //tomar como "falso" o "verdadero" los valores booleanos

	if _varB_ {
		fmt.Println("Estas definiendo bien los valores")
		var _varaux_ int = _variable1_ % 2
		switch _varaux_ {
		case 0:
			fmt.Print("el valor es mayor a 0 y menos a 2")
		case 2:
			fmt.Print("el valor es mayor a 2")
		}
	}
	_metodo_1_()
}

/*Ahora empezamos con las funciones y procedimientos*/

func _potenciaManual_(_base_ int, _exponente_ int) {
	var _i_ int = 0
	var _acumulado_ int = 0
	for _i_ = 0; _i_ == _exponente_-1; _i_++ {
		_acumulado_ = _acumulado_ + _acumulado_
	}
	fmt.Print(_acumulado_)
	fmt.Println(" Esta es la potencia Manual")
}

func _potenciaFuncion_(_base_ int, _exponente_ int) float64 {
	var _potencia_ float64 = math.Pow(float64(_base_), float64(_exponente_))
	return _potencia_
}

func _metodo_1_() {
	fmt.Println("estamos entrando al metodo 1")
	_potenciaManual_(3*1+4/2, 3+2)
	fmt.Print(_potenciaFuncion_(3*1+4/2, 3+2))
	fmt.Println(" Esta es la potencia Funcion")
}



*/

//////SALIDA EN PYTHON

def _potenciaManual_(_base_, _exponente_):
	_i_ = 0
	_acumulado_ = 1
	for _i_ in range(0,_exponente_):
		_acumulado_ = _base_ * _acumulado_

	print(_acumulado_)
	print("Esta es la potencia Manual")


def _potenciaFuncion_(_base_, _exponente_):
	_potencia_ = _base_ ** _exponente_
	return _potencia_


def _metodo_1_():
	print("estamos entrando al metodo 1")
	_potenciaManual_(3*1+4/2, 3+2)
	print(_potenciaFuncion_(3*1+4/2, 3+2))
	print(" Esta es la potencia Funcion")
	
def main():
	_variable1_ = 5
	_v1_, _v2_, _v3_ = "esta es una cadena", "esta es una cadena", "esta es una cadena"

	_v1_ = "esta es la cadena numero 1"
	_v2_, _v3_ = "estas cadenas deben ser diferentes", "estas cadenas deben ser diferentes"

	print((_v3_))

	if _v1_ == _v2_ :
		print("Al parecer no funciona la asignacion")
		while not (_variable1_ >= 5*5+8/2):
			print(_variable1_)
			_variable1_ = _variable1_ + 1
		
	

	_varB_ = False 

	if _varB_ :
		print("Estas definiendo bien los valores")
		_varaux_ = _variable1_ % 2

		#simulando el switch
		if _varaux_ == 0:
			print("el valor es mayor a 0 y menos a 2")
		elif _varaux_ == 2:
			print("el valor es mayor a 2")
		
	_metodo_1_()

if __name__ == "__main__":
	main()
