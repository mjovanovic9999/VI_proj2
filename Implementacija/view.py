from typing import Callable

def show_start_screen() -> None:
    print("Dobrodošli u ČŠ generator testova :)")

def read_input_untill_valid(message: str, error_message: str, condition: Callable[[str], bool]) -> str:
    read_input = input(message + ":")
    if condition(read_input):
        return read_input
    print(error_message)
    return read_input_untill_valid(message, error_message, condition)