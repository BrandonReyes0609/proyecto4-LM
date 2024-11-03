import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definir las variables de entrada y salida
luz_natural = ctrl.Antecedent(np.arange(0, 101, 1), 'luz_natural')
hora_del_dia = ctrl.Antecedent(np.arange(0, 24, 1), 'hora_del_dia')
intensidad_luz = ctrl.Consequent(np.arange(0, 101, 1), 'intensidad_luz')

# Definir los conjuntos difusos para luz natural
luz_natural['baja'] = fuzz.trimf(luz_natural.universe, [0, 0, 50])
luz_natural['moderada'] = fuzz.trimf(luz_natural.universe, [25, 50, 75])
luz_natural['alta'] = fuzz.trimf(luz_natural.universe, [50, 100, 100])

# Definir los conjuntos difusos para hora del día
hora_del_dia['mañana'] = fuzz.trimf(hora_del_dia.universe, [0, 8, 12])
hora_del_dia['tarde'] = fuzz.trimf(hora_del_dia.universe, [12, 16, 20])
hora_del_dia['noche'] = fuzz.trimf(hora_del_dia.universe, [18, 24, 24])

# Definir los conjuntos difusos para la intensidad de la luz artificial
intensidad_luz['baja'] = fuzz.trimf(intensidad_luz.universe, [0, 0, 50])
intensidad_luz['media'] = fuzz.trimf(intensidad_luz.universe, [25, 50, 75])
intensidad_luz['alta'] = fuzz.trimf(intensidad_luz.universe, [50, 100, 100])

# Definir las reglas difusas
rule1 = ctrl.Rule(luz_natural['alta'] & hora_del_dia['mañana'], intensidad_luz['baja'])
rule2 = ctrl.Rule(luz_natural['moderada'] & hora_del_dia['tarde'], intensidad_luz['media'])
rule3 = ctrl.Rule(luz_natural['baja'] | hora_del_dia['noche'], intensidad_luz['alta'])

# Crear el sistema de control y simulación
control_iluminacion = ctrl.ControlSystem([rule1, rule2, rule3])
simulacion_iluminacion = ctrl.ControlSystemSimulation(control_iluminacion)

# Valores de entrada para probar el sistema
simulacion_iluminacion.input['luz_natural'] = 30  # Cambiar según las condiciones
simulacion_iluminacion.input['hora_del_dia'] = 21

# Calcular la intensidad de luz artificial
simulacion_iluminacion.compute()
print(f"Intensidad de luz recomendada: {simulacion_iluminacion.output['intensidad_luz']}%")

# Visualizar los gráficos de los conjuntos difusos con títulos
plt.figure()
luz_natural.view()
plt.title("Conjunto Difuso de Luz Natural")
plt.ylabel("Grado de Pertenencia")  # Cambia el eje Y
plt.show()

plt.figure()
hora_del_dia.view()
plt.title("Conjunto Difuso de Hora del Día")
plt.ylabel("Grado de Pertenencia")  # Cambia el eje Y
plt.show()

plt.figure()
intensidad_luz.view()
plt.title("Conjunto Difuso de Intensidad de Luz Artificial")
plt.ylabel("Grado de Pertenencia")  # Cambia el eje Y
plt.show()

# Pausar la consola para que no se cierre inmediatamente
input("Presiona Enter para salir...")
