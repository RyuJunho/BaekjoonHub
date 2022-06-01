time_list = []
for _ in range(4) :
    time_list.append(int(input()))

print(sum(time_list)//60)
print(sum(time_list)%60)