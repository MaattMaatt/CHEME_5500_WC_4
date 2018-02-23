# did sum between 1 and 100 inclusive since it wasnt specified

allnum = range(1,101)
evennum = allnum[1::2]

sum = 0
for i in range(len(evennum)):
    sum += evennum[i]

print sum