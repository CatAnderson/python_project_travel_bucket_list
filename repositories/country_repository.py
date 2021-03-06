from db.run_sql import run_sql

from models.destination import Destination
from models.country import Country


def save(country):
    sql = "INSERT INTO countries (name, continent) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        name = row['name']
        continent = row['continent']
        country_id = row['id']
        country = Country(name, continent, country_id)
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        name = result['name']
        continent = result['continent']
        country_id = result['id']
        country = Country(name, continent, country_id)
    return country


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (name, continent) = (%s, %s) WHERE id = %s"
    values = [country.name, country.continent, country.id]
    run_sql(sql, values)


