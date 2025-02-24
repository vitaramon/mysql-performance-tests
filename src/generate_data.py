import pymysql
import random
from tqdm import tqdm

conn = pymysql.connect(host='localhost', user='root', password='root', database='figures_db')
cursor = conn.cursor()

colors = ['red', 'blue', 'green', 'yellow', 'black']
types = ['rectangle', 'circle']

print("Filling the database with data...")

for _ in tqdm(range(10000000)):  # 10 million records
    figure_type = random.choice(types)
    color = random.choice(colors)
    
    cursor.execute("INSERT INTO figures (type, color) VALUES (%s, %s)", (figure_type, color))
    figure_id = cursor.lastrowid
    
    if figure_type == 'rectangle':
        cursor.execute("INSERT INTO figure_dimensions (figure_id, height, width) VALUES (%s, %s, %s)",
                       (figure_id, random.randint(1, 100), random.randint(1, 100)))
    else:
        cursor.execute("INSERT INTO figure_dimensions (figure_id, radius) VALUES (%s, %s)",
                       (figure_id, random.randint(1, 50)))

conn.commit()
cursor.close()
conn.close()

print("Data uploaded successfully")
