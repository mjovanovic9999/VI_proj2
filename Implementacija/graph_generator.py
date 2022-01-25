from copy import deepcopy


def generate_graph(question_dict: dict[str, tuple[int, int, str, tuple[str, str, str, str]]], number_of_questions: int, number_of_easy_questions: int, number_of_medium_questions: int, number_of_hard_questions: int, question_groups: list[int]) -> dict:
    remaining_question_groups = deepcopy(question_groups)
    questions = []
    generated_graph = {}
    
    return generated_graph

def append_random_question_to_list_by_difficulty_and_question_group(questions: list, difficulty: int, question_groups: list[int]) -> None:
    #question_with_selected_difficulty = [question for question ]
    pass