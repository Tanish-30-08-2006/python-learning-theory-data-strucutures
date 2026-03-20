def remove(l,word):
    n=[]
    for i in range(0,len(l),1):
        if not(l[i]==word):
            n.append(l[i])
    return n

l=list(input("enter elements with space: ").split())
word=input("word to cut : ")
print(l)
print(remove(l,word))

