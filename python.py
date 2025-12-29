with open('biblioreka.txt') as x:
    t=x.read()

print((t.split('\n')))  
def add_book(arr, section: str, title: str, available: bool=True) -> bool:
    index_title = find_index(arr[0], 'title')

    # Проверяем все книги, кроме заголовка
    for book in arr[1:]:
        if book[index_title].strip().lower() == title.strip().lower():
            return False  # книга уже есть

    # Если не нашли — добавляем один раз
    arr.append([section.strip(), title.strip(), str(available)])
    return True

print(add_book(biblioteka, 'fantazy', 'chasodei', False))  # добавит книгу
print(add_book(biblioteka, 'fantazy', '1', False))  # не добавит, вернёт False
print(biblioteka)