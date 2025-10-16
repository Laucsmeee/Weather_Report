#  Weather Logger (Python Pet Project)

Невеликий pet-проєкт на Python, який отримує дані про погоду з [OpenWeather API](https://openweathermap.org/api),  
відображає їх у терміналі та записує у `.txt` файл для подальшого аналізу.

---

##  Функціонал
- Отримання поточної погоди для заданого міста.
- Збереження даних у файл `weather_log.txt`.
- Підтримка української мови опису погоди.
- Безпечне зберігання API-ключа у файлі `.env`.

---

##  Як це працює
1. Програма надсилає запит до **OpenWeather API**.
2. Відповідь приходить у форматі **JSON**.
3. Програма парсить основні дані: температуру, опис погоди тощо.
4. Результат зберігається у файл `data/weather_log.txt`.

---

OpenWeather API

```http
  GET https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ua
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| `CITY`       | `string` | **Required**. City name (e.g., Kyiv)     |
| `units`   | `string` | Optional. Measurement units (`metric`)   |
| `lang`    | `string` | Optional. Language of description (`ua`) |



---


##  Встановлення

1. Клонуйте проєкт:
 ```bash
   git clone https://github.com/yourusername/weather-logger.git
   cd weather-logger
```
2.Створіть віртуальне середовище (рекомендовано):
 ```bash
    python -m venv .venv
    source .venv/bin/activate   # Linux/macOS
    .venv\Scripts\activate      # Windows
 ```
3. Встановіть залежності:
 ```bash
pip install -r requirements.txt
```
4.Створіть файл .env у корені проєкту:
```bash
API_KEY=your_openweather_api_key
```
5.Додайте .env у .gitignore, щоб не викладати ключ у GitHub:

.env

---


Безпека

API ключ не зберігається у відкритому коді.

Для роботи потрібно створити .env з власним ключем.

Бібліотека python-dotenv\

---

Використані технології

Python 3

Requests — для HTTP-запитів

python-dotenv — для приховування API-ключа

OpenWeather API — джерело даних

---

Ідеї для розвитку

Додавання прогнозу на кілька днів.

Збереження даних у формат .json або .csv.

Побудова графіка зміни температури за тиждень.

Використання зібраних даних для навчання AI-моделі прогнозування погоди.
