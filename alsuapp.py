import streamlit as st

# Настройка страницы (заголовок во вкладке браузера)
st.set_page_config(page_title="Счетчик калорий", page_icon="🍏", layout="centered")

# Красивый заголовок на странице
st.title("🍏 Мой умный счетчик калорий")
st.write("Проект по информатике ученика 10 класса")

# Создаем вкладки на сайте для удобства
tab1, tab2 = st.tabs(["📊 Расчет нормы", "🍽️ Дневник питания"])

# База данных продуктов
FOOD_DATABASE = {
    "Яблоко (100г)": 52,
    "Куриная грудка (100г)": 165,
    "Рис отварной (100г)": 130,
    "Овсянка (100г)": 342,
    "Банан (100г)": 89,
    "Шоколад (100г)": 540
}

# Инициализация памяти (чтобы сайт помнил съеденное при обновлении страницы)
if "calories_eaten" not in st.session_state:
    st.session_state.calories_eaten = 0.0

# ВКЛАДКА 1: РАСЧЕТ НОРМЫ
with tab1:
    st.header("Укажите ваши параметры")
    
    # Удобные переключатели и поля ввода
    gender = st.radio("Ваш пол:", ["Мужской", "Женский"])
    weight = st.number_input("Ваш вес (кг):", min_value=30.0, max_value=200.0, value=65.0, step=0.1)
    height = st.number_input("Ваш рост (см):", min_value=100, max_value=250, value=170)
    age = st.number_input("Ваш возраст:", min_value=10, max_value=100, value=16)

    # Кнопка расчета
    if st.button("Рассчитать суточную норму"):
        if gender == "Мужской":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
            
        daily_norm = int(bmr * 1.2) # Минимальная активность
        st.session_state.daily_norm = daily_norm
        st.success(f"Ваша суточная норма калорий: **{daily_norm} ккал**")

# ВКЛАДКА 2: ДНЕВНИК ПИТАНИЯ
with tab2:
    st.header("Что вы сегодня съели?")
    
    # Проверяем, рассчитана ли норма в первой вкладке
    if "daily_norm" not in st.session_state:
        st.warning("Сначала рассчитайте свою норму на первой вкладке!")
    else:
        # Выпадающий список продуктов
        food_choice = st.selectbox("Выберите продукт из базы:", list(FOOD_DATABASE.keys()))
        grams = st.number_input("Сколько грамм вы съели?", min_value=1, max_value=2000, value=100, step=10)
        
        if st.button("Добавить в дневник"):
            cal_per_100g = FOOD_DATABASE[food_choice]
            gained = (cal_per_100g * grams) / 100
            st.session_state.calories_eaten += gained
            st.toast(f"Добавлено {gained:.1f} ккал!")

        # Вывод статистики и прогресса
        norm = st.session_state.daily_norm
        eaten = st.session_state.calories_eaten
        left = max(0.0, norm - eaten)
        
        st.subheader("Статистика за день:")
        st.write(f"Съедено: **{eaten:.1f}** из **{norm}** ккал")
        st.write(f"Осталось съесть: **{left:.1f}** ккал")
        
        # Индикатор выполнения (прогресс-бар)
        progress = min(1.0, eaten / norm)
        st.progress(progress)
        
        # Кнопка сброса дня
        if st.button("Очистить дневник питания"):
            st.session_state.calories_eaten = 0.0
            st.rerun()
