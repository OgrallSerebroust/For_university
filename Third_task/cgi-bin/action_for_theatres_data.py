from cgi import FieldStorage
from neo4j import GraphDatabase

our_data_from_form = FieldStorage()
name_of_theatre = our_data_from_form.getfirst("name_of_theatre", "Не задано")
place_of_theatre = our_data_from_form.getfirst("place_of_theatre", "Не задано")
how_many_visitors = our_data_from_form.getfirst("how_many_visitors", "Не задано")


def add_data_to_bd(self, name, place, visitors):
    self.run("CREATE(theatre:Theatre)"
             "SET theatre.name = $name, theatre.place = $place, theatre.visitors = $visitors", name=name, place=place, visitors=visitors)


driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "admin"))
with driver.session() as session:
    session.write_transaction(add_data_to_bd, name_of_theatre, place_of_theatre, how_many_visitors)
driver.close()
print("Content-type: text/html")
print()
print("""
<!DOCTYPE HTML>
<html>
    <head>
        <link href="../css/style.css" type="text/css" rel="stylesheet">
        <meta charset="utf-8">
    </head>
    <body>
        <div id="main_part_of_bad_page">
            <div id="text_complete">
                Ваши данные отправлены!<br>Вы можете ознакомиться с ними на специальной странице!
            </div>
            <div id="buttons_of_bad_page">
                <a href = "core.py">
                    Вернуться на главную!
                </a>
            </div>
        </div>
    </body>
</html>
""")
