import os
from dotenv import load_dotenv

# 1. Загружаем переменные из .env в окружение
load_dotenv('test.env') 

def print_author():
# 2. Читаем переменную AUTHOR из окружения
    author = os.getenv('AUTHOR')
  
    # Печатаем результат
    print(f"Автор проекта: {author}")
print_author()