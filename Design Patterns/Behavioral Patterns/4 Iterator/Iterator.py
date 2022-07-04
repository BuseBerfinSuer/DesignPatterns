 
def abcs(letter):
    
    for i in range(65, ord(letter)+1):
            yield chr(i)

 
abcs_H = abcs('H')
abcs_Z = abcs('Z')
 
for abc in abcs_H:
        print(abc, end=" ")
 
print()
 
for abc in abcs_Z:
    print(abc, end=" ")