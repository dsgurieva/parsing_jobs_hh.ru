from src.dbmanager import DBManager
from src.writing_table import WritingTable
from src.job_hh_api import HeadHunterAPI


def main():
    def data_recording():
        # Создание экземпляра класса HeadHunterAPI()
        hh = HeadHunterAPI()

        # Получение списка вакансий
        hh.get_vacancies(2)

        # Форматирование списка вакансий
        hh_employer = hh.formatted_employer()
        hh_vacancy = hh.formatted_vacancy()

        # Добавление вакансий в csv файл
        hh.add_employer(hh_employer)
        hh.add_vacancy(hh_vacancy)

        # Создание экземпляра класса WritingTable()
        wt = WritingTable()

        # Добавление данных в таблицы базы данных
        wt.writing_table_employer()
        wt.writing_table_vacancy()

    while True:
        user = input(f"Для получения данных и записи в базу введите - 1\n"
                     f"Для работы с данными введите - 2\n"
                     f"Для выхода нажмите - 3 ")
        if user == "1":
            data_recording()
        elif user == "2":

            while True:

                print(f"Для для продолжения работы с данными введите:\n"
                      f"1 - продолжить работу\n"
                      f"2 - выйти  ")
                user_input = input()
                if user_input == "1":
                    db = DBManager()
                    user_in = input(
                        f"При вводе вы можете получить:\n"
                        f"1 - список всех компаний и количество вакансий у каждой компании;\n"
                        f"2 - список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n"
                        f"3 - среднюю зарплату по вакансиям;\n"
                        f"4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям;\n"
                        f"5 - список всех вакансий, в названии которых содержатся переданные в метод слова, например 'python'\n"
                        f"6 - выйти\n"
                        f"Введите число: "
                    )

                    if user_in == "1":
                        print(db.get_companies_and_vacancies_count())
                    elif user_in == "2":
                        print(db.get_all_vacancies())
                    elif user_in == "3":
                        print(db.get_avg_salary())
                    elif user_in == "4":
                        print(db.get_vacancies_with_higher_salary())
                    elif user_in == "5":
                        user_key = input("Введите ключевое слово для поиска: ")
                        print(db.get_vacancies_with_keyword(user_key))
                    elif user_in == "6":
                        break
                    else:
                        user_in = input(
                            f"При вводе произошла ошибка, введите число:\n"
                            f"1 - список всех компаний и количество вакансий у каждой компании;\n"
                            f"2 - список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n"
                            f"3 - среднюю зарплату по вакансиям;\n"
                            f"4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям;\n"
                            f"5 - список всех вакансий, в названии которых содержатся переданные в метод слова, например 'python'\n"
                            f"6 - выйти\n"
                            f"Введите число: "
                        )
                elif user_input == "2":
                    break
                else:
                    user_input = input (f"Ошибка ввода, для для продолжения работы с данными введите:\n"
                                        f"1 - продолжить работу\n"
                                        f"2 - выйти  ")

        elif user == "3":
            break




if __name__ == "__main__":
    main()

