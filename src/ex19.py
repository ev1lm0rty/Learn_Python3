def cheese(count,boxes):
    print(f"You have {count} cheese!")
    print(f"You have {boxes} boxes!")
    print("Damn")

print("We can just give the function numbers directly:")
cheese(20,30)

print("OR, we can use variables from our script:")
pp = 10
qq = 50

cheese(pp,qq)

print("We can even do math inside too:")
cheese(5+10,60/3)

print("And we can combine two variables also:")
cheese(pp+100, qq+10)
