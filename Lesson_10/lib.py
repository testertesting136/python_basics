from rich import print
from rich import inspect

print("[red]Hello[/red], [bold purple]from Rich![/bold purple]")
list_1 = [1, 2, 3, 4]
print(list_1)

inspect(list_1, help=True, methods=True)