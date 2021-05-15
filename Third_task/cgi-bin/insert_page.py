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
                    <input type="text" name="name_of_theatre">
                    <input type="text" name="place_of_theatre">
                    <input type="submit">
                </form>
            </div>
            <div id="form_of_shows" class="forms">
                <form>
                    <input type="text" name="name_of_show">
                    <input type="submit">
                </form>
            </div>
            <div id="form_of_visitors" class="forms">
                <form action="/cgi-bin/action_for_visitors_data.py">
                    <input type="text" name="name_of_visitor">
                    <input type="text" name="age_of_visitor">
                    <input type="text" name="which_theatre">
                    <input type="submit">
                </form>
            </div>
        </div>
    </body>
</html>
""")
