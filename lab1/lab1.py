import random

def removeDuplicates(list):
	ln = len(list)
	new_list = []
	mp = {i : 0 for i in list}
	for i in range(ln):
		if mp[list[i]] == 0:
			new_list.append(list[i])
			mp[list[i]] = 1
	return new_list

def sortList(list):
	ln = len(list)
	for i in range(ln):
		for j in range(ln-1):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]

r = random.choices(range(30), k=20)
print(f'Generated a random integer list: {r}')		

no_dup_list = removeDuplicates(r)
print(f'Without duplicates: {no_dup_list}')

sortList(no_dup_list)
print(f'Sorted: {no_dup_list}')