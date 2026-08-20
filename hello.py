import string
from string import addQuestionMark

def addExclamation(name: str) -> str:
    return f"{name}!"

print(addExclamation("Hello, World"))
print(string.addQuestionMark("Goodbye, Planet"))
print(addQuestionMark("Goodbye, Planet"))