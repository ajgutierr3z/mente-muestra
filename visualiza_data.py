import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer el dataset directamente desde el archivo CSV
df = pd.read_csv('dataset_observacion.csv')

# 2. Calcular automáticamente los promedios grupales a partir de las columnas
ansiedad_pre = df['Ansiedad_Pre_Intervencion'].mean()
ansiedad_post = df['Ansiedad_Post_Intervencion'].mean()

retencion_pre = df['Retencion_Pre_Intervencion'].mean()
retencion_post = df['Retencion_Post_Intervencion'].mean()

# Agrupar los datos calculados para inyectarlos en la gráfica
indicadores = ["Ansiedad Matemática", "Retención Conceptual"]
valores_pre = [ansiedad_pre, retencion_pre]
valores_post = [ansiedad_post, retencion_post]

# 3. Configuración del lienzo (Estilo minimalista de Edward Tufte)
fig, ax = plt.subplots(figsize=(7, 6), facecolor='white')

# Colores: Rojo apagado (Ansiedad/Desgaste) y Verde oliva (Retención/Mejora)
colores = ['#A32626', '#1E4620']
ancho_linea = 2.5

# 4. Dibujar el Slopegraph iterando sobre los datos procesados
for i in range(len(indicadores)):
    # Línea de tendencia
    ax.plot([0, 1], [valores_pre[i], valores_post[i]], color=colores[i], linewidth=ancho_linea, alpha=0.95)

    # Nodos en los extremos
    ax.scatter([0, 1], [valores_pre[i], valores_post[i]], color=colores[i], s=70, zorder=3)

    # Etiquetas de datos a la izquierda (Pre)
    ax.text(-0.06, valores_pre[i], f"{indicadores[i]}\n {valores_pre[i]:.1f}",
            ha='right', va='center', fontsize=11, fontweight='semibold', color='#2b2b2b')

    # Etiquetas de datos a la derecha (Post)
    ax.text(1.06, valores_post[i], f"{valores_post[i]:.1f}\n {indicadores[i]}",
            ha='left', va='center', fontsize=11, fontweight='semibold', color='#2b2b2b')

# 5. Eliminación de "basura gráfica" (Chartjunk)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.tick_params(axis='x', which='both', length=0)  # Quitar marcas del eje X

# Configurar las etiquetas del eje X
ax.set_xticks([0, 1])
ax.set_xticklabels(['PRE-INTERVENCIÓN\n(Método Tradicional)', 'POST-INTERVENCIÓN\n("Mente y Muestra")'],
                   fontsize=11.5, fontweight='bold', color='#1a1a1a')

# Ajustar los límites para que las etiquetas de texto no se corten
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(min(valores_post + valores_pre) - 1.5, max(valores_post + valores_pre) + 1.5)

# Título descriptivo en formato APA
plt.title(
    'Figura 2. Transformación de los indicadores observados pre y post intervención\n(Escala observacional de 1 a 10)',
    fontsize=11, loc='center', pad=25, fontweight='bold', color='#333333', style='italic')

plt.tight_layout()
plt.show()
