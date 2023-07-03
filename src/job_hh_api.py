import requests
import json
import csv


class HeadHunterAPI():
    """ Класс для работы с API HeadHunter"""


    def __init__(self):
        """
        Инициализация класса
        """
        self.url = "https://api.hh.ru/vacancies"


    def get_vacancies(self, page: int, count_page=1):
        """
        Подключение к API  и получени информации о вакансии
        vacancies: ключвое слово для поиска вакансии
        params: параметры поиска
        'page': Индекс страницы поиска на HH
        'per_page': Кол-во вакансий на 1 странице
        'employer_id': id компании
        """
        self.page = page
        self.count_page = count_page

        with open('src/employer_id.json', 'r') as f:
            employers = json.load(f)

        results = []

        for employer in employers['employers']:

            for i in range(page+1):

                params = {
                    'employer_id': employer['id'],
                    'page': i,
                    'per_page': {count_page}
                }

                response = requests.get(self.url, params=params)

                if response.status_code != 200:
                    print(response.raise_for_status())
                    raise ParsingError(f"Ошибка получения вакансии")

                results.append(response.json())
        return results


    def formatted_vacancy(self):
        """
        Обработка данных полученных из API HeadHanter
        возвращает список словарей с вакансиями с ключами:
        "title": название вакансии
        "url": сслыка на вакансию
        "salary_from": зарплата от
        "salary_to": зарплата до
        "requirement": требования
        """
        v = HeadHunterAPI()
        vacansies_hh = v.get_vacancies(self.page, self.count_page)

        vacancy_list = []
        counter = 0

        for i in range(len(vacansies_hh)):

            vac = vacansies_hh[i]['items'][0]

            vacancy_salary = vac['salary']

            if vacancy_salary == None:
                vacancy_list.append(
                    (counter+1, counter, vac['name'], 0, 0, vac['alternate_url'], vac['snippet']['requirement'])
                )
                counter +=1

            elif vacancy_salary['from'] == None:
                vacancy_list.append(
                    (counter+1, counter, vac['name'], 0, vacancy_salary["to"], vac['alternate_url'], vac['snippet']['requirement'])
                )
                counter += 1

            elif vacancy_salary['to'] == None:
                vacancy_list.append(
                    (counter+1, counter, vac['name'], vacancy_salary["from"], 0, vac['alternate_url'], vac['snippet']['requirement'])
                )
                counter += 1

            else:
                vacancy_list.append(
                    (counter+1, counter, vac['name'], vacancy_salary["from"], vacancy_salary["to"], vac['alternate_url'], vac['snippet']['requirement'])
                )
                counter +=1


        return vacancy_list

    def formatted_employer(self):
        """
        Обработка данных полученных из API HeadHanter
        возвращает список кортежей с названием компании и id
        """
        v = HeadHunterAPI()
        vacansies_hh = v.get_vacancies(self.page, self.count_page)

        employer_list = []
        counter = 0

        for i in range(len(vacansies_hh)):

            employer_list.append((counter, vacansies_hh[i]['items'][0]['employer']['name']))
            counter += 1

        return employer_list

    def add_employer(self, employers):
        """
        Добавление вакансии в файл csv - 'employer.csv', созхранение в формате таблицы
        с колонками "id_employer", "company_name"
        """

        with open('employer.csv', "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(
                ("id_employer", "company_name")
            )

        for employer in employers:
            with open("employer.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    employer
                )

    def add_vacancy(self, vacancy):
        """
        Добавление вакансии в файл csv - 'vacancy.csv', сохранение в формате таблицы
        с колонками "id_vacancy", "id_employer", "vacancy_name", "salary_from", "salary_to", "url", "requirements"
        """

        with open('vacancy.csv', "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(
                ("id_vacancy", "id_employer", "vacancy_name", "salary_from", "salary_to", "url", "requirements")
            )

        for vac in vacancy:
            with open("vacancy.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    vac
                )





