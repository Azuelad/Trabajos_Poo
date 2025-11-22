import numpy as np
import random

def calcular_calificaciones_sin_comentarios():
    try:
        num_estudiantes = int(input("Ingrese el número de estudiantes: "))
        num_materias = int(input("Ingrese el número de materias: "))
    except ValueError:
        print("Error: Ingrese números enteros válidos.")
        return

    if num_estudiantes <= 0 or num_materias <= 0:
        print("Error: Los números deben ser mayores que cero.")
        return

    calificaciones = []
    
    # Captura de calificaciones (se podría sustituir por random.randint(0, 100) para prueba)
    print("\n--- Captura de Calificaciones (0-100) ---")
    for i in range(num_estudiantes):
        fila_estudiante = []
        print(f"\nEstudiante {i + 1}:")
        for j in range(num_materias):
            while True:
                try:
                    calif = float(input(f"  Calificación Materia {j + 1}: "))
                    if 0 <= calif <= 100:
                        fila_estudiante.append(calif)
                        break
                    else:
                        print("La calificación debe estar entre 0 y 100.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
        calificaciones.append(fila_estudiante)

    matriz_calificaciones = np.array(calificaciones)
    
    print("\n" + "="*50)
    print("RESULTADOS DEL ANÁLISIS")
    print("="*50)

    # Promedio por estudiante (Axis 1: Horizontal)
    promedios_estudiantes = matriz_calificaciones.mean(axis=1)
    print("Promedio por Estudiante:")
    for i, promedio in enumerate(promedios_estudiantes):
        print(f"Estudiante {i + 1}: {promedio:.2f}")

    print("-" * 50)

    # Promedio por materia (Axis 0: Vertical)
    promedios_materias = matriz_calificaciones.mean(axis=0)
    print("Promedio por Materia:")
    for j, promedio in enumerate(promedios_materias):
        print(f"Materia {j + 1}: {promedio:.2f}")

    print("-" * 50)

    # Calificación más alta
    calificacion_maxima = matriz_calificaciones.max()
    print(f"Calificación Más Alta: {calificacion_maxima:.2f}")

    # Calificación más baja
    calificacion_minima = matriz_calificaciones.min()
    print(f"Calificación Más Baja: {calificacion_minima:.2f}")
    
    print("="*50)
    
calcular_calificaciones_sin_comentarios()