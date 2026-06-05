import json

DATA_FILE = "books.json"

def load_books():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def is_duplicate(books, author, title):
    """Проверяет, есть ли уже такая книга."""
    for book in books:
        if book['author'].lower() == author.lower() and book['title'].lower() == title.lower():
            return True
    return False

def add_book():
    """Добавляет новую книгу."""
    print("\n--- Добавление новой книги ---")
    
    author = input("Введите автора: ").strip()
    if not author:
        print("Ошибка: автор не может быть пустым.")
        return
    
    title = input("Введите название: ").strip()
    if not title:
        print("Ошибка: название не может быть пустым.")
        return
    
    # Загружаем текущие книги и проверяем дубликаты
    books = load_books()
    if is_duplicate(books, author, title):
        print(f"Ошибка: книга '{title}' автора '{author}' уже существует.")
        return
    
    # Проверка оценки
    try:
        rating = int(input("Введите оценку (от 1 до 5): "))
        if rating < 1 or rating > 5:
            print("Ошибка: оценка должна быть от 1 до 5.")
            return
    except ValueError:
        print("Ошибка: введите целое число.")
        return
    
    # Ввод даты
    date = input("Введите дату прочтения (например, 2024-05-15): ").strip()
    if not date:
        print("Ошибка: дата не может быть пустой.")
        return
    
    # Создаём запись и сохраняем
    new_book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    }
    
    books.append(new_book)
    save_books(books)
    print(f"Книга '{title}' успешно добавлена!")

def show_all_books():
    print("Функция показа всех книг (в разработке)")

def show_avg_rating():
    print("Функция средней оценки (в разработке)")

def show_author_stats():
    print("Функция статистики по авторам (в разработке)")

def delete_book():
    print("Функция удаления книги (в разработке)")

def main():
    while True:
        print("\n--- Трекер прочитанных книг ---")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            show_all_books()
        elif choice == '3':
            show_avg_rating()
        elif choice == '4':
            show_author_stats()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
