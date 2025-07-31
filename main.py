from db.crud import *

while True:
    print("1. Створити продукт")
    print("2. Створити замовника")
    print("3. Додати замовлення")
    print("4. Загальний обсяг продажів")
    print("5. Кількість замовлень на кожного клієнта")
    print("6. Середній чек замовлення")
    print("7. Найбільш популярна категорія товарів")
    print("8. Загальна кількість товарів кожної категорії")
    print("9. Смартфони з ціною +10%")
    print("0. Вийти")

    choice = input("Виберіть дію: ")

    if choice == "1":
        product_id = int(input("Введіть ID товару: "))
        name = input("Введіть назву товару: ")
        category = input("Введіть категорію товару: ")
        price = float(input("Введіть ціну товару: "))
        create_product(product_id, name, category, price)
        print("Товар створений.")

    elif choice == "2":
        customer_id = int(input("Введіть ID замовника: "))
        first_name = input("Введіть ім'я замовника: ")
        last_name = input("Введіть прізвище замовника: ")
        email = input("Введіть email замовника: ")
        create_customer(customer_id, first_name, last_name, email)
        print("Замовник створений.")

    elif choice == "3":
        order_id = int(input("Введіть ID замовлення: "))
        customer_id = int(input("Введіть ID замовника: "))
        product_id = int(input("Введіть ID товару: "))
        quantity = int(input("Вкажіть кількість товарів: "))
        order_date = input("Введіть дату замовлення (наприклад, 30.07.2025): ")
        create_order(order_id, customer_id, product_id, quantity, order_date)
        print("Замовлення створене.")

    elif choice == "4":
        total = total_sales()
        print(f"Загальний обсяг продажів: {total} грн")

    elif choice == "5":
        results = orders_customer()
        print("Кількість замовлень кожного клієнта:")
        for first_name, last_name, count in results:
            print(f"{first_name} {last_name}: {count} замовлень")

    elif choice == "6":
        results = avg_order_price()
        print("Середній чек для кожного замовлення:")
        for order_id, avg_price in results:
            print(f"Замовлення #{order_id}: {avg_price:.2f} грн")

    elif choice == "7":
        result = most_popular_category()
        if result:
            category, count = result
            print(f"Найпопулярніша категорія: {category} ({count} продажів)")
        else:
            print("Немає даних.")

    elif choice == "8":
        results = count_by_category()
        print("Кількість товарів у кожній категорії:")
        for category, count in results:
            print(f"{category}: {count} шт")

    elif choice == "9":
        results = smartphones_increase()
        print("Смартфони з ціною +10%:")
        for name, price, new_price in results:
            print(f"{name}: стара ціна — {price}, нова ціна — {new_price:.2f}")

    elif choice == "0":
        print("Завершення роботи.")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
