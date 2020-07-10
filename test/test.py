# arr=['3','30','34','5','9']
# print(sorted(arr, key=lambda x:x*3, reverse=True))

phoneBook = ["119", "97674223", "1195524421","543151","6456415416","12371928312"]
phoneBook = sorted(phoneBook)
for p1,p2 in zip(phoneBook, phoneBook[1:]):
    print(p1)
    print(p2)
    if p2.startswith(p1):
        print("false")
print("true")