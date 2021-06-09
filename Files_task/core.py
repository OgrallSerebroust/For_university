a = []
with open("dictionary.txt", "r", encoding="utf-8") as data_from_file:
    for line in data_from_file:
        a.append(line[:-1].lower())
    a.sort()
with open("sorted_dictionary.txt", "w", encoding="utf-8") as final_file:
    for _ in a:
        final_file.write(_ + "\n")
