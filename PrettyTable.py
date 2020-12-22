from prettytable import PrettyTable

table = PrettyTable()

table.add_column("dongwoo",["talmo", "biman"])
table.add_column("yeongil",["handsome", "sexy"])
table.align = "l"
print(table)