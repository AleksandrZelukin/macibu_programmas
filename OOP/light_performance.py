import time
from random import shuffle, choice
from string import Template


def old_style(name, age):
    return "Привет, меня зовут %s. Мне %d лет." % (name, age)


def concat_style(name, age):
    return "Привет, меня зовут " + name + ". Мне " + str(age) + " лет."


def new_style(name, age):
    return "Привет, меня зовут {}. Мне {} лет.".format(name, age)


def template_style(name, age):
    return Template("Привет, меня зовут $name. Мне $age лет.").substitute(name=name, age=age)


def f_style(name, age):
    return "Привет, меня зовут {name}. Мне {age} лет."


if __name__ == "__main__":
    styles = [concat_style, old_style, template_style, new_style, f_style]
    shuffle(styles)
    for style in styles:
        t0 = time.time()
        for i in range(300000):
            style(choice(["Иван", "Олег", "Дмитрий", "Никита", "Антон"]), choice([10, 20, 55, 13, 76]))
        t1 = time.time()
        total = t1 - t0
        print(style.__name__, total)


