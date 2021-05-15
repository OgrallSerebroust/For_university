from cgi import FieldStorage
from neo4j import GraphDatabase

our_data_from_form = FieldStorage()
name_of_visitor = our_data_from_form.getfirst("name_of_visitor", "Не задано")
age_of_visitor = our_data_from_form.getfirst("age_of_visitor", "Не задано")
which_theatre = our_data_from_form.getfirst("which_theatre", "Не задано")


def add_friend(tx, name, age, theatre):
    tx.run("CREATE (visitor:Visitor{name: $name, age: $age})", name=name, age=age)
    tx.run("""MATCH (a: Visitor), (b: Theatre) WHERE a.name = $name AND b.name = $theatre CREATE (a)-[r: Посетитель]->(b);""", name=str(name), theatre=str(theatre))


driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "admin"))
with driver.session() as session:
    session.write_transaction(add_friend, name_of_visitor, age_of_visitor, which_theatre)
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
