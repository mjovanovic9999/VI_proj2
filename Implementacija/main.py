import os
from tokenize import group
from file_manipulator import read_questions_from_file
from view import read_input_untill_valid, show_start_screen


def main() -> None:
    show_start_screen()

    file_path = read_input_untill_valid(
        "Unesite putanju fajla sa pitanjima", "Neispravna putanja fajla!", os.path.isfile)

    destination_folder = read_input_untill_valid(
        "Unesite putanju posojećeg foldera u kome će se smestiti generisani testovi", "Neispravna putanja folder!", os.path.isdir)

    question_dict = read_questions_from_file(file_path)

    number_of_tests = int(read_input_untill_valid("Unesite broj testova za generisanje",
                          "Broj testova mora biti pozitivan broj!", lambda x: x.isdigit() and int(x) > 0))

    number_of_questions = int(read_input_untill_valid("Unesite broj pitanja na testu", "Broj pitanja na testu mora biti pozitivan broj, ne veći od broja pitanja u fajlu!",
                              lambda x: x.isdigit() and int(x) > 0 and int(x) <= len(question_dict.keys())))

    number_of_easy_questions = int(read_input_untill_valid(
        "Unesite broj lakih pitanja", "Broj lakih pitanja mora biti pozitivan broj, ne veći od broja pitanja na testu!", lambda x: x.isdigit() and int(x) > 0 and int(x) <= number_of_questions))

    questions_left = number_of_questions - number_of_easy_questions

    number_of_medium_questions = 0 if questions_left <= 0 else int(read_input_untill_valid("Unesite broj srednje teških pitanja (preostala pitanja će biti kategorisana kao teška)",
                                                                   "Broj srednje teških pitanja mora biti pozitivan broj, ne veći od preostalog broja pitanja na testu!", lambda x: x.isdigit() and int(x) > 0 and int(x) <= questions_left))

    number_of_hard_questions = questions_left - number_of_medium_questions

    question_groups = []
    while not question_groups:
        [question_groups.append(group[0]) for group in question_dict.values(
        ) if group[0] not in question_groups]

        question_groups_to_exclude = read_input_untill_valid(
            "Unesite oblasti pitanja koje želite da preskočite [nijedna oblast]", "Unesite brojne vrednosti razdvojene tačno jednim blanko znakom ili prazan unos", lambda x: x == "" or x == " " or all(group.isdigit() for group in x.split(" ")))
        if question_groups_to_exclude != "" and question_groups_to_exclude != " ":
            question_groups_to_exclude = question_groups_to_exclude.split(" ")

        [question_groups.remove(int(group)) for group in question_groups_to_exclude if int(
            group) in question_groups]
        if not question_groups:
            print("Izbacili ste sve oblasti!")

    print(question_groups)


main()
