"""
Pon las funciones del ejemplo printing_models.py en un archivo separado llamado
printing_functions.py.
Escribe una sentencia al comienzo del archivo printing_models.py, y modifica el fichero
para que use las funciones importadas.
"""

from printing_model import print_models, show_completed_models
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
