
import math

def power_of_2(n, k):
    if (k == 1):
        temp = math.log2(n)
        if (len(str(temp)) == 3):
            return "YES"
        else:
            return "NO"
    if (n < k):
        return "NO"
    minimum_number = n - k
    power_of_2_lst = []
    for i in range(minimum_number):
        temp_power = 2 ** 1
        if temp_power < minimum_number:
            power_of_2_lst.append(i)
        else:
            break
    print(power_of_2_lst)

    


if __name__ == "__main__":
    n, k = str.split(input())
    n = int(n)
    k = int(k)
    # print(f"n is {n}")

    power_of_2(n,k) 
    
    