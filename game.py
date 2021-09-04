
def nem(num):
    prime=[]
    for i in range(2,num+1):
        cut = 0
        for j in range(2, i+1):
            if i%j==0:
                cut+=1
            if cut>1:
                prime.append(i)
  
         
                return prime

nem(1000)

