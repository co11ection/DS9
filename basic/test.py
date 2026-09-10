# text = input("Введите свой текст: ")
# words = text.lower().split()
# counts = {}

# for word in words:
#     counts[word] = counts.get(word, 0) + 1
    
# # most_common = max(counts, key=counts.get)
# # print(most_common)

# max_value = 1
# keys = []
# for k, v in counts.items():
#     if v > max_value:
#         max_value = v
#         keys = [k]
#     elif v == max_value:
#         keys.append(k)
    
# print(keys, max_value)



#13
def is_valid_username(username):
    if (3 >= len(username) or len(username)>=15):
        return False
    if " " in username:
        return False
    if not username[0].isalpha():
        return False
    return True


print(is_valid_username("Тимати"))
print(is_valid_username("4Тиматим"))
print(is_valid_username("Ти"))
print(is_valid_username(" Тим "))