#! /usr/bin/env python3

import psycopg2

DBNAME = "news"


def queries(sql_query):
    """Opens and connects to database, run query and return results.

    Args:
        sql_query: String to query the database.
    Returns:
        results: Returns database cursor objects.
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results


def popular_articles():
    """Selects and prints the most popular articles."""
    query = "SELECT articles.title, COUNT(*) AS views " \
            "FROM articles INNER JOIN log ON log.path " \
            "LIKE concat('%', articles.slug, '%') " \
            "WHERE log.status NOT LIKE '%404%' GROUP BY articles.title " \
            "ORDER BY views DESC limit 3;"
    top_three = queries(query)
    print('The most popular articles of all time are:')
    for record in top_three:
        print('\t' + '"' + str(record[0]) + '"' + ' --- '
              + str(record[1]) + ' views')


def most_popular_author():
    """Selects and prints the most top three most popular authors."""
    query = "SELECT authors.name, COUNT(*) AS views " \
            "FROM articles INNER JOIN authors ON " \
            "articles.author = authors.id INNER JOIN log ON " \
            "log.path LIKE concat('%', articles.slug, '%')" \
            "WHERE log.status NOT LIKE '%404%' GROUP BY authors.name " \
            "ORDER BY views DESC"
    most_popular = queries(query)
    print('The most popular article authors of all time are')
    for record in most_popular:
        print('\t' + str(record[0]) + ' --- '
              + str(record[1]) + ' views')


def down_time():
    """Selects and prints dates that have had more than 1% error rate"""
    query = "select * from (select to_char(time, 'MONTH FMDD, YYYY') as dt, " \
            "ROUND((COUNT(*) filter (WHERE status like '%404%') *" \
            " 100)::numeric / count(*) filter (where status like " \
            "'%200%'), 2) as error_rate from log group by to_char(time, " \
            "'MONTH FMDD, YYYY')) ss where error_rate >= 1;"
    error_times = queries(query)
    print('On which days did more than 1% of requests lead to errors?')
    for record in error_times:
        print('\t' + str(record[0]) + ' with '
              + str(record[1]) + '% errors')


if __name__ == "__main__":
    popular_articles()
    most_popular_author()
    down_time()
