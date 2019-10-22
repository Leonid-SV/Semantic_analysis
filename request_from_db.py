import psycopg2
from psycopg2 import sql
from contextlib import closing

def db_execute(keyword):

    request_form = 'SELECT text FROM comments_short WHERE id = {}'

    # подключение к базе данных ToxicStackOverflow
    with closing(psycopg2.connect(dbname='ToxicStackOverflow', user='postgres', password='2409', host='localhost')) as conn:
        with conn.cursor() as cursor:

            # запрос по словам из списка
            result = []
            if isinstance(keyword, list):
                for kw in keyword:
                    query = request_form.format(kw)
                    cursor.execute(query)

                    for row in cursor:
                        result.append(row)
            else:
                query = request_form.format(keyword)
                cursor.execute(query)

                for row in cursor:
                    result.append(row)
        conn.commit()
    return result

# print('+'*60)
# print(db_execute([2, 16]))
# print('+'*60)

import webapp
from webapp import create_app

app = create_app()
with app.app_context():

    pass


