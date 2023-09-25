class hej():
    def __init__(self) -> None:
        # hej hej
        self.todos = ["heja på svensson", "skjut INTE upp skolan"]

    def tabort_todo(self, index):
        self.todos.pop(index)

    def add_todo(self, item: str) -> None:
        self.todos.append(item)


minlista = hej()
print(minlista.todos)
minlista.tabort_todo(1)
print(minlista.todos)
item = input()
minlista.add_todo(item)
print(minlista.todos)
