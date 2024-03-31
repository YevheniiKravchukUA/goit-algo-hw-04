from typing import List, Dict

def get_cats_info(path: str) -> List[Dict[str, str]]:
    cats_list = []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            
        for line in lines:
            cats_list.append({
                "id": line.strip().split(",")[0],
                "name": line.strip().split(",")[1],
                "age": line.strip().split(",")[2]
            })
    except FileNotFoundError as fnfe:
        print(fnfe.strerror)
    except Exception:
        print("Something going wrong! :skull_and_crossbones:")
    return cats_list