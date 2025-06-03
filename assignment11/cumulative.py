import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Task 2: A Line Plot with Pandas
try:
    with sqlite3.connect('../db/lesson.db') as conn:
        query = """
        Select o.order_id, SUM(p.price * l.quantity) AS total_price
        FROM orders o
        JOIN line_items l ON o.order_id = l.order_id
        JOIN products p ON l.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id;
        """
        df = pd.read_sql_query(query, conn)

    def cumulative(row):
        totals_above = df['total_price'][0:row.name + 1]
        return totals_above.sum()
    
    df['cumulative'] = df.apply(cumulative, axis=1)

    df.plot(x='order_id', y='cumulative', kind='line',  color='green', title='Cumulative Revenue by Order ID')

    plt.xlabel('Order ID', fontsize=12)
    plt.ylabel('Cumulative Revenue', fontsize=12)
    plt.grid(linestyle='--', linewidth=0.5)
    plt.show()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")