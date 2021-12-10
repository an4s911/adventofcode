import pickle
with open('data_sum_2020.bat', 'rb') as f:
	data = pickle.load(f)

check = False
for i in data:
	if not check:
		for j in data:
			if not check:
				for k in data:
					if i + j + k == 2020:
						print(f"{i}, {j}, {k} --> {i*j*k}")
						check = True
						break





