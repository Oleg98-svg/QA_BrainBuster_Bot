import asyncio
import random
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "8261330449:AAHdv1aWGEZaVgtrV4sgnQCrb38ohLUPA40"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 💡 Вставь свой список из 50+ вопросов сюда
all_questions = [
    {
        "question": "Що таке тестування програмного забезпечення?",
        "options": [
            "Процес створення коду",
            "Процес перевірки, чи відповідає програма вимогам",
            "Процес встановлення програми",
            "Процес написання документації"
        ],
        "answer": 1,
        "explanation": "Тестування — це процес перевірки, чи працює програма згідно з вимогами."
    },
    {
        "question": "Що таке баг (bug)?",
        "options": [
            "Функція програми",
            "Очікувана поведінка",
            "Помилка або дефект у програмі",
            "Документ для розробника"
        ],
        "answer": 2,
        "explanation": "Баг — це помилка, яка призводить до неправильної роботи програми."
    },
    {
        "question": "Що таке інтеграційне тестування?",
        "options": [
            "Тестування окремих модулів",
            "Тестування взаємодії між компонентами",
            "Тестування інтерфейсу",
            "Тестування графіки"
        ],
        "answer": 1,
        "explanation": "Інтеграційне тестування перевіряє, як взаємодіють між собою частини системи."
    },
    {
        "question": "Що таке unit-тестування?",
        "options": [
            "Тестування лише UI",
            "Тестування продуктивності",
            "Тестування окремих функцій чи методів",
            "Тестування документації"
        ],
        "answer": 2,
        "explanation": "Unit-тестування перевіряє окремі одиниці коду, як правило, функції або методи."
    },
    {
        "question": "Яка основна мета smoke-тестування?",
        "options": [
            "Перевірити, чи працюють основні функції програми",
            "Повністю протестувати систему",
            "Знайти дрібні помилки",
            "Оцінити дизайн"
        ],
        "answer": 0,
        "explanation": "Smoke-тестування — поверхнева перевірка життєздатності продукту."
    },
    {
        "question": "Що таке sandbox у QA?",
        "options": [
            "Пісочниця для дітей",
            "Ізольоване середовище для безпечного тестування",
            "Середовище для релізу",
            "Базова бібліотека"
        ],
        "answer": 1,
        "explanation": "Sandbox — це ізольоване середовище для безпечного експериментування та тестування."
    },
    {
        "question": "Що таке TMS у тестуванні?",
        "options": [
            "Test Management System",
            "Technical Manual System",
            "Trusted Module System",
            "Test Metrics Source"
        ],
        "answer": 0,
        "explanation": "TMS — система для керування тест-кейсами, планами, звітами (наприклад, TestRail, Zephyr)."
    },
    {
        "question": "Який з нижче наведених є прикладом функціонального тестування?",
        "options": [
            "Тестування часу завантаження",
            "Тестування інтерфейсу",
            "Тестування логіки логіну",
            "Тестування стабільності"
        ],
        "answer": 2,
        "explanation": "Функціональне тестування перевіряє, чи відповідає функціональність очікуванням."
    },
    {
        "question": "Що таке баг-фікс?",
        "options": [
            "Виправлення помилки",
            "Написання нового модуля",
            "Оновлення інтерфейсу",
            "Запуск тестів"
        ],
        "answer": 0,
        "explanation": "Баг-фікс — це виправлення знайденої помилки в коді."
    },
    {
        "question": "Що означає статус 'In Progress' у баг-репорті?",
        "options": [
            "Баг закритий",
            "Баг не підтверджено",
            "Баг в процесі виправлення",
            "Баг не знайдено"
        ],
        "answer": 2,
        "explanation": "In Progress — помилка в роботі: над нею працює розробник."
    },
    {
        "question": "Що таке code freeze?",
        "options": [
            "Коли код заморожується для продакшену",
            "Коли сервер зависає",
            "Коли система вимикається",
            "Коли блокують тестування"
        ],
        "answer": 0,
        "explanation": "Code freeze — етап, коли заборонені нові зміни в код перед релізом."
    },
    {
        "question": "Яка роль QA в Agile-команді?",
        "options": [
            "Лише писати баги",
            "Бути незалежним від розробки",
            "Бути частиною команди, забезпечувати якість на всіх етапах",
            "Не брати участі у спринтах"
        ],
        "answer": 2,
        "explanation": "QA — повноцінний учасник Agile-команди, відповідальний за якість на всіх етапах."
    },
    {
        "question": "Яка мета ретроспективи в Scrum?",
        "options": [
            "Провести тестування",
            "Оцінити виконання задач",
            "Поліпшити процес розробки та взаємодії",
            "Оновити беклог"
        ],
        "answer": 2,
        "explanation": "Ретроспектива дозволяє команді оцінити роботу та знайти можливості для покращення."
    },
    {
        "question": "Що таке Acceptance Criteria?",
        "options": [
            "Умови прийняття завдання",
            "Код рев'ю",
            "Метрика швидкодії",
            "Документ помилок"
        ],
        "answer": 0,
        "explanation": "Acceptance Criteria — умови, які мають бути виконані для прийняття задачі."
    },
    {
        "question": "Що таке Load Testing?",
        "options": [
            "Тестування при високому навантаженні",
            "Тестування без даних",
            "Тестування швидкості мережі",
            "Ручне тестування"
        ],
        "answer": 0,
        "explanation": "Load Testing — це перевірка, як система працює під навантаженням."
    },
    {
        "question": "Що таке Jenkins у QA?",
        "options": [
            "CI/CD інструмент для автоматизації процесів",
            "Інструмент створення UI",
            "Сервіс підтримки",
            "Менеджер логів"
        ],
        "answer": 0,
        "explanation": "Jenkins — система CI/CD для автоматизації тестування, збірки та деплою."
    },
    {
        "question": "Що таке test suite?",
        "options": [
            "Один тест-кейс",
            "Група тест-кейсів",
            "Баг-репорт",
            "CI-сервер"
        ],
        "answer": 1,
        "explanation": "Test Suite — набір тест-кейсів, що перевіряють пов'язаний функціонал."
    },
    {
        "question": "Що таке boundary value analysis?",
        "options": [
            "Техніка тестування, яка перевіряє граничні значення",
            "Аналіз дизайну",
            "Перевірка документації",
            "Метод навантаження"
        ],
        "answer": 0,
        "explanation": "Boundary Value Analysis — техніка тест-дизайну для перевірки крайніх значень."
    },
    {
        "question": "Що таке TestRail?",
        "options": [
            "Система керування тест-кейсами",
            "Інструмент малювання діаграм",
            "Сервіс для логів",
            "Баг-трекер"
        ],
        "answer": 0,
        "explanation": "TestRail — популярна система для створення та запуску тест-кейсів."
    },
    {
        "question": "Що означає термін 'defect leakage'?",
        "options": [
            "Кількість дефектів, що пройшли на продакшн",
            "Рівень покриття коду",
            "Швидкість тестування",
            "Загальний час багфіксів"
        ],
        "answer": 0,
        "explanation": "Defect leakage — баги, що не були знайдені тестуванням і потрапили до користувача."
    },
    {
        "question": "Що таке regression suite?",
        "options": [
            "Набір тестів для нового функціоналу",
            "Набір випадкових тестів",
            "Набір тестів для smoke-тестування",
            "Набір тестів для перевірки старого функціоналу після змін"
        ],
        "answer": 3,
        "explanation": "Regression Suite — це набір тестів для перевірки, чи працює все після змін у коді."
    },
    {
        "question": "Що таке exploratory session?",
        "options": [
            "Плановане дослідне тестування без сценаріїв",
            "Інтерв'ю з користувачем",
            "Розсилка багів",
            "Презентація інтерфейсу"
        ],
        "answer": 0,
        "explanation": "Exploratory session — коли тестер вивчає систему без детального плану."
    }
]

