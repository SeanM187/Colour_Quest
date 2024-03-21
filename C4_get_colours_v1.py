import csv

file = open("00_colour_list_hex_v3.csv", "r")
all_colours = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row (header values)
all_colours.pop(0)

# get the first 50 rows (used to develop colour
# buttons for play GUI)
print(all_colours[:50])

print("Length: {}".format(len(all_colours)))