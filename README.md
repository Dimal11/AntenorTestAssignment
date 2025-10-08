# 🧪 Antenor Test Assignment

Автоматизоване тестування сторінки **Dashboard** системи [Antenor.online](https://antenor.online).  
Проєкт побудовано на **Python + Playwright + pytest + Allure**, повністю ізольований у Docker-контейнері.  
Після запуску автоматично генерується HTML-звіт Allure, який відкривається у браузері.

---

## 🚀 Запуск проєкту через Docker

### 1️⃣ Клонування репозиторію
```bash
  git clone https://github.com/<your-repo>/AntenorTestAssignment.git
  cd AntenorTestAssignment
```

### 2️⃣ Збірка Docker-образу
```bash
  docker build -t antenor-tests .
```

### 3️⃣ Запуск контейнера
```bash
  docker run -p 8080:8080 antenor-tests
```

Після завершення тестів Allure-звіт буде доступний за адресою:  
👉 **http://localhost:8080**

---

## ⚙️ Змінні середовища (.env)

У корені проєкту повинен бути файл **`.env`**, що містить конфіденційні дані для тестів (логіни, паролі, адреси тощо).  
Файл **`.env`** не входить у репозиторій з міркувань безпеки, але існує шаблон **`.env.example`**, який показує необхідну структуру.

### 🧩 Приклад `.env.example`
```env
# Дані користувача для авторизації
USER_LOGIN=****
USER_PASS=******
```

Перед запуском скопіюй `.env.example` у `.env` і при потребі зміни значення:
```bash
cp .env.example .env
```

---

## 📂 Структура проєкту

```
AntenorTestAssignment/
├── data_set/           # тестові дані
├── page_objects/       # Page Object класи
│   ├── base_form.py
│   └── auth_form.py
├── tests/              # тест-кейси (pytest + playwright)
│   └── test.py
├── utils/              # утиліти
│   ├── dot_dict.py
│   └── fake_generator.py
├── .env                # змінні середовища
├── .env.example        # приклад структури env
├── .gitignore
├── config.py
├── conftest.py
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🧾 Результат запуску

- ✅ Виконуються всі Playwright-тести  
- 🧮 Зберігаються результати у `allure-results/`  
- 📊 Генерується звіт у `allure-report/`  
- 🌐 Allure-звіт автоматично відкритий на порту `8080`  
  👉 **http://localhost:8080**

---

## 🧰 Використані технології

| Компонент | Опис |
|------------|------|
| **Python 3.13** | Основна мова автоматизації |
| **Pytest** | Тестовий раннер |
| **Playwright** | Автоматизація браузера |
| **Allure Pytest** | Формування звітів |
| **Docker** | Ізольоване середовище для запуску |
| **Dotenv** | Робота зі змінними середовища |

---

## 🧩 Ключові можливості

- Автоматизація сценаріїв авторизації  
- Використання патерну **Page Object**  
- Збереження скріншотів у звіт Allure  
- Візуальні та функціональні перевірки  
- Повністю автономний Docker-запуск без залежностей

---

## 👨‍💻 Автор

**Dmytro Levchenko**  
Automation QA Engineer
