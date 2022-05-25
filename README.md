*Cristian Acosta - A00820013*
*Kevin Chinchilla - A00825945*

# Entrega 6
En esta entrega generamos código para objetos, y funciones.

En cuanto a **funciones**, se genera ERA, llamándolo con el ID de la función
Se hace RETURN a un espacio de memoria global, por lo que todavía no soporta
llamadas recursivas como la siguiente:

Pero es algo que planeamos resolver para la entrega final.

```
fun1()
{
    ..
    fun1() + fun1()
}
```

En cuanto a **objetos**, se guardan atributos como variables, siendo 
obj.atributo.
Se hacen todas las validaciones relevantes, tanto que el atributo exista, y que
pertenezca a la clase (o a una clase padre).

De la misma manera, estos atributos ya se compilan para expresiones.

Todavía no se generan cuádruplos referenciando memoria, sin embargo, ya esta 
definido el módulo, que se prueba en expresiones de assignment (estas
ya aparecen referenciando direcciones de memoria).

Para la proxima entrega planeamos ya tener ejecución de código.