# Пользователь вводит предложение,
# заменить все пробелы на "-" 2-мя способами

user_string = input("Введите строку: ")

# я понял задание так, что необходимо "получить" измененную строку,
# а не просто вернуть измененную
changed_string1 = user_string.replace(" ", "-")  # вариант 1

temp_string = user_string.split(" ")  # вариант 2, временное удаление пробелов
changed_string2 = "-".join(temp_string)  # вариант 2, склейка с вставлением "-"

# в задании не было необходимости вывода измененной строки, просто для проверки :-)
print(changed_string1)
print(changed_string2)

# если просто вернуть строку с замененными символами то:
# print(user_string.replace(" ", "-"))

# и второй вариант, но в таком виде хуже читается
# print("-".join(user_string.split(" ")))
