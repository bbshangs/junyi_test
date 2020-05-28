str=input()

#split the input string with space
str=str.split() 

#reverse every word in the list
for i in range(len(str)):
	str[i]=str[i][::-1]

#convert the list to a string
ans=" ".join(str)

print(ans)


