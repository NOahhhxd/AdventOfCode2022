#### PART 1 #####
print("-----------Part 1---------------")
# oneliner 
print(sum([(ord(x)+23==(ord(y)))*(ord(y)-ord("W")+3) + ((ord(x)+21)==ord(y) or (ord(x)+24)==ord(y))*((ord(y)-ord("W"))+6) + (((ord(x)+22)==ord(y)) or (ord(x)+25)== ord(y))*(ord(y)-ord("W")) for x,y, in [i.split(" ") for i in open("day2.data","r").read().split("\n")]]))


# fomer idea
sum_ = 0
for val in open("day2.data","r").read().split("\n"):
    x,y = val.split(" ")
    sum_ += (ord(x)+23==(ord(y)))*(ord(y)-ord("W")+3) + ((ord(x)+21)==ord(y) or (ord(x)+24)==ord(y))*((ord(y)-ord("W"))+6) + (((ord(x)+22)==ord(y)) or (ord(x)+25)== ord(y))*(ord(y)-ord("W"))
   
   
print(sum_)





#### Part 2 ####
print("-----------Part 2---------------")

# oneliner 
print(sum([(y=="Y")*(ord(x)-ord("A")+1+3)+(y=="X")*((ord(x)-ord("A")+2)%3+1)+(y=="Z")*((ord(x)-ord("A")+1)%3+1+6) for x,y in [i.split(" ") for i in open("day2.data","r").read().split("\n")]]))

# former idea
sum_ = 0
for val in open("day2.data","r").read().split("\n"):
    x,y = val.split(" ")
    sum_ += (y=="Y")*(ord(x)-ord("A")+1+3)+(y=="X")*((ord(x)-ord("A")+2)%3+1)+(y=="Z")*((ord(x)-ord("A")+1)%3+1+6)
print(sum_)