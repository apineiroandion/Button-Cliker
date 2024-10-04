# Button-Clicker

## Indice por aqui

## Explicacion por aca

## Código por aqui
```
def __init__(self):
    super().__init__()  # Llamamos al constructor de la clase padre
    self.total_clicks = None  # Inicializamos la variable para contar el total de clics
    self.contadores = None  # Inicializamos la lista de contadores (uno por botón)
    self.initUI()  # Llamamos a la función que inicializa la interfaz gráfica
```
Este es el `método constructor` de la clase. Cada vez que se crea un nuevo objeto de esta clase, Python llama automáticamente a este método para inicializar el objeto. 
Por otro lado, `self` es una referencia al objeto actual (la instancia de la clase). A través de `self`, puedes acceder a las variables y métodos de la clase.

```
super().__init__():
```
super() es una función incorporada en Python que se utiliza para llamar a un método de la clase padre (o superclase) desde la clase hija (o subclase).
`__init__()` es el constructor de la clase padre. Al llamarlo, inicializas cualquier configuración que se define en la clase base.
### Por Qué Usar 'super()'?
Aquí hay algunas razones para usar super():

    Inicialización Adecuada: Permite que la clase padre se inicialice correctamente, lo que es esencial si la clase padre tiene atributos o inicializaciones necesarias.

    Mantenimiento del Código: Si decides cambiar la clase base en el futuro, el uso de super() ayuda a mantener el código más limpio y fácil de manejar.

    Soporte para Múltiple Herencia: En Python, puedes heredar de múltiples clases. Usar super() es una manera más segura de asegurarte de que todos los constructores de las clases base se llamen en el orden correcto.

## Conclusión por aca