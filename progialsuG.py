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
    "Яблоко (100г)": {"калории": 52, "белки": 0.4, "жиры": 0.4, "углеводы": 9.8},
    "Банан (100г)": {"калории": 89, "белки": 1.5, "жиры": 0.1, "углеводы": 21.8},
    "Апельсин (100г)": {"калории": 47, "белки": 0.9, "жиры": 0.2, "углеводы": 10.3},
    "Клубника (100г)": {"калории": 33, "белки": 0.8, "жиры": 0.4, "углеводы": 7.5},
    "Виноград (100г)": {"калории": 65, "белки": 0.6, "жиры": 0.2, "углеводы": 16.8}, 
    
    # овощи:
    "Огурец (100г)": {"калории": 15, "белки": 0.8, "жиры": 0.1, "углеводы": 2.8},
    "Помидор (100г)": {"калории": 18, "белки": 0.6, "жиры": 0.2, "углеводы": 4.2},
    "Картофель вареный (100г)": {"калории": 82, "белки": 2.0, "жиры": 0.4, "углеводы": 16.7},
    "Морковь (100г)": {"калории": 41, "белки": 1.3, "жиры": 0.1, "углеводы": 9.3},
    # гарнир:
    "Овсянка (100г)": {"калории": 342, "белки": 12.0, "жиры": 6.0, "углеводы": 67.0},
    "Рис отварной (100г)": {"калории": 130, "белки": 2.2, "жиры": 0.2, "углеводы": 24.9},
    "Гречка отварная (100г)": {"калории": 110, "белки": 4.2, "жиры": 1.1, "углеводы": 21.3},
    "Макароны вареные (100г)": {"калории": 112, "белки": 3.9, "жиры": 0.4, "углеводы": 23.2},
    # мясо,рыба и яйца:
    "Куриная грудка (100г)": {"калории": 165, "белки": 31.0, "жиры": 3.6, "углеводы": 0.0},
    "Говядина тушеная (100г)": {"калории": 230, "белки": 16.0, "жиры": 17.0, "углеводы": 0.0},
    "Лосось запеченный (100г)": {"калории": 206, "белки": 22.0, "жиры": 12.0, "углеводы": 0.0},
    "Яйцо вареное (1 шт, 50г)": {"калории": 75, "белки": 6.3, "жиры": 5.3, "углеводы": 0.4},
    # молочка
    "Молоко 2.5% (100г)": {"калории": 54, "белки": 2.9, "жиры": 2.5, "углеводы": 4.8},
    "Творог 5% (100г)": {"калории": 121, "белки": 17.2, "жиры": 5.0, "углеводы": 1.8},
    "Сыр (100г)": {"калории": 402, "белки": 25.0, "жиры": 33.0, "углеводы": 0.0},
    "Йогурт без добавок (100г)": {"калории": 60, "белки": 4.5, "жиры": 3.2, "углеводы": 3.5},
    # хлебобулочные изделия
    "Пицца (100г)": {"калории": 266, "белки": 11.4, "жиры": 9.8, "углеводы": 33.0},
    "Бургер (100г)": {"калории": 295, "белки": 13.0, "жиры": 14.0, "углеводы": 29.0},
    "Хлеб пшеничный (100г)": {"калории": 242, "белки": 8.1, "жиры": 1.0, "углеводы": 48.8},
    # сладкий перекус
    "Шоколад молочный (100г)": {"калории": 540, "белки": 6.9, "жиры": 35.7, "углеводы": 52.4},
    "Мороженое (100г)": {"калории": 207, "белки": 3.5, "жиры": 11.0, "углеводы": 23.5},
    "Печенье (100г)": {"калории": 440, "белки": 6.5, "жиры": 15.0, "углеводы": 69.5}
}

# память при клике кнопок
if "call" not in streamlit.session_state:
    streamlit.session_state.call = 0.0
if "belki" not in streamlit.session_state:
    streamlit.session_state.belki = 0.0
if "zir" not in streamlit.session_state:
    streamlit.session_state.zir = 0.0
if "uglevod" not in streamlit.session_state:
    streamlit.session_state.uglevod = 0.0    

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
        streamlit.session_state.norm_b = int(ves * 1.5)
        streamlit.session_state.norm_z = int(ves * 1.0)
        streamlit.session_state.norm_u = int(ves * 3.5)
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
             # информация о продуктах из списка
            product_info = food[food_choice]
                                                
            # расчет белков жиров углеводов и калорий
            call = (product_info["калории"] * grams) / 100
            belki = (product_info["белки"] * grams) / 100
            zir = (product_info["жиры"] * grams) / 100
            uglevod = (product_info["углеводы"] * grams) / 100
            
           # сумма белков жиров углеводов и калорий за день
            streamlit.session_state.call += call
            streamlit.session_state.belki += belki
            streamlit.session_state.zir += zir
            streamlit.session_state.uglevod += uglevod
                        
            # уведомление о добавлении
        #streamlit.toast("Добавлено:" + str(call) + "ккал!") 
        norm = streamlit.session_state.daily_norm
        eaten = streamlit.session_state.call
        left = max(0.0, norm - eaten)
        
        streamlit.header("Статистика за день:")
        streamlit.write("Съедено:" +str(eaten)+ "из"+ str(norm)+ "ккал")
        streamlit.write("Осталось съесть:"+ str(left)+ "калл")
        
        # Индикатор выполнения 
        progress = min(1.0, eaten / norm)
        streamlit.progress(progress)

        # БЖУ
        streamlit.header("Статистика БЖУ:")
        
        # Достаем съеденное и нормы из памяти
        b_eat = streamlit.session_state.belki
        z_eat = streamlit.session_state.zir
        u_eat = streamlit.session_state.uglevod
        
        b_norm = streamlit.session_state.norm_b
        z_norm = streamlit.session_state.norm_z
        u_norm = streamlit.session_state.norm_u
        
        # вывод белков
        streamlit.write("🥩 Белки:" + str(b_eat)+ "из" + str(b_norm)+ "г")
        streamlit.progress(min(1.0, b_eat / b_norm))
        
        # вывод жиров
        streamlit.write("🥑 Жиры:" + str(z_eat)+ "из" + str(z_norm)+ "г")
        streamlit.progress(min(1.0, z_eat / z_norm))
        
        # вывод углеводов
        streamlit.write("🍞 углеводы:" + str(u_eat)+ "из" + str(u_norm)+ "г")
        streamlit.progress(min(1.0, u_eat / u_norm))         
        
        # сброса дня в виде кнопки
        if streamlit.button("Очистить дневник питания"):
            streamlit.session_state.call= 0.0
            streamlit.session_state.belki = 0.0
            streamlit.session_state.zir = 0.0
            streamlit.session_state.uglevod = 0.0
            streamlit.rerun()
            streamlit.rerun()
