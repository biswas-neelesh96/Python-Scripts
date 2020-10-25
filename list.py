#Functions Of list
#insert i e: Insert integer e at position i .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer e at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list
li=[]
N = int(input())
for i in range(N):
    function= raw_input().split()
    if function[0] == "insert":
        insert_at=int(function[1])
        insert_what=int(function[2])
        li.insert(insert_at,insert_what)

    if function[0] == "print":
        print(li)
    
    if function[0] == "remove":
       removed_character=int(function[1])
       li.remove(removed_character) 
    
    if function[0]=="append":
        appended_character=int(function[1])
        li.append(appended_character)

    if function[0]=="sort":
        li.sort()

    if function[0]=="pop":
        li.pop()

    if function[0]=="reverse":
        li.reverse()
