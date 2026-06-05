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

def add_book():
    print("Функция добавления книги (в разработке)")


def show_all_books():
    books = load_books()
    if not books:
        print("\nСписок книг пуст.")
        return
    print("\n--- Список всех книг ---")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['author']} - '{book['title']}'. Оценка: {book['rating']}. Дата: {book['date']}")

def show_avg_rating():
    print("Функция средней оценки (в разработке)")

def show_author_stats():
    print("Функция статистики по авторам (в разработке)")

def delete_book():
    books = load_books()
    if not books:
        print("\nСписок книг пуст.")
        return
    show_all_books()
    try:
        index = int(input("\nВведите номер книги для удаления: "))
        if index < 1 or index > len(books):
            print("Ошибка: неверный номер.")
            return
        removed = books.pop(index - 1)
        save_books(books)
        print(f"Книга '{removed['title']}' удалена!")
    except ValueError:
        print("Ошибка: введите число.")

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
