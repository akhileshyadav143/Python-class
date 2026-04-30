# q= x="hello. everyone. lets. learn. python"
# output="Python learn lets everyone hello"

# x="hello everyone lets learn python"
# x=x.split()
# x.reverse()
# x=" ".join(x).capitalize()
# print(x)



# Q= olleh enoyreve stel ntael nohtpy

# x="hello everyone lets learn python"
# print(" ".join(y[::-1] for y in x.split()))
# x=x.split()
# x=[i[::-1] for i in x]
# x=" ".join(x)
# print(x)



# email = input("Enter email: ")

# at_pos = email.find('@')
# dot_pos = email.rfind('.')   

# if at_pos > 0 and dot_pos > at_pos + 1 and dot_pos < len(email) - 1:
#     print("Valid Email")
# else:
#     print("Invalid Email")


# x="Hello World from Python"
# x=x.split()
# x.reverse()
# print(x)


# x=input("Enetr a string :")
# ch=input("Enter the char:")
# lst=[]
# for i in range(len(x)):
#     if x[i]==ch:
#         lst.append(i)
        
        
# print(lst) 




# text = input("Enter a string: ")
# char = []
# for ch in text:
#     if ch not in char:
#         char.append(ch)
# print(char)



x = input("Enter a string: ")
src = input("Enter substring to remove: ")

result = x.replace(src, "")

print(result)



