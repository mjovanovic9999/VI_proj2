import re


def read_questions_from_file(file_path: str) -> dict[str, tuple[int, int, str, tuple[str, str, str, str]]]:
    question_dict = {}
    file_content = ""
    with open(file_path, 'r') as file:
        file_content = file.read()

    valid_questions: list[str] = re.findall(
        "[0-9]+\.\ [0-9]+\ [1-3]\n\".*\"\n\".*\"\n\".*\"\n\".*\"\n\".*\"[\n]?", file_content)

    for question in valid_questions:
        split_question = question.split("\n")
        first_line_split = split_question[0].split(" ")
        number_of_question = int(first_line_split[0].removesuffix("."))

        if number_of_question not in question_dict.keys():
            question_dict[number_of_question] = (int(first_line_split[1]), int(
                first_line_split[2]), split_question[1], (split_question[2], split_question[3], split_question[4], split_question[5]))

    return question_dict

