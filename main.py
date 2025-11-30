DRINKS = "напиток → «чай», «кофе», «сок»"
SOUP = "суп → «борщ», «щи», «суп-пюре»"
DESSERT = "десерт → «торт», «мороженое», «фрукты»"

print(DRINKS)
print(SOUP)
print(DESSERT)

menu = input("")

if menu == "напиток":
    print(DRINKS)
elif menu == "суп":
    print(SOUP)
elif menu == "десерт":
    print(DESSERT)
else:
    print("Выберите категорию из списка!")

price = input("")

match price:
    case "чай":
        print("40p")
    case "кофе":
        print("70р")
    case "сок":
        print("100р")
    case "борщ":
        print("120р")
    case "щи":
        print("110р")
    case "суп-пюре":
        print("140р")
    case "торт":
        print("100р")
    case "мороженное":
        print("80р")
    case "фрукты":
        print("130р")
    case _:
        print("ошибка")

        #sdelal