for i in range (int(input())):
    skillset={}
    for j in range (int(input())):
        m,s=map(int,input().split())
        skillset[s]=m
        #sk1=min(skillset,key='10')
        print(skillset)
        print(type(skillset))