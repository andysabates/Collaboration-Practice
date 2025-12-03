my_tpl = (1, 2, 3)

list_my_tpl = list(my_tpl)  # new variable containing the conversion into a list

list_my_tpl[2] = 4

my_tpl = tuple(list_my_tpl)

my_tpl