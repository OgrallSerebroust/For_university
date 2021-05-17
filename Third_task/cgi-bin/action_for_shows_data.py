from cgi import FieldStorage
from neo4j import GraphDatabase

our_data_from_form = FieldStorage()
name_of_show = our_data_from_form.getfirst("name_of_show", "Не задано")
how_many_visitors = our_data_from_form.getfirst("how_many_visitors", "Не задано")
which_theatre = our_data_from_form.getfirst("which_theatre", "Не задано")


def add_data_to_bd(self, name, visitors, which_theatre):
    self.run("MERGE (show: Show{name: $name, visitors: $visitors})", name=name, visitors=visitors)
    self.run("""MATCH (a: Show), (b: Theatre) WHERE a.name = $name AND b.name = $which_theatre CREATE (a)-[r: Проводится]->(b);""", name=name, which_theatre=which_theatre)


driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "admin"))
with driver.session() as session:
    session.write_transaction(add_data_to_bd, name_of_show, how_many_visitors, which_theatre)
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
