num_lst = input()
new_list = [int(n) for n in num_lst]
running_total = [sum(new_list[:i + 1]) for i in range(len(num_lst))]
print(running_total)
