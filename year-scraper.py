import regex
f = open("new-name.txt","r+")
for line in f:
    x = regex.findall(r'(?:\bdigit-|\s|^)(\d{4})(?=[.?\s]|-digit\b|$)', line)
    print(x)

