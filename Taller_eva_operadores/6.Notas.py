nota1 = float(input("Ingrese la nota del taller 1: "))
nota2 = float(input("Ingrese la nota del taller 2: "))
nota3 = float(input("Ingrese la nota del cuestionario 1: "))
nota4 = float(input("Ingrese la nota del cuestionario 2: "))
nota5 = float(input("Ingrese la nota del proyecto de aula: "))

nota_def = nota1 * 0.2 + nota2 * 0.15 + nota3 * 0.22 + nota4 * 0.1 + nota5 * 0.33

print(f"La nota definitiva del curso de fundamentos de algoritmos es: {nota_def:.2f}")

if 