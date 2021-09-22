# from prettytable import PrettyTable

# # # Specify the Column Names while creating the newly Table

# newTable = PrettyTable(["Student Name", "Class", "Subject", "Makrs"])

# # # Add rows
# newTable.add_row(["Camron", "X", "English", "91"])
# newTable.add_row(["Haris", "X", "Math", "63"])
# newTable.add_row(["Jenny", "X", "Science", "90"])
# newTable.add_row(["Bernald", "X", "Art", "92"])
# newTable.add_row(["Jackson", "X", "Science", "98"])
# newTable.add_row(["Samual", "X", "English", "88"])
# newTable.add_row(["Stark", "X", "English", "95"])

# newTable.clear_rows()

# print(newTable)

# from prettytable import PrettyTable

# columns = ["Student Name", "Class", "Subject", "Marks"]

# newTable = PrettyTable()

# # Add Columns
# newTable.add_column(columns[0], ["Jacob", "Peter", "Grenger",
# 					"Stark", "Falcon", "Matthew", "Jackson"])
# newTable.add_column(columns[1], ["X", "X", "X", "X", "X", "X", "X"])
# newTable.add_column(columns[2], ["English", "Art", "Science", "Math", "Science", "English", "English"])
# newTable.add_column(columns[3], ["91", "63", "90", "92",
# 										"98", "83", "95"])

# print(newTable)
from prettytable import PrettyTable

from prettytable import ORGMODE

# # Specify the Column Names while creating the newly Table

newTable = PrettyTable(["Student Name", "Class", "Subject", "Makrs"])

# # Add rows
newTable.add_rows( 
    [
        ["Camron", "X", "English", "91"],
        ["Haris", "X", "Math", "63"],
        ["Jenny", "X", "Science", "90"],
        ["Bernald", "X", "Art", "92"],
        ["Jackson", "X", "Science", "98"],
        ["Samual", "X", "English", "88"],
        ["Stark", "X", "English", "95"],

    ]
)
# newTable.align = 'r'
# print(newTable)

newTable.set_style(ORGMODE)
print(newTable)