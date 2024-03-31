from typing import Tuple

def total_salary(path: str) -> Tuple[int, float]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]
        
        summ = sum(int(line.split(",")[1]) for line in lines)
    except FileNotFoundError as fnfe:
        print(fnfe.strerror)
    except Exception as ex:
        print("Something going wrong! :skull_and_crossbones:")
    else:
        return tuple([summ, summ / 2])