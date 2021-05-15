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
            <div id="buttons">
                <a href = "data_page.py" style="margin-right: 1em;">
                    Посмотреть данные
                </a>
                <a href = "insert_page.py">
                    Ввести данные
                </a>
            </div>
        </div>
    </body>
</html>
""")
