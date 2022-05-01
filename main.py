"""Определить класс с именем MARSH, содержащий следующие поля:
- название начального пункта маршрута;
- название конечного пункта маршрута;
- номер маршрута.
Определить методы доступа к этим полям и перегруженные операции извлечения
и вставки для объектов типа MARSH.

- ввод с клавиатуры данных в массив, состоящий из 8(сделал для 4) объектов MARSH;
- записи должны быть упорядочены по номерам маршрутов;
- вывод на экран информации о маршруте, номер которого введен с клавиатуры;
- если таких маршрутов нет, выдать на дисплей соответствующее сообщение.
"""


class Marsh:
    def __init__(self, start, end, number):
        if not isinstance(number,int):
            print("номер не корректен")
            self.__del__()
        self.__start = start
        self.__end = end
        self.__number = number
    def __del__(self):
        pass

    @property
    def start(self, val):
        self.__start = val

    @property
    def end(self, val):
        self.__end = val

    @property
    def number(self, val):
        self.__number = val

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end
    @property
    def number(self):
        return self.__number

def new_marsh() -> Marsh:
    try:
        start, end = input("начало и конец маршурта: ").split()
    except ValueError:
        print("error")
    try:
        number = int(input("номер маршута "))
    except ValueError:
        print("номер неверен")
        return
    return Marsh(start,end,number)
def sort_marsh(classes_list) -> list:
    try:
        return classes_list.sort(key=lambda el:el.number)
    except AttributeError:
        print("номер введен не верно")
        return
"""москва питер 
    4
    кемерово нск
    5
    юрга питер
    6
    курск ростов
    1"""

def main():
    classes_list = []
    print("Добавьте 4 обьекта")
    for i in range(4):
        classes_list.append(new_marsh())
    sort_marsh(classes_list)
    while True:
        print("Ввести \n1 - изменить значение маршрута\n2 - удалить\n3 - добавить\n4 - найти маршрут\n5 - посмотреть список\n6 - выйти")
        get_input = input(">>> ")
        if get_input == "1":
            index=int(input("индекс элемента: "))
            change=input("что заменить: ")
            if change=="start":
                classes_list[index].start=input(">>> ")
            elif change=="end":
                classes_list[index].end=input(">>> ")
            elif change=="number":
                classes_list[index].number=input(">>> ")
            else:
                continue
        elif get_input=="2":
            index=int(input("индекс элемента: "))
            try:
                del classes_list[index]

            except IndexError:
                print("слишком большой индекс")
                continue
            sort_marsh(classes_list)
        elif get_input=="3":
                classes_list.append(new_marsh())
                sort_marsh(classes_list)
        elif get_input=="4":
            find=int(input("номер маршрута: "))
            flag=0
            for i in classes_list:
                if i.number == find:
                    print(f"start={i.start},end={i.end},number={i.number}")
                    flag+=1
            if flag==0:
                print("нет таких маршрутов")
        elif get_input=="5":
            j=0
            for i in classes_list:
                print(f"{j}: start={i.start}, end={i.end}, number={i.number}")
                j+=1
        elif get_input=="6":
            break
        else:
            continue

if __name__ == '__main__':
    main()
