### Redes de Petri  
* Herramienta gráfica y matemática para modelar sistemas concurrentes y distribuidos.
* Creada por Carl Adam Petri en 1962.
* Representa eventos, condiciones, recursos compartidos y su interacción temporal.
* Permite analizar el comportamiento dinámico de un sistema (sincronización, paralelismo, bloqueos, etc.)
* Cada objeto tiene un estado (marcado) y transiciones que representan eventos o acciones.
* Útil en informática, ingeniería de control, sistemas de manufactura, redes, biología computacional, entre otros.
* Similar a los diagramas de transición de estados.
* Utiliza teorías matemáticas.  

#### Definición Formal  
Una Red de Petri (RP) es una 4-upla R=(P,T,I,O) donde:  

P = {p₁, p₂, …, pₘ} conjunto finito de “lugares”.  

T = {t₁, t₂, …, tₘ} es un conjunto finito de “transiciones”.  

I: P x T → ℕ es una “función de entrada a las transiciones”.  

O: P x T → ℕ es una “función de salida de las transiciones”.  

#### ¿Cómo se diseñana?  
* *Plazas/Lugares*  

Representan los estados posibles del sistema.
* *Transiciones*  

Son los eventos o acciones que causan el cambio de estado.
* *Arco (Flechas)*  

Cada Arco conecta una Plaza con una transición o una transición con una plaza.
* *Token*  

Marca el estado activo en ese momento.

<!-- Agregar el diseño de cada componente -->
<!-- Agregar Secuencias -->

#### Propiedades principales  
* *Alcanzabilidad*  
Si un estado (resultado) puede alcanzarse.  
¿Existe algún camino de disparos que me lleve desde el estado inicial hasta ese estado?  

* *Acotación*  
Asegura que no haya desbordes de tokens (nuestras redes son 1-acotadas).  
¿Puede acumularse una cantidad infinita de tokens en algún lugar?

* *Vivacidad*  
Garantiza que ninguna transición quede “muerta” (sin posibilidad de disparo).  
¿Ninguna transición se queda muerta para siempre?

> [!IMPORTANT]  
> Tiene que haber un token en cada plaza para que la transición se dispare.  
> Al dispararse, consume tokens de entrada y produce tokens de salida.  

---  
### Redes de Petri Coloreadas (CPN)  
* Son una extensión de las redes de Petri tradicionales.
* Permiten que los tokens tengan información asociada, llamada color (puede ser un número, texto o estructura de datos).
* Sirven para modelar sistemas más complejos sin necesidad de duplicar plazas o transiciones.  

Además de plazas, transiciones y arcos, las CPN agregan:  
* *Colores:* tipos de datos que describen los tokens.
* *Variables:* representan tokens en las expresiones.
* *Guardas:* condiciones lógicas que controlan cuándo se dispara una transición.  

#### Petri tradicional VS Coloreada   
| Aspecto | Tradicional | Coloreada(CPN)|
|:---:|:---|:---|
|Tokens|Todos iguales|Cada token tiene un “color” (dato)|
|Datos|No maneja información|Usa tipos de datos (números, texto, tuplas)|
|Condiciones|No hay condiciones lógicas|Tiene guardas (ej: [prioridad > 2])|
|Variables|No existen|Usa variables para manipular datos|
|Tamaño del modelo|Más grande (muchas plazas y transiciones)|Más compacto (una red representa varios casos)|
|Visualización|Tokens idénticos|Tokens diferenciados por color o etiqueta|
|Nivel de abstracción|Bajo|Alto (estructura + datos + lógica)|
|Uso típico|Procesos simples o sincronización básica|Sistemas con datos, prioridades o clases distintas|