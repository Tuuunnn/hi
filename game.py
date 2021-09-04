
def find_num_prime(num):
    non_prime=[]
    for i in range(2,num+1):
        cut = 0
        for j in range(2, i+1):
            if i%j==0:
                cut+=1
            if cut>1:
                non_prime.append(i)
                break
           
    return non_prime

print(find_num_prime(1000))

