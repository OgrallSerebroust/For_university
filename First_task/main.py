min_positive_speed, second_min_positive_speed, second_max_negative_speed, max_negative_speed, min_negative_speed, max_positive_speed = 10000, 10000, 10000, 0, 0, 0
if __name__ == '__main__':
    with open("data_in.txt", "r", encoding="utf-8") as data_from_file:
        data_from_file.readline()
        for _ in data_from_file:
            if int(_) > 0:
                if int(_[1::]) > max_positive_speed:
                    max_positive_speed = int(_[1::])
                if int(_[1::]) <= min_positive_speed:
                    second_min_positive_speed = min_positive_speed
                    min_positive_speed = int(_[1::])
                if second_min_positive_speed >= int(_[1::]) > min_positive_speed:
                    second_min_positive_speed = int(_[1::])
            elif int(_) < 0:
                if int(_[1::]) > min_negative_speed:
                    min_negative_speed = int(_[1::])
                if int(_[1::]) >= max_negative_speed:
                    second_max_negative_speed = max_negative_speed
                    max_negative_speed = int(_[1::])
                if second_max_negative_speed >= int(_[1::]) > max_negative_speed:
                    second_max_negative_speed = int(_[1::])
        multiplication_of_positives = int(min_positive_speed * second_min_positive_speed)
        multiplication_of_positive_and_negative = int("-" + str(max_positive_speed * min_negative_speed))
        multiplication_of_negatives = int(max_negative_speed * second_max_negative_speed)
        if multiplication_of_positives == 0:
            multiplication_of_positives = 100000000
        if multiplication_of_positive_and_negative == 0:
            multiplication_of_positive_and_negative = 100000000
        if multiplication_of_negatives == 0:
            multiplication_of_negatives = 100000000
        if multiplication_of_positives < multiplication_of_positive_and_negative and multiplication_of_positives < multiplication_of_negatives:
            print(multiplication_of_positives)
        elif multiplication_of_positive_and_negative < multiplication_of_positives and multiplication_of_positive_and_negative < multiplication_of_negatives:
            print(multiplication_of_positive_and_negative)
        else:
            print(multiplication_of_negatives)
