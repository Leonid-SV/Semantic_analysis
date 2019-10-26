# -*- coding: utf-8 -*-
import psycopg2
from psycopg2 import sql
from contextlib import closing

def db_request(keyword):

    request_id = "SELECT id FROM posts WHERE tags LIKE '%<{}>%'"
    request_comm = "SELECT text FROM comments_s WHERE postid IN ({})"

    # подключение к базе данных ToxicStackOverflow
    with closing(psycopg2.connect(dbname='ToxicStackOverflow', user='postgres', password='2409', host='localhost')) as conn:
        with conn.cursor() as cursor:

            # запрос id по словам из списка
            id_result = []
            if isinstance(keyword, list):
                for kw in keyword:
                    query = request_id.format(kw)
                    cursor.execute(query)

                    for row in cursor:
                        id_result.append(row[0])

            else:
                query = request_id.format(keyword)
                cursor.execute(query)

                for row in cursor:
                    id_result.append(row[0])

            query_comments = request_comm.format(sql.SQL(', ').join([sql.Literal(r) for r in id_result]).as_string(conn))

            cursor.execute(query_comments)

            comm_result = []
            for r in cursor:
                comm_result.append(r[0])
                if r[0]: print(r[0])

            print(comm_result)

        conn.commit()
        conn.close()

    return comm_result


if __name__ == '__main__':
    db_request('python')


