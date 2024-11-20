### Type Hints ###

MyVariable = "My String variable"
print(MyVariable)
print(type(MyVariable))

MyVariable = 5
print(MyVariable)
print(type(MyVariable))


# Es imoprtante decir exactamente qué tipo de dato es
# Así nunca habra confusiones en el servidor
# Se hace declarando la variable y después : dato(str, int, float, list)

my_typed_variable: str = "This is a string"
print(type(my_typed_variable))

my_typed_variable: str = 5
print(type(my_typed_variable))

#Por más que se intente, el tipado de python es 
# debil y no se puede obligar
# al fichero a cambiar el dato