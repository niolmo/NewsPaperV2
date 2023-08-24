from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int):  # проверяем, что value — это точно строка, а arg — точно
        # число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(
            f'Нельзя умножить {type(value)} на {type(arg)}')  # в случае, если кто-то неправильно воспользовался
        # нашим тегом, выводим ошибку


badWords = ['Узнайте', 'словесными', 'Lorem', 'Панграмма', ]


@register.filter(name='Censor')
def censor(value):
    text = value.split()
    for i in text:
        if isinstance(i, str) and i in badWords:
            return value.replace(i, '******')
        else:
            return value
