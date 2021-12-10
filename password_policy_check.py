
def check_policy(min_limit:int, max_limit:int, char:str, pwd:str)->bool:
	ch_count = pwd.count(char)  # char count in pwd
	if ch_count >= min_limit and ch_count <= max_limit:
		return True
	else:
		return False

import pickle
data = pickle.load(open('data_pwd_policy.bat', 'rb')) # 3-12 l: jgrzdzvqbrllsljfl

count = 0

for item in data:
	policy, pwd = item.split(': ') # splits '1-3 a: abcde' to policy='1-3 a' and pwd='abcde'
	limit, char = policy.split(' ') # splits '1-3 a' to limit='1-3' and char='a'
	min_limit, max_limit = tuple(map(int, limit.split('-'))) # splits '1-3' to min_limit=1 and max_limit=3 after converting them to integer values
	# print(f"{min_limit, max_limit, char, pwd}")
	count += 1 if check_policy(min_limit, max_limit, char, pwd) else 0