#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#imprime 5 porque es el valor que retorna la funcion

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#(number_of_days_in_a_week_silicon_or_triangle_sides no esta definido por lo tanto no lo va a imprimir.


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#imprime 5 debido a que se toma el primer return

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#imprime 5 ya que hay un return y eso lo toma antes del siguiente codigo

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# imprime solamente 5 porque imprime number_of_great_lakes que se remplazo por el x 


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#imprime 3 y 5 porque add(1,2) y add(2,3) se suman y da el resultado de cada una

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) 
#imprime 25 porque es la suma de b + c pero al estar 'str' se juntan y da 25 como resultado

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#imprime 10 porque b es 100 entonce imprime el else

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# la funcion  7 + 14 y en la ultima llamada imprime 21 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#va a imprimir 8 ya que se suma B y C y estan declarados como 3 y 5

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#imprime 500 luego 500 llama la funcion que muestra 300 y luego vuelve a 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#primero nos va a imprimir 2 veces 500 ya que primero se imprime solo y desoues returna luego se invoca el foobar que es 300 y a continuacion vuelve a imprimir 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#imprime 500 luego 500 llama la funcion que muestra 300 y nuevamente 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#va a imprimir 1 , 3 y luego 2 ya que se define bar como 2 

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#la primera funcion que imprimira es 1,3 y 5 en cuanto a la segunda sera 10