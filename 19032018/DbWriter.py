import sqlite3

import DbWriterEroor


class DbWriter:
    def __init__(self, filename):
        self.filename = str(filename)
        self.connector = sqlite3.connect(self.filename)

    def write_in_html(self, htmlwriter, table):
        htmlwriter.add_simle_line(str(table))
        cur = self.connector.cursor()
        try:
            cur.execute(" \
                SELECT stars.name, stars.distance, companies.name,price \
                FROM  " + table + " \
                JOIN stars \
                ON star_id = stars.id \
                JOIN companies \
                ON companies.id = company_id \
            ")
        except Exception:
            print('Некорректный запрос')
            raise DbWriterEroor
        while True:
            row = cur.fetchone()
            if row is None:
                break
            htmlwriter.add_file_arr(row)
        htmlwriter.write()
        htmlwriter.close()
        self.close_connect()

    def close_connect(self):
        self.connector.close()
