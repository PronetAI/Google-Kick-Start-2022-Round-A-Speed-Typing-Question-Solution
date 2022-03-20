test_cases=int(input())
answers=[]
inc=1
for a in range(0,test_cases,1):
    i=str(input(""))
    p=str(input(""))
    p_total=len(p)
    for num in i:
        if num in p:
            p_total=p_total-1
    if p_total==0:
        answers.append("IMPOSSIBLE")
    else:
        answers.append(p_total)
for b in answers:
    print("Case #"+str(inc)+":",b)
    inc=inc+1
