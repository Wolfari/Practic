# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
define e = Character(_('Елена'), color="#c8ffc8")

label start:

    e"что ты любишь конфеты или шоколад?"

    $ timez = 5
    $ time_range = 5
    $ marker = "not_chance"

    menu:
        "конфеты":
            jump var1
        "шоколад":
            jump var2


label var1:
    "Я выбираю конфеты!"
    jump next

label var2:
    "Я выбираю шоколад!"
    jump next

label not_chance:
    e"выбрать не можешь!"
    jump next

label next:
    "конец"


    return