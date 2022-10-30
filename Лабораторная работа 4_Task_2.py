def get_count_char(str_):
    frequency_dict = {}
    DEFULT_COUNT = 0
    str_ = str_.lower()
    for word in str_:
        if word.isalpha():
            frequency_dict[word] = frequency_dict.get(word, DEFULT_COUNT)+1
    return frequency_dict
def percentage_(dict_):
    percentage_dict = {}
    for key, values in dict_.items():
        percentage_dict[key] = percentage_dict.get(key, values/sum(dict_.values()))
    return percentage_dict
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percentage_(get_count_char(main_str)))
