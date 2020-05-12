#Given n names and phone numbers,assemble a phonebook that map friends' names to their respective phone numbers.you will then be given an unknown number of names to query your phone book  for .for each name queried ,print the asssociated entry from your phone book on a new line in the form name=phoneNumber;if an entry for name is not found , print Not found instead.......INPUT FORMAT:the first line contain contais an integer, n,denoting the number of entries in the notebook.each of the n subsequent lines describes an entry in the form two space-separated values on the single line.the first value is a friend's name,and the second value is an 8-digit phone number.after the n lines of phonebook entries,there are an unknown number of lines of queries.Each line(query) contains name to look up,and you must continue the reading lines until there is no more input...OUTPUT FORMAT:on a new line for each query,print Not found if the name has no corresponding entry in the phone book;otherwise,print the full name and phoneNumber in the format name=phoneNumber.



















n=int(input())
d=dict()
for i in range(0,n):
  name,number=input().split()
  d[name]=number
for i in range(0,n):
    try:
        name=input()
        if name in d:
            print(f'{name}={d[name]}')
        else:
            print("Not found")
    except:
        break
