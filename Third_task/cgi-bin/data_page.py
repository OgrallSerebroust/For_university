from neo4j import GraphDatabase


def query_data_of_theatres(self):
    for name, place in self.run("MATCH (a: Theatre) RETURN a.name, a.place"):
        print("""
            <tr>
                <td>
        """ + name + """                    
                </td>
                <td>
        """ + place + """
                </td>
            </tr>
        """)


def query_data_of_shows(self):
    for name, visitors, theatre in self.run("""MATCH (b: Show)-[r: Проводится]->(c: Theatre) RETURN b.name, b.visitors, c.name"""):
        print("""
                <tr>
                    <td>
                    """ + name + """                    
                    </td>
                    <td>
                    """ + visitors + """
                    </td>
                    <td>
                    """ + theatre + """
                    </td>
                </tr>
        """)


def query_data_of_visitors(self):
    for name, age, show in self.run("""MATCH (d: Visitor)-[: Посетил]->(e: Show) RETURN d.name, d.age, e.name"""):
        print("""
                <tr>
                    <td>
                    """ + name + """
                    </td>
                    <td>
                    """ + age + """
                    </td>
                    <td>
                    """ + show + """
                    </td>
                </tr>
        """)


driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "admin"))
print("Content-type: text/html")
print()
print("""
<html>
    <head>
        <link href="../css/style.css" type="text/css" rel="stylesheet">
        <meta charset="utf-8">
    </head>
    <body>
        <div id="main_part">
            <div id="theatres_data">
                <table cellpadding=0 cellspacing=0>
                    <thead>
                        <tr>
                            <td>
                                Название театра
                            </td>
                            <td>
                                Местоположение театра
                            </td>
                        </tr>
                    </thead>
                    <tbody>
""")
with driver.session() as session:
    session.read_transaction(query_data_of_theatres)
print("""
                    </tbody>
                </table>
            </div>
            <div id="shows_data">
                <table border=0 cellpadding=0 cellspacing=0>
                    <thead>
                        <tr>
                            <td>
                                Название мероприятия
                            </td>
                            <td>
                                Количество посетителей
                            </td>
                            <td>
                                В каком театре проводится
                            </td>
                        </tr>
                    </thead>
                    <tbody>
""")
with driver.session() as session:
    session.read_transaction(query_data_of_shows)
print("""
                    </tbody>
                </table>
            </div>
            <div id="visitors_data">
                <table border=0 cellpadding=0 cellspacing=0>
                    <thead>
                        <tr>
                            <td>
                                Ф.И.О.
                            </td>
                            <td>
                                Возраст
                            </td>
                            <td>
                                Какое мероприятие посещал(а)
                            </td>
                        </tr>
                    </thead>
                    <tbody>
""")
with driver.session() as session:
    session.read_transaction(query_data_of_visitors)
print("""
                    </tbody>
                </table>
            </div>
        </div>
        <div id="home_button">
            <a href="core.py">
                На главную!
            </a>
        </div>
    </body>
</html>
""")
