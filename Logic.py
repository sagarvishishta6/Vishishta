from typing import Union

def return_one():
    return {"1"}

def return_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
