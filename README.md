# Libreria_Complejos
Librería de operaciones entre complejos en Python  
Hecho por *Sebastian Cardona Parra*  
Entre dichas operaciones de complejos, esta:
---
+ Suma  
def sumcplx(a,b):  
    real = a[0]+b[0]  
    img = a[1]+b[1]  
    return real,img  
aqui se presenta la sintaxis basica de la suma de numeros complejos, una funciòn que recibe dos parametros que son complejos, opera real con real e imaginario con imaginario para devolver un resultado  
Las demas funciones de operaciones entre complejos manejan una sintaxis similar, con el ligero cambio que en cada funciòn que hace la operacion respectiva.  
+ resta  
+ multiplicacion  
+ division  
+ modulo  
que se refiera a la raiz cuadrada entre el cuadrado del real mas el cuadrado del imaginario pero sin la i, dicha funcion recibe un complejo y devuelve un real  
+ conjugado  
es el mismo complejo pero con la parte imaginaria negada  
+ conversion polar a cartesiano  
en el plano se puede representar un punto de manera convencional pero tambien de manera polar, igual sucede en los complejos, donde se representa de la manera
(a,b) siendo a el modulo y b el angulo respecto al eje polar, llamado tambien fase  
+ fase  
