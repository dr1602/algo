def switch_demo(day):
    switcher = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes"
    }
    return switcher.get(day, "Fin de semana")

day = 3
print(switch_demo(day))  # Imprime "Miércoles"
