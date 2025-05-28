import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Task 1: Plotting with Pandas

try:
    with sqlite3.connect('../db/lesson.db') as conn:
        query = """
        SELECT last_name, SUM(price * quantity) AS revenue 
        FROM employees e 
        JOIN orders o ON e.employee_id = o.employee_id 
        JOIN line_items l ON o.order_id = l.order_id 
        JOIN products p ON l.product_id = p.product_id 
        GROUP BY e.employee_id;
        """

        employee_results = pd.read_sql_query(query, conn)

    employee_results.plot(x='last_name', y='revenue', kind='bar', color='skyblue', title='Employee Revenue Report', legend=False)

    # plt.xlabel('Employee')
    # plt.ylabel('Revenue')
    # plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.show()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
