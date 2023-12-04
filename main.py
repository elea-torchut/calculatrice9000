def saisie_nombre():
    while True:
        try:
            nombre = float(input("Entrez un nombre : "))
            return nombre
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def saisie_operation():
    operations_valides = ['+', '-', '*', '/']
    while True:
        operation = input("Entrez l'opération (+, -, *, /) : ")
        if operation in operations_valides:
            return operation
        else:
            print("Opération non valide. Veuillez réessayer.")

def calculatrice():
    try:
        nombre1 = saisie_nombre()
        operation = saisie_operation()
        nombre2 = saisie_nombre()

        if operation == '+':
            resultat = nombre1 + nombre2
        elif operation == '-':
            resultat = nombre1 - nombre2
        elif operation == '*':
            resultat = nombre1 * nombre2
        elif operation == '/':
            if nombre2 == 0:
                print("Erreur : division par zéro.")
                return
            else:
                resultat = nombre1 / nombre2

        print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à : {resultat}")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    calculatrice()
