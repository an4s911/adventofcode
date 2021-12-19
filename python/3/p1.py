
with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    n = len(lines[0])

    gamma_rate = ""
    epsilon_rate = ""

    for i in range(n):
        count_1 = 0
        count_0 = 0
        for line in lines:
            if line[i] == '1':
                count_1 += 1
            elif line[i] == '0':
                count_0 += 1
            else:
                print("LOL")
                break
        
        if count_1 > count_0:
            gamma_rate += "1"
            epsilon_rate += "0"
        elif count_0 > count_1:
            gamma_rate += "0"
            epsilon_rate += "1"
    
    print(gamma_rate, epsilon_rate)
    gamma_rate_dec = int(gamma_rate, 2)
    epsilon_rate_dec = int(epsilon_rate, 2)

    print(gamma_rate_dec * epsilon_rate_dec)

