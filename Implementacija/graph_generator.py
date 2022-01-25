from copy import deepcopy
import random


def generate_graph(question_dict: dict[str, tuple[int, int, str, tuple[str, str, str, str]]],
                   number_of_easy_questions: int,
                   number_of_medium_questions: int,
                   number_of_hard_questions: int,
                   question_groups: list[int],
                   number_of_combinations: int,
                   number_of_questions: int) -> dict[tuple[int,int,int], list[tuple[int,int,int]]]:
    remaining_question_groups = deepcopy(question_groups)
    generated_graph = {}
    questions = []

    append_many_random_questions_to_list_by_difficulty_and_question_group(
        question_dict, questions, 1, remaining_question_groups, question_groups, number_of_easy_questions)
    append_many_random_questions_to_list_by_difficulty_and_question_group(
        question_dict, questions, 2, remaining_question_groups, question_groups, number_of_medium_questions)
    append_many_random_questions_to_list_by_difficulty_and_question_group(
        question_dict, questions, 3, remaining_question_groups, question_groups, number_of_hard_questions)

    for combination in range(number_of_combinations):
        add_set_of_questions_to_graph(number_of_questions,generated_graph,combination,questions)
        random.shuffle(questions)

    return generated_graph


def append_random_question_to_list_by_difficulty_and_question_group(question_dict: dict[str, tuple[int, int, str, tuple[str, str, str, str]]], questions: list, difficulty: int, remaining_question_groups: list[int], question_groups: list[int]) -> None:
    questions_with_selected_difficulty_and_valid_group = [(number_of_question, question_data[0]) for number_of_question, question_data in question_dict.items(
    ) if ((not remaining_question_groups and question_data[0] in question_groups) or question_data[0] in remaining_question_groups) and question_data[1] == difficulty]
    random_question = random.choice(
        questions_with_selected_difficulty_and_valid_group)
    if random_question[1] in remaining_question_groups:
        remaining_question_groups.remove(random_question[1])
    questions.append(random_question[0])


def append_many_random_questions_to_list_by_difficulty_and_question_group(question_dict: dict[str, tuple[int, int, str, tuple[str, str, str, str]]], questions: list, difficulty: int, remaining_question_groups: list[int], question_groups: list[int], number_of_questions: int) -> None:
    while number_of_questions > 0:
        append_random_question_to_list_by_difficulty_and_question_group(
            question_dict, questions, difficulty, remaining_question_groups, question_groups)
        number_of_questions -= 1

def add_set_of_questions_to_graph(number_of_questions: int, generated_graph: dict[tuple[int,int,int], list[tuple[int,int,int]]],current_number_of_combinations: int, questions: list[int]) -> None:
    for question in range(number_of_questions):
        new_key = (current_number_of_combinations + 1, question + 1, questions[question])
        generated_graph[new_key] = []
        for key, value in generated_graph.items():
            if  key != new_key and (key[2] == new_key[2] or key[1] == new_key[1] or (key[0] == new_key[0] and key[1] == new_key[1] - 1)):
                value.append(new_key)
                generated_graph[new_key].append(key)
