def sub_string(str):
    length=len(str)
    count=0
    for x in range(1,len(str)+1):
        end=x
        for y in range(length):
            print(str[y:end])
            count+=1
            end+=1
        length-=1
    print("length = ",count)
x="banana"
sub_string(x)
