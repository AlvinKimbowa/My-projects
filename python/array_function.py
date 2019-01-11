lucky_numbers = [4, 87, 63, 58, 13, 5]
friends = ["kevin", "Kent", "Kent", "Kent", "Floso", "Oscar", "Paul"]
friends.sort()
print(friends)

friends.extend(lucky_numbers)
friends.append("creed")
friends.insert(2, "Kelly")
friends.remove("Floso")
# friends.clear()           deletes everything

print(friends.index("creed"))   #prints position of an element

friends.pop()       # removes the last element
print(friends)

print(friends.count("Kent"))

lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

lucky_numbers2 = friends.copy()
print(lucky_numbers2)