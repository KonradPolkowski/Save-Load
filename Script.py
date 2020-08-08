"ok this is my first mechanism to save things but what things :O"

# # print("\nWelcome to Book Editor\n")
# # answer = input(
# #     "what you want to do:\n\n1. Create new page\n2. Edit exist page\n3. Change number of page\n4. Delete\n")

# if answer == str(1):
#     print("pamiętam")

test = open("Saves.txt", "w+")

for i in range(10):
    test.write("This is line %d\n" % (i+1))

test.close()

test2 = open("Saves.txt", "r")
lol = test2.readlines()
print(lol)

lista = list(lol)
dl = int(len(lista))
print(dl)
final_list = []
for i in lista:
        final_list.append(i.strip())

print(final_list)
# dict1 = []
# x = 1
# while x <= dl:
#     for line in lista:
#         dict1.append({x: line})
#         x = x+1


# print(dict1)
# test2.close()

# dict1[0] = {1: "input"}
# print(dict1[0])
# print(dict1)

# nowe = []
# for x in dict1:
#     for a in x:
#         nowe.append(x[a])
#         print(x[a])

# print(nowe)


# test3 = open("Saves.txt", "w+")
# for i in nowe:
#     test3.write(i+"\n")
# test3.close()


# nowe.remove(nowe[7])
# print(nowe)
