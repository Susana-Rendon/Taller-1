nota1 = float(input("Ingrese la nota del taller 1: "))
nota2 = float(input("Ingrese la nota del taller 2: "))
nota3 = float(input("Ingrese la nota del cuestionario 1: "))
nota4 = float(input("Ingrese la nota del cuestionario 2: "))
nota5 = float(input("Ingrese la nota del proyecto de aula: "))

if 1 <= nota1 <= 5 and 1 <= nota2 <= 5 and 1 <= nota3 <= 5 and 1 <= nota4 <= 5 and 1 <= nota5 <= 5:
    nota_def = nota1 * 0.2 + nota2 * 0.15 + nota3 * 0.22 + nota4 * 0.1 + nota5 * 0.33
    print(f"La nota definitiva del curso de fundamentos de algoritmos es: {nota_def:.2f}")

    if 1 <= nota_def <= 2.9:
        nota_def = "Su nota es insuficiente"
    elif 3 <= nota_def <= 3.9:
        nota_def = "Su nota es regular"
    elif 4 <= nota_def < 4.5:
        nota_def = "Su nota es buena"
    elif 4.6 < nota_def <= 5:
        nota_def = "Su nota es excelente"
    else:
        print("ingreso un valor incorrecto")

    print(nota_def)
else:
    print("Ingresó un valor incorrecto en las notas. Las notas deben estar entre 1 y 5.")








