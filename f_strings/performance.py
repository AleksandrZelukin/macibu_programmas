import time
from random import shuffle
from string import Template
from datetime import datetime as dt
year = 365.25

planet = {
    "name": "Земля",
    "radius": 6378000,
    "mass": 5.9726*10**24
}

now = dt.now()


def old_style():
    return "Сегодня %s.\n" \
            "Мы живём на планете %s. Её радиус %d км., а масса %.3e.\n" \
            "Период обращения планеты вокруг Солнца %d дней." % (
    now.strftime("%d.%m.%Y"),
    planet["name"],
    planet["radius"] / 1000,
    planet["mass"],
    round(year)
)


def concat_style():
    return "Сегодня " + now.strftime("%d.%m.%Y") + ".\n" \
           "Мы живём на планете " + planet["name"] + ". Её радиус " + str(int(planet["radius"] / 1000)) + " км., а масса " + str(planet["mass"]) + "\n" \
           "Период обращения планеты вокруг Солнца " + str(round(year)) + " дней."


def new_style():
    return "Сегодня {now:%d.%m.%Y}.\n" \
            "Мы живём на планете {name}. Её радиус {radius} км., а масса {mass:.3e}\n" \
            "Период обращения планеты вокруг Солнца {year} дней.".format(
    now=now, name=planet["name"], radius=int(planet["radius"] / 1000), mass=planet["mass"], year=round(year))


def template_style():
    return Template("Сегодня $now.\n"
            "Мы живём на планете $name. Её радиус $radius км., а масса $mass\n"
            "Период обращения планеты вокруг Солнца $year дней.").substitute(
    now=now.strftime("%d.%m.%Y"), name=planet["name"], radius=int(planet["radius"] / 1000),
    mass=planet["mass"], year=round(year))


def f_style():
    return f"Сегодня {now:%d.%m.%Y}.\n" \
           f"Мы живём на планете {planet['name']}. Её радиус {int(planet['radius'] / 1000)} км., а масса {planet['mass']:.3e}\n" \
           f"Период обращения планеты вокруг Солнца {round(year)} дней."


if __name__ == "__main__":
    styles = [concat_style, old_style, template_style, new_style, f_style]
    shuffle(styles)
    for style in styles:
        t0 = time.time()
        for i in range(100000):
            style()
        t1 = time.time()
        total = t1 - t0
        print(style.__name__, total)


