class Employee:
    def __init__(self, name, dolzhnost, zarplata, stazh):
        try:
            if not name:
                raise ValueError("Имя не может быть пустым")
            if not dolzhnost:
                raise ValueError("Должность не может быть пустой")
            if zarplata < 0:
                raise ValueError("Зарплата не может быть отрицательной")
            if stazh < 0:
                raise ValueError("Стаж не может быть отрицательным")

            self.name = name
            self.dolzhnost = dolzhnost
            self.zarplata = zarplata
            self.stazh = stazh

        except ValueError as e:
            print("Ошибка:", e)

    def info(self):
        print("Имя:", self.name)
        print("Должность:", self.dolzhnost)
        print("Зарплата:", self.zarplata, "тг")
        print("Стаж:", self.stazh, "лет")

    def pov_zarplata(self):
        if self.stazh >= 3:
            self.zarplata = self.zarplata * 1.15
            print("Повышение на 15%")
        elif self.stazh >= 2:
            self.zarplata = self.zarplata * 1.10
            print("Повышение на 10%")
        else:
            print("Повышения нет")

    def god_zarplata(self):
        return self.zarplata * 12


Daneker = Employee("Zhunus Daneker Seitgaliuly", "Программист", 700000, 3)
Zhanerke = Employee("Zhunus Zhanerke Seitgalikyzy", "Менеджер", 400000, 1)
Nurdaulet = Employee("Zhunus Nurdaulet Seitgaliuly", "Охранник", 100000, 0)

employees = [Daneker, Zhanerke, Nurdaulet]


while True:
    print("\n===== МЕНЮ =====")
    print("1. Показать всех сотрудников")
    print("2. Повысить зарплату")
    print("3. Зарплата за год")
    print("4. Найти сотрудника с наибольшим стажем")
    print("0. Выход")

    try:
        choice = input("Выберите действие: ")

        if choice == "1":
            for employee in employees:
                employee.info()
                print()

        elif choice == "2":
            for employee in employees:
                print(employee.name)
                employee.pov_zarplata()
                print("Новая зарплата:", employee.zarplata, "тг")

        elif choice == "3":
            for employee in employees:
                print(employee.name, "-", employee.god_zarplata(), "тг в год")

        elif choice == "4":
            max_employee = employees[0]

            for employee in employees:
                if employee.stazh > max_employee.stazh:
                    max_employee = employee

            print("Наибольший стаж у:", max_employee.name)
            print("Стаж:", max_employee.stazh, "лет")

        elif choice == "0":
            print("Программа завершена")
            break

        else:
            raise ValueError("Неверный выбор!")

    except ValueError as e:
        print("Ошибка:", e)
