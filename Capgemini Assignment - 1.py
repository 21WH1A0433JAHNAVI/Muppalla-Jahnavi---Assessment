inventory = [
    ["name", "category", "unit_price", "units_sold", "units_left"],
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

#total revenue
total_revenue = 0
for i in range(1, len(inventory)):
    total_revenue += inventory[i][2] * inventory[i][3]
print("Total Revenue is ", total_revenue)

print()

#low stock
for i in range(1, len(inventory)):
    if inventory[i][-1] < 5:
        print("Name is %s and Category is %s"%(inventory[i][0], inventory[i][1]))

print()

#categorywise revenue
print('{0:^12} | {1:^12} | {2:^12}'.format('Name', 'Category', 'Revenue'))
print('-'*50)
for i in range(1, len(inventory)):
    print('{0:^12} | {1:^12} | {2:^12}'.format(inventory[i][0], inventory[i][1], inventory[i][2] * inventory[i][3]))
