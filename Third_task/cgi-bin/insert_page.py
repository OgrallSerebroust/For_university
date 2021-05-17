#!/usr/bin/env python3

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
            <div id="form_of_theatres" class="forms">
                <form action="/cgi-bin/action_for_theatres_data.py">
                    <input type="text" name="name_of_theatre" placeholder="Название театра">
                    <input type="text" name="place_of_theatre" placeholder="Местоположение театра">
                    <input type="text" name="how_many_visitors" placeholder="Сколько возможно посетителей">
                    <input type="submit" value="Отправить" class="buttons_in_form">
                </form>
            </div>
            <div id="form_of_shows" class="forms">
                <form action="/cgi-bin/action_for_shows_data.py">
                    <input type="text" name="name_of_show" placeholder="Название мероприятия">
                    <input type="text" name="how_many_visitors" placeholder="Сколько возможно посетителей">
                    <input type="text" name="which_theatre" placeholder="В каком театре проводится">
                    <input type="submit" value="Отправить" class="buttons_in_form">
                </form>
            </div>
            <div id="form_of_visitors" class="forms">
                <form action="/cgi-bin/action_for_visitors_data.py">
                    <input type="text" name="name_of_visitor" placeholder="Ф.И.О">
                    <input type="text" name="age_of_visitor" placeholder="Возраст">
                    <!--<input type="text" name="which_theatre" placeholder="Какой театр посещал(а)">-->
                    <input type="text" name="which_show" placeholder="Какое мероприятие посещал(а)">
                    <input type="submit" value="Отправить" class="buttons_in_form">
                </form>
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