user_data = {}

def get_keyboard(options):
    keyboard = [[KeyboardButton(text=chr(65 + i))] for i in range(len(options))]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    questions_copy = random.sample(all_questions, k=min(50, len(all_questions)))  # 50 уникальных вопросов
    user_data[user_id] = {
        "score": 0,
        "total": 0,
        "questions": questions_copy,
        "current": None
    }
    await send_question(message)

async def send_question(message: types.Message):
    user_id = message.from_user.id
    data = user_data[user_id]

    if not data["questions"]:
        percent = round(data["score"] / data["total"] * 100) if data["total"] > 0 else 0
        await message.answer(
            f"🏁 Квіз завершено!\n"
            f"✅ Ви відповіли правильно на {data['score']} з {data['total']}.\n"
            f"🎯 Точність: {percent}%\n\nНатисніть /start щоб почати знову.",
            reply_markup=types.ReplyKeyboardRemove()
        )
        return

    question = data["questions"].pop(0)
    data["current"] = question

    text = f"🧠 *Питання {data['total'] + 1}/50:*\n{question['question']}\n\n"
    for i, opt in enumerate(question["options"]):
        text += f"{chr(65 + i)}) {opt}\n"

    keyboard = get_keyboard(question["options"])
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

@dp.message(F.text.in_({"A", "B", "C", "D"}))
async def handle_answer(message: types.Message):
    user_id = message.from_user.id
    data = user_data.get(user_id)

    if not data or not data.get("current"):
        await message.answer("Натисніть /start щоб почати спочатку.")
        return

    user_answer = message.text.strip().upper()
    question = data["current"]
    correct_letter = chr(65 + question["answer"])

    data["total"] += 1
    if user_answer == correct_letter:
        data["score"] += 1
        response = "✅ Правильно!"
    else:
        correct_text = question["options"][question["answer"]]
        response = f"❌ Неправильно! Правильна відповідь: {correct_letter}) {correct_text}"

    response += f"\n💡 {question['explanation']}"
    response += f"\n\n🎯 Рахунок: {data['score']}/{data['total']}"
    await message.answer(response)

    await send_question(message)

async def main():
    print("🤖 Бот запущений!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())