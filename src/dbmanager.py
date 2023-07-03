import psycopg2


class DBManager():
    """Класс DBManager подключается к БД Postgres"""


    def __init__(self):
        self.conn = CONN


    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании
        """

        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT employer.company_name, COUNT(vacancy.id_vacancy) AS vacancy_count FROM employer
                LEFT JOIN vacancy ON employer.id_employer = vacancy.id_vacancy GROUP BY employer.company_name;
                """
            )
            return cur.fetchall()


    def get_all_vacancies(self):
        """
         Получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию
        """
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT employer.company_name, vacancy.vacancy_name, vacancy.url FROM vacancy
                INNER JOIN employer USING (id_employer); 
                """
            )
            return cur.fetchall()


    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        """
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT AVG(salary_from) FROM vacancy
                WHERE salary_from <> 0;
                """
            )
            return cur.fetchall()


    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям.
        """
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT vacancy_name FROM vacancy
                WHERE salary_from > (SELECT AVG(salary_from) FROM vacancy WHERE salary_from <> 0);
                """
            )
            return cur.fetchall()


    def get_vacancies_with_keyword(self, word):
        """
         Получает список всех вакансий, в названии которых
         содержатся переданные в метод слова, например “python”
        """
        self.word = word
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT * FROM vacancy WHERE vacancy_name LIKE '%{self.word}%';")
            return cur.fetchall()


