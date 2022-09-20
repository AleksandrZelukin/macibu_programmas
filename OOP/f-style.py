def old_style(name, age):
    return "Привет, меня зовут %s. Мне %d лет." % (name, age)


def concat_style(name, age):
    return "Привет, меня зовут " + name + ". Мне " + str(age) + " лет."


def new_style(name, age):
    return "Привет, меня зовут {}. Мне {} лет.".format(name, age)


def template_style(name, age):
    return Template("Привет, меня зовут $name. Мне $age лет.").substitute(name=name, age=age)


def f_style(name, age):
    return f"Привет, меня зовут {name}. Мне {age} лет."
    return "Привет, меня зовут", name, "Мне", age, "лет."

a=f_style("Anna", 18)
print(a)
