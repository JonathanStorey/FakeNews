import stringFunctions
from stringFunctions import addQuestionMark

def addExclamation(name: str) -> str:
    return f"{name}!"

print(addExclamation("Hello, World"))
print(stringFunctions.addQuestionMark("Goodbye, Planet"))
print(addQuestionMark("Goodbye, Planet"))