import streamlit

# расположение сайта в центре экрана для красивой графики
streamlit.set_page_config( layout="centered")

# заголовок страницы и содержательный текст 
streamlit.title("🍏 Мой умный счетчик калорий")
streamlit.write("Проект по информатике ученицы 10В класса Гиздуллиной.А.Р")

# вкладки сайта
tab1, tab2 = streamlit.tabs(["Расчет нормы калорий", "Дневник питания"])

# словарь для продуктов
food = {
    # фруктики и ягодки:
    "Яблоко (100г)": 52,
    "Банан (100г)": 89,
    "Апельсин (100г)": 47,
    "Клубника (100г)": 33,
    "Виноград (100г)": 65,
    # овощи:
    "Огурец (100г)": 15,
    "Помидор (100г)": 18,
    "Картофель вареный (100г)": 82,
    "Морковь (100г)": 41,
    # гарнир:
    "Овсянка (100г)": 342,
    "Рис отварной (100г)": 130,
    "Гречка отварная (100г)": 110,
    "Макароны вареные (100г)": 112,
    # мясо,рыба и яйца:
    "Куриная грудка (100г)": 165,
    "Говядина тушеная (100г)": 230,
    "Лосось запеченный (100г)": 206,
    "Яйцо вареное (1 шт, ~50г)": 75,
    
    # молочка
    "Молоко 2.5% (100г)": 54,
    "Творог 5% (100г)": 121,
    "Сыр (100г)": 402,
    "Йогурт без добавок (100г)": 60,
    
    # хлебобулочные изделия
    "Пицца (100г)": 266,
    "Бургер (100г)": 295,
    "Хлеб пшеничный (100г)": 242,
    
    # сладкий перекус
    "Шоколад молочный (100г)": 540,
    "Мороженое (100г)": 207,
    "Печенье (100г)": 440
}

# память при клике кнопок
if "calories" not in streamlit.session_state:
    streamlit.session_state.calories = 0.0

# первая вкладка, расчитывающая норму калорий в день
with tab1:
    streamlit.header("Укажите ваши параметры")
    
    # переключатели параметров
    pol = streamlit.radio("Ваш пол:", ["Мужской", "Женский"])
    ves = streamlit.number_input("Ваш вес (кг):", value=65.0, step=0.1)
    rost = streamlit.number_input("Ваш рост (см):",  value=170)
    vozrast = streamlit.number_input("Ваш возраст:", value=16)

    # расчет суточной нормы калорий
    if streamlit.button("Рассчитать суточную норму"):
        if pol == "Мужской":
            bmr = 10 * ves + 6.25 * rost - 5 * vozrast + 5
        else:
            bmr = 10 * ves + 6.25 * rost - 5 * vozrast - 161
            
        daily_norm = int(bmr * 1.2) #дневная нориа калорий для неподвижного человека
        streamlit.session_state.daily_norm = daily_norm
        streamlit.success("Ваша суточная норма калорий:" + str(daily_norm)+ "ккал")

# вторая вкладка,дневник питания
with tab2:
    streamlit.header("Что вы сегодня съели?")
    
    # Проверка, рассчитана ли норма в первой вкладке
    if "daily_norm" not in streamlit.session_state:
        streamlit.warning("Сначала рассчитайте свою норму на первой вкладке!")
    else:
        # Выпадающий список продуктов
        food_choice = streamlit.selectbox("Выберите продукт:", list(food.keys()))
        grams = streamlit.number_input("Сколько грамм вы съели?", value=100, step=10)
        
        if streamlit.button("Добавить в дневник"):
            cal_per_100g = food[food_choice]
            gained = (cal_per_100g * grams) / 100
            streamlit.session_state.calories += gained
            streamlit.toast("Добавлено" +str(gained)+ "ккал!")

        # Вывод остаток калорий на день которые можно сьесть
        norm = streamlit.session_state.daily_norm
        eaten = streamlit.session_state.calories
        left = max(0.0, norm - eaten)
        
        streamlit.header("Статистика за день:")
        streamlit.write("Съедено:" +str(eaten)+ "из"+ str(norm)+ "ккал")
        streamlit.write("Осталось съесть:"+ str(left)+ "кал")
        
        # Индикатор выполнения 
        progress = min(1.0, eaten / norm)
        streamlit.progress(progress)
        
        # сброса дня в виде кнопки
        if streamlit.button("Очистить дневник питания"):
            streamlit.session_state.calories = 0.0
            streamlit.rerun()
