import sqlite3

# 1. إنشاء الاتصال بقاعدة البيانات (store.db)
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# 2. إنشاء جدول المنتجات (products)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
    )
''')

# مسح أي بيانات قديمة لتجنب التكرار عند إعادة التشغيل
cursor.execute('DELETE FROM products')

# 3. إدراج بيانات 5 منتجات متنوعة
sample_products = [
    ('Laptop', 'Electronics', 15000.0),
    ('Mouse', 'Electronics', 450.0),
    ('T-Shirt', 'Clothing', 250.0),
    ('Jeans', 'Clothing', 600.0),
    ('Headphones', 'Electronics', 850.0)
]

cursor.executemany('''
    INSERT INTO products (name, category, price)
    VALUES (?, ?, ?)
''', sample_products)

conn.commit()

print("--- تم إدخال المنتجات بنجاح ---\n")

# 4. التنفيذ والاستعلام الأول: استرجاع المنتجات التابعة لفئة معينة (مثلاً Electronics) باستخدام WHERE
print("=== الاستعلام الأول: منتجات قسم Electronics ===")
cursor.execute("SELECT * FROM products WHERE category = 'Electronics'")
electronics_products = cursor.fetchall()
for row in electronics_products:
    print(row)

print("\n")

# 5. التنفيذ والاستعلام الثاني: استرجاع جميع المنتجات مرتبة من الأعلى سعراً للأقل باستخدام ORDER BY price DESC
print("=== الاستعلام الثاني: المنتجات مرتبة من الأعلى للأقل سعراً ===")
cursor.execute("SELECT * FROM products ORDER BY price DESC")
sorted_products = cursor.fetchall()
for row in sorted_products:
    print(row)

# إغلاق الاتصال بقاعدة البيانات
conn.close()