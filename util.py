def load_input(_in="1.in") -> list[str]:
    with open(_in,"r") as file:
       return [x for x in file]

