words = ['python', 'word', 'java', 'word']
count = 0
for word in words:
    if "word" == word:
        count+=1
    
print(count)


from collections import Counter
words = ['python', 'word', 'java', 'word']
counts = Counter(words)
print(counts["word"])
letters = Counter("миссисипи")
print(letters)

a = ['python', 'word', 'java', 'word']
b = ['python', 'word', 'java', 'word', 'python', 'java']
result = Counter(a) + Counter(b)
print(result)

from collections import defaultdict

a = ['python', 'word', 'java', 'pword']
groups = defaultdict(list)
for word in a:
    first_letter = word[0]
    groups[first_letter].append(word)
print(groups)


list1 = ["A", "B", "C", "A", "A", "B"]
counts = Counter(list1)
print(counts)

students_records = [
    ("Иван", 78),
    ('Иван', 87),
    ('Айдар', 85),
    ('Айдар', 75),
    ("Дина", 56),
    ("Дина", 99),
]
result = defaultdict(list)
for key, value in students_records:
    result[key].append(value)
    
print(result)


string = 'Яблоко'
result = defaultdict(int)
for letter in string:
    result[letter] +=1
print(result)


from collections import deque

list1 = deque(maxlen=3)
for i in range(1, 11):
    list1.appendleft(i)
    print(list1)

list1.popleft()
print(list1)


user = ("John", 25)
print(user[0])


from collections import namedtuple
user = namedtuple("user", ['name', 'age'])
user1 = user("John", 25)
print(user1.name)
print(user1.age)
print(user1[1])



from collections import namedtuple, Counter, defaultdict 
  
Sale = namedtuple("Sale", ["product", "category", "amount"]) 
  
sales = [ 
    Sale("Ноутбук", "Электроника", 350000), 
    Sale("Мышь", "Электроника", 5000), 
    Sale("Ноутбук", "Электроника", 350000), 
    Sale("Стол", "Мебель", 45000), 
    Sale("Стул", "Мебель", 15000), 
    Sale("Стул", "Мебель", 15000), 
    Sale("Мышь", "Электроника", 5000), 
    Sale("Стол", "Мебель", 45000), 
] 
  
# TODO 1: Counter по продукту, найти самый продаваемый товар 
product_counts = {}
for sale in sales:
    product = sale.product
    if product not in product_counts:
        product_counts[product] = 0
    product_counts[product] += 1
product_counts = Counter(product_counts)
top_product = product_counts.most_common(1)[0]
print(top_product)
  
# TODO 2: defaultdict(list) — суммы продаж по категориям 
by_category = None 
  
# TODO 3: суммарная выручка по каждой категории 
revenue_by_category = None