# ValueError: time data 'X' does not match format '%Y-%m-%d'

# Using a correct format for the second argument
from datetime import datetime


my_str = '2023-24-09' # 👉️ YYYY-DD-MM

date = datetime.strptime(my_str, '%Y-%d-%m')
print(date)  # 👉️ 2023-09-24 00:00:00