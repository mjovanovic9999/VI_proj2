from random import shuffle
import re


def read_questions_from_file(file_path: str) -> dict[str, tuple[int, int, str, str, tuple[str, str, str]]]:
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
                first_line_split[2]), split_question[1], split_question[2], (split_question[3], split_question[4], split_question[5]))

    return question_dict


def store_test_combinations_to_files(test_name: str, test_folder: str, number_of_combinations: int, question_dict: dict[str, tuple[int, int, str, str, tuple[str, str, str]]], test_combinations: list[tuple[tuple[int, int, int], str]]) -> None:
    for combination in range(1, number_of_combinations + 1):
        new_test_name = test_name+"_kombinacija_"+str(combination)
        store_test_to_file(new_test_name, test_folder,
                           combination, question_dict, test_combinations)


def store_test_to_file(test_name: str, test_folder: str, current_combination: int, question_dict: dict[str, tuple[int, int, str, str, tuple[str, str, str]]], test_combinations: list[tuple[tuple[int, int, int], str]]):
    with open(f'{test_folder}\\{test_name}.txt', "w") as file:
        counter = 1
        current_test_combination = [
            question for question in test_combinations if question[0][0] == current_combination]
        current_test_combination.sort(key=lambda x: x[0][1])
        for question in current_test_combination:
            question_data = question_dict[question[0][2]]
            answers = {}
            wrong_answer_options = ["A", "B", "C", "D"]
            answers[f'{question[1]})'] = question_data[3]
            wrong_answer_options.remove(question[1])
            wrong_answers = list(question_data[4])
            for wrong_answer_option in wrong_answer_options:
                shuffle(wrong_answers)
                answers[f'{wrong_answer_option})'] = wrong_answers.pop()
            file.write(f'{counter}. {question_data[2]}\n')
            counter += 1
            for answer_option in sorted(list(answers.keys())):
                file.write(f'\t{answer_option} {answers[answer_option]}\n')
