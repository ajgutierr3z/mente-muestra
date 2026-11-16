# Proyecto "Mente y Muestra": Observación Cualitativa y Visualización

Este repositorio contiene el conjunto de datos (dataset) y el código fuente en Python utilizados para visualizar el impacto cualitativo del proyecto **"Mente y Muestra"**, una innovación de transposición didáctica que utiliza inteligencia artificial (Suno AI) y música hip-hop *lo-fi* para enseñar Estadística en la carrera de Psicología.

El objetivo de estos archivos es medir y graficar cómo la intervención musical ayuda a reducir la **ansiedad matemática** y aumentar la **retención conceptual** en los estudiantes.

## 📂 Contenido del Repositorio

* `dataset_observacion.csv`: Conjunto de datos simulados basados en la rúbrica de observación docente en el aula.
* `visualiza_data.py`: Script de Python que lee el archivo CSV y genera una gráfica de pendiente (*Slopegraph*) comparativa.

## 📊 Sobre el Dataset (`observacion_cualitativa.csv`)

Los datos están estructurados en una escala ordinal del 1 al 10, obtenida mediante observación cualitativa pre y post intervención. El dataset contiene las siguientes columnas:

* `Estudiante`: Identificador anónimo del alumno (ej. E01, E02).
* `Ansiedad_Pre_Intervencion`: Nivel de tensión y bloqueo cognitivo (filtro afectivo) durante el método tradicional.
* `Ansiedad_Post_Intervencion`: Nivel de tensión tras escuchar la canción "Mente y Muestra".
* `Retencion_Pre_Intervencion`: Capacidad de evocación de conceptos con el método tradicional.
* `Retencion_Post_Intervencion`: Capacidad de evocación y recuerdo al usar las rimas musicales.

## 📈 Visualización (Estilo Edward Tufte)

El script de visualización está diseñado bajo los estrictos principios del teórico **Edward Tufte**. Se utiliza un *Slopegraph* (Gráfico de pendiente) que elimina por completo la "basura gráfica" (*chartjunk*), prescindiendo de ejes pesados, cuadrículas y bordes para maximizar la proporción datos-tinta. Esto permite ilustrar de manera honesta y directa el contraste entre el "Antes" y el "Después".

## 🚀 Cómo ejecutar el código

### Requisitos previos
Asegúrate de tener instalado Python 3.x en tu sistema. Necesitarás las librerías `pandas` y `matplotlib`. Puedes instalarlas ejecutando:

```bash
pip install pandas matplotlib
