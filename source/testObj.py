tabla = {'Persona': {'attributes': {'age': 'int', 'height': 'float'}, 'methods': {}},
         'Alumno': {'attributes': {}, 'methods': {}}}


#directorio_funciones[scope][2][var_id] = [var_type, var_kind, address]
tabla['Persona']['attributes']['name'] = 'char'
print(tabla['Persona']['attributes']['age'])
