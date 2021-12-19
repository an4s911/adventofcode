# with open("test.txt", 'r') as input_file:
with open("input.txt", 'r') as input_file:
# with open("mytest.txt", 'r') as input_file:
    input_lines = input_file.readlines()
    n = len(input_lines)
    prev_sum = None
    count = 0
    curr_char = 65
    for i in range(n):
        if i + 2 < n:
            b = [int(input_lines[i]), int(input_lines[i+1]), int(input_lines[i+2])]

            if prev_sum == None: 
                prev_sum = sum(b)
            else:
                # print("------------------")
                # print()
                # print("------------------")
                # print("Sum b:", sum(b))
                # print("prev_sum:", prev_sum)
                print(count)
                # ch = input(f"Prev: {prev_sum}\nCurr: {sum(b)}\nIs it increase?\n: ")
                # if ch.lower() in ['y', 'ye', 'yes']:
                if sum(b) > prev_sum:

                    count += 1
                prev_sum = sum(b)


            #     if sum(b) > prev_sum:
            #         count += 1
            #         # print("Count++")
            #         prev_sum = sum(b)
            # print(chr(curr_char) + ":", sum(b))
            # curr_char += 1
            
print(count) # Answer: 1571

# 213 A          
# 781 A  B        
# 762 A  B  C      
# 213    B  C  D   
# 762       C  D  E             
# 721          D  E  F          
# 123             E  F  G        
# 276                F  G       
# 325                   G      

# A: 1756 (NA)
# B: 1756 (nc)
# C: 1737 (dec)
# D: 1696 (dec)
# E: 1606 (dec)
# F: 1120 (dec)
# G: 724  (dec)
# 0