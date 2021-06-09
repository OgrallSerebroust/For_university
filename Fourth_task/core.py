import pymysql
from lxml import etree


def get_theatres_data():
    connection = pymysql.connect(host="localhost", user="athena", password="0MechTa8", database="for_xml",
                                 charset="utf8", cursorclass=pymysql.cursors.DictCursor)
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM theatres")
        return cursor.fetchall()


def get_shows_data():
    connection = pymysql.connect(host="localhost", user="athena", password="0MechTa8", database="for_xml",
                                 charset="utf8", cursorclass=pymysql.cursors.DictCursor)
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM shows")
        return cursor.fetchall()


def get_visitors_data():
    connection = pymysql.connect(host="localhost", user="athena", password="0MechTa8", database="for_xml",
                                 charset="utf8", cursorclass=pymysql.cursors.DictCursor)
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM visitors")
        return cursor.fetchall()


def dump_theatres(theatres_data, main):
    theater = etree.SubElement(main, "theaters")
    for row in theatres_data:
        for key in row.keys():
            theater_item = etree.SubElement(theater, key)
            theater_item.text = str(row[key])


def dump_shows(shows_data, main):
    show = etree.SubElement(main, "shows")
    for row in shows_data:
        for key in row.keys():
            show_item = etree.SubElement(show, key)
            show_item.text = str(row[key])


def dump_visitors(visitors_data, main):
    visitor = etree.SubElement(main, "visitors")
    for row in visitors_data:
        for key in row.keys():
            visitor_item = etree.SubElement(visitor, key)
            visitor_item.text = str(row[key])


if __name__ == "__main__":
    data_about_theatres = get_theatres_data()
    data_about_shows = get_shows_data()
    data_about_visitors = get_visitors_data()
    root = etree.Element('for_xml')
    dump_theatres(data_about_theatres, root)
    dump_shows(data_about_shows, root)
    dump_visitors(data_about_visitors, root)
    etree.ElementTree(root).write("database_dump.xml", encoding="utf-8")
