import sqlite3

conn = sqlite3.connect('market.db')
cursor = conn.cursor()

def create_product(product_id, name, category, price):
    cursor.execute('''
    INSERT INTO products (product_id, name, category, price) 
    VALUES (?, ?, ?, ?)
    ''', (product_id, name, category, price))
    conn.commit()

def create_customer(customer_id, first_name, last_name, email):
    cursor.execute('''
    INSERT INTO customers (customer_id, first_name, last_name, email) 
    VALUES (?, ?, ?, ?)
    ''', (customer_id, first_name, last_name, email))
    conn.commit()

def create_order(order_id, customer_id, product_id, quantity, order_date):
    cursor.execute('''
    INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date)
    VALUES (?, ?, ?, ?, ?)
    ''', (order_id, customer_id, product_id, quantity, order_date))
    conn.commit()

def total_sales():
    cursor.execute('''
    SELECT SUM(products.price * orders.quantity)
    FROM orders
    JOIN products ON products.product_id = orders.product_id
    ''')
    return cursor.fetchone()[0]

def orders_customer():
    cursor.execute('''
    SELECT customers.first_name, customers.last_name, COUNT(orders.order_id)
    FROM orders
    INNER JOIN customers ON orders.customer_id = customers.customer_id
    GROUP BY orders.customer_id
    ''')
    return cursor.fetchall()

def avg_order_price():
    cursor.execute('''
    SELECT orders.order_id, AVG(products.price * orders.quantity)
    FROM orders
    JOIN products ON orders.product_id = products.product_id
    GROUP BY orders.order_id
    ''')
    return cursor.fetchall()

def most_popular_category():
    cursor.execute('''
    SELECT products.category, COUNT(*) AS cnt
    FROM orders
    JOIN products ON orders.product_id = products.product_id
    GROUP BY products.category
    ORDER BY cnt DESC
    LIMIT 1
    ''')
    return cursor.fetchone()

def count_by_category():
    cursor.execute('''
    SELECT category, COUNT(*)
    FROM products
    GROUP BY category
    ''')
    return cursor.fetchall()

def smartphones_increase():
    cursor.execute('''
    SELECT name, price, price * 1.10
    FROM products
    WHERE category = 'smartphone'
    ''')
    return cursor.fetchall()