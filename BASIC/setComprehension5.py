# list comprehension
new_list = [ x for x in range(10) ]
print(new_list)

new_new_list = [ x % 3 for x in range(10) ]
print(new_new_list)

new_new_new_list = [ x + y for x in range(5) for y in range(5) ]
print(new_new_new_list)

# set comprehension
new_set = { x for x in range(10) }
print(new_set)

new_new_set_list = { x % 3 for x in range(10) }
print(new_new_set_list)

new_new_new_set_list = { x + y for x in range(5) for y in range(5) }
print(new_new_new_set_list)
