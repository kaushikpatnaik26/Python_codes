# def fn(n):
#     for ch in n:
#         if ord(ch)<48 or ord(ch) > 57:
#             print("pls enter a pos number")
#     count =0
#     for i in n:
#         count += 1
#     return count
    
# str = input("Enter a str: ")
# print("no of dig :" , fn(str))
    
        
# list = [1,2,3, "baisakhi" , "kaushik"]
# for i in list:
#     print(i, end=" ")
# print("\n")
# print(list[4])
# list[0] = " new "
# list.insert(2, "aish")
# print(list)

marks = (1,2,3,3,4,5,6,7,3,5,7)

if 99 in marks:
    print(marks.index(99))
else: print("element not present")
