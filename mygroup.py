groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
    print('\n')

def print_sr_chach(sr_znach, students):
    for student in students:
        if sum(student['marks']) / len(student['marks']) >= int(sr_znach):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


if __name__ == '__main__':
    print_students(groupmates)
    sr_znach = input('Введите среднее значение оценок студентов: ')
    print_sr_chach(sr_znach, groupmates)