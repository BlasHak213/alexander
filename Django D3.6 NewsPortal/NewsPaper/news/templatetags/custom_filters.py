from django import template


register = template.Library()


@register.filter()
def censor(value, censor_words):
    words_list = [word.strip() for word in censor_words.split(',')]
    for word in words_list:
        value = value.replace(word, '*' * len(word), -1)
    return value
