Título → Shark Attacks: Análisis de patrones en ataques de tiburón

Objetivo del proyecto → Analizar los ataques de tiburón registrados para identificar patrones geográficos, temporales y relacionados con las actividades realizadas, así como estudiar la fatalidad de los incidentes. El análisis busca obtener información útil para desarrollar iniciativas de concienciación y prevención en zonas con una alta concentración de ataques registrados.

Contexto del negocio → El proyecto está planteado para una organización pública internacional ficticia enfocada en la concienciación y prevención de ataques de tiburón.

La organización necesita comprender dónde se concentran los ataques registrados, qué actividades estaban realizando las personas, cómo han evolucionado los registros a lo largo del tiempo y qué proporción de los ataques fueron mortales.

Los resultados pueden ayudar a identificar zonas y actividades en las que podría ser útil reforzar las campañas de información y prevención.

Dataset → Utilizamos un dataset de ataques de tiburón con más de 7.000 registros.

El dataset original contiene información sobre la fecha, localización, actividad, víctima, lesiones, fatalidad, especie de tiburón y otras características relacionadas con cada incidente.

Para nuestro análisis seleccionamos cinco variables principales:
"Country" País donde se registró el ataque
"State" Estado o región donde ocurrió
"Year" Año del ataque
"Activity" Actividad que realizaba la persona
"Fatal Y/N" Indica si el ataque fue mortal o no

Notas sobre calidad del dato → Durante la exploración inicial detectamos varios problemas de calidad que debían tenerse en cuenta antes de realizar el análisis. Entre ellos: 
- Valores nulos en variables relevantes como "Country", "State", "Activity", "Year" y "Fatal Y/N".
- Falta de estandarización en variables categóricas, con diferencias de mayúsculas, minúsculas y espacios adicionales.
- Valores inconsistentes en "Fatal Y/N", donde además de "Y" y "N" aparecían otros valores que no permitían determinar correctamente la fatalidad.
- Gran variedad de valores en "Activity", al tratarse de una variable con descripciones poco estandarizadas.
- Dos registros sin información de "Year", que se mantuvieron como valores desconocidos para no asignar información de forma artificial.
- Registros históricos con diferente nivel de detalle, lo que puede afectar especialmente al análisis temporal.

Preguntas clave → Nuestro análisis busca responder cuatro preguntas principales:

1. ¿Dónde se concentran los ataques de tiburón registrados?
Hipótesis: Los ataques registrados se concentran en determinadas zonas geográficas.
2. ¿Qué estaban haciendo las personas cuando ocurrió el ataque?
Hipótesis: Determinadas actividades acuáticas aparecen con mayor frecuencia que otras.
3. ¿Cómo han cambiado los ataques registrados a lo largo del tiempo?
Hipótesis: Los ataques registrados muestran una mayor concentración en los periodos más recientes.
4. ¿Varía la fatalidad según la localización?
Hipótesis: La proporción de ataques mortales varía según la localización geográfica.

Proceso de análisis → El análisis se realizó en tres fases principales:

- Limpieza: tratamiento de valores nulos, formatos inconsistentes y estandarización de las variables seleccionadas mediante funciones en "cleaning.py".
- Análisis Exploratorio de Datos (EDA): agrupaciones, conteos y visualizaciones para analizar patrones geográficos, actividades, evolución temporal y fatalidad.
- Métricas clave: número de ataques por localización y actividad, promedio de ataques por año y tasa de fatalidad global y por localización.

Finalmente, los resultados obtenidos se utilizaron para contrastar las hipótesis planteadas.

Resultados e insights →
- Concentración geográfica: Florida destaca con 1.200 ataques registrados, seguida por varias regiones de Australia y Estados Unidos.
- Actividad: "surfing" es la actividad más frecuente y ocupa el primer lugar en 4 de las 5 zonas con más ataques registrados.
- Evolución temporal: Los datos muestran una tendencia general de aumento de los ataques registrados a lo largo del tiempo
- Fatalidad: El 23,1 % de los casos con desenlace conocido fueron mortales y la tasa de fatalidad presenta diferencias importantes según la localización.

En conjunto, los resultados apoyan las hipótesis planteadas y muestran que una mayor frecuencia de ataques registrados no implica necesariamente una mayor fatalidad.

Recomendaciones de negocio → A partir de los resultados obtenidos, las campañas de concienciación podrían priorizar las regiones con una elevada concentración de incidentes registrados, especialmente Florida y determinadas regiones de Australia.

También podría ser útil desarrollar campañas específicas dirigidas a actividades que aparecen frecuentemente asociadas a los ataques registrados, especialmente "surfing" y "swimming".

Sin embargo, el número de ataques registrados no debe interpretarse directamente como una medida del riesgo real. Para tomar decisiones basadas en riesgo sería necesario incorporar información adicional sobre la exposición de las personas al mar.

En una siguiente fase sería útil analizar el perfil de las personas afectadas para identificar qué grupos aparecen con mayor frecuencia en los registros y orientar mejor las campañas de prevención y su comunicación.

Limitaciones → La principal limitación del proyecto es que el dataset contiene información sobre ataques registrados, pero no incluye datos suficientes para calcular el riesgo real de sufrir un ataque.

Por ejemplo, desconocemos:

- El número de bañistas de cada región.
- El número de surfistas.
- El tiempo de exposición al agua.
- El volumen de turismo.
- La frecuencia con la que se practica cada actividad.
- Si los registros históricos tienen el mismo nivel de cobertura que los actuales.

Por este motivo: Más ataques registrados no es igual a un mayor riesgo individual.

Además, el aumento de ataques registrados a lo largo del tiempo podría estar influido por mejoras en los sistemas de registro y recopilación de información.

Las tasas de fatalidad también pueden resultar poco representativas cuando existen pocos casos. Por este motivo, para el análisis geográfico de fatalidad utilizamos únicamente localizaciones con al menos 20 ataques con desenlace conocido.

Próximos pasos → Si dispusiéramos de más tiempo y datos, podríamos ampliar el proyecto mediante:

- Datos de turismo y afluencia a las playas
- Número estimado de personas expuestas al mar
- Analizar el perfil de las personas afectadas
- Relación entre actividad y fatalidad
- Comparación de patrones entre diferentes periodos históricos
- Creación de un mapa interactivo
- Desarrollo de un dashboard para explorar los resultados

Cómo replicar el proyecto → El proyecto puede replicarse utilizando el dataset original y ejecutando el código de análisis incluido en el repositorio.
Las funciones utilizadas para la limpieza y estandarización de los datos se encuentran en "cleaning.py". 
Entre las tecnologías utilizadas:  Python, Pandas, Matplotlib, Jupyter Notebook.
