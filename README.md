# QA Quiz Bot 🤖

Интерактивный Telegram-бот для тренировки знаний в сфере QA (Quality Assurance) и подготовки к собеседованиям или экзаменам.  

**Автор проекта:** [Oleh Sytnyk](https://www.linkedin.com/in/oleh-sytnyk/)  

---

## 🚀 Возможности
- 🧠 **База вопросов** по QA (ручное, автоматизированное тестирование, процессы и инструменты)
- 🎯 **Режим квиза**: 50 случайных вопросов без повторов
- 📈 Подсчёт очков и вывод точности
- 🌐 **Поддержка языков**: украинский, русский, английский *(в планах)*
- 🛠 Плейсхолдеры для будущих функций:
 
---

## 🛠 Стек технологий
- [Python 3.10+](https://www.python.org/)
- [Aiogram v3](https://docs.aiogram.dev/en/latest/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🛠 Установка и запуск

1. **Клонировать репозиторий**  
   `git clone https://github.com/Oleg98-svg/QA_Quiz_Bot.git && cd QA_Quiz_Bot`

2. **Установить зависимости**  
   `pip install -r requirements.txt`

3. **Скопировать `.env.example` в `.env` и добавить свой токен**  
   `BOT_TOKEN=ваш_токен_бота  ADMIN_ID=ваш_ID_в_Telegram  LOG_LEVEL=INFO`

4. **Запустить бота**  
   `python qa_quiz_bot_v3.py`
