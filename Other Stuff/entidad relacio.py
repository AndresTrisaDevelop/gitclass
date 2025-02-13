from graphviz import Digraph

# Crear un nuevo gráfico dirigido
dot = Digraph()

# Añadir nodos
dot.node('Producto', 'Producto')
dot.node('Categoría', 'Categoría')
dot.node('Feature', 'Feature')
dot.node('Opción', 'Opción')
dot.node('Precio', 'Precio')

# Añadir aristas (relaciones)
dot.edge('Categoría', 'Producto', label='1 a N')
dot.edge('Producto', 'Feature', label='1 a N')
dot.edge('Feature', 'Opción', label='1 a N')
dot.edge('Producto', 'Precio', label='1 a N')
dot.edge('Opción', 'Precio', label='1 a N')

# Renderizar el gráfico
dot.render('/mnt/data/diagrama_ER', format='png', cleanup=True)

