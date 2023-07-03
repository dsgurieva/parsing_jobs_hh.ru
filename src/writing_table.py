import psycopg2
import csv

class WritingTable():
    """Класс для запись данных в базу данных """

    def __init__(self):

        self.conn = CONN

    def writing_table_employer(self):
        """Запись данных в таблицу employer"""

        with self.conn:
            with self.conn.cursor() as cursor:
                with open('employer.csv', 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader)

                    for row in reader:
                        cursor.execute(
                            "INSERT INTO employer (id_employer,company_name) VALUES (%s, %s)", row
                            )




    def writing_table_vacancy(self):
        """Запись данных в таблицу vacancy"""

        with self.conn:
            with self.conn.cursor() as cursor:
                 with open('vacancy.csv', 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader)

                    for row in reader:
                        cursor.execute(
                            "INSERT INTO vacancy (id_vacancy,id_employer,vacancy_name,salary_from,salary_to,url,requirements) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)", row
                        )

        self.conn.close()

