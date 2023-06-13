from flask import Flask, request, render_template, redirect, session
from flask_session import Session
import tmdbsimple as tmdb
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
import helpers
import time
import random
iso_lang = 'uk'
year_list = range(1900, 2017)
month_list = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
day_list = range(1,32)
country_list = ["Австралія","Австрія","Азербайджан","Аландські Острови","Албанія","Алжир","Американське Самоа","Ангола","Анґілья","Андорра","Антарктика","Антиґуа і Барбуда","Аргентина","Аруба","Афганістан","Багамські Острови","Бангладеш","Барбадос","Бахрейн","Беліз","Бельґія","Бенін","Бермудські Острови","Білорусь","Болгарія","Болівія","Боснія і Герцеґовина","Ботсвана","Бразілія","Британська територія в Індійському Океані","Британські Віргінські острови","Бруней","Буркіна-Фасо","Бурунді","Бутан","Вануату","Ватикан","Велика Британія","Венесуела","Віддалені острови США","Віргінські острови США","Вірменія","Вʼєтнам","Габон","Гаїті","Гамбія","Гана","Гвінея","Гвінея-Бісау","Гондурас","Гонконг О.А.Р. Китаю","Греція","Грузія","Ґайана","Ґваделупа","Ґватемала","Ґернсі","Ґібралтар","Ґренада","Ґренландія","Ґуам","Данія","Джерсі","Джибуті","Домініка","Домініканська Республіка","Еквадор","Екваторіальна Гвінея","Еритрея","Есватіні","Естонія","Ефіопія","Єгипет","Ємен","Замбія","Західна Сахара","Зімбабве","Ізраїль","Індія","Індонезія","Ірак","Іран","Ірландія","Ісландія","Іспанія","Італія","Йорданія","Кабо-Верде","Казахстан","Кайманові Острови","Камбоджа","Камерун","Канада","Катар","Кенія","Киргизстан","Китай","Кіпр","Кірібаті","Кокосові (Кілінґ) Острови","Колумбія","Комори","Конго – Браззавіль","Конго – Кіншаса","Коста-Ріка","Кот-дʼІвуар","Куба","Кувейт","Кюрасао","Лаос","Латвія","Лесото","Литва","Ліберія","Ліван","Лівія","Ліхтенштейн","Люксембурґ","Мавританія","Маврікій","Мадагаскар","Майотта","Макао О.А.Р Китаю","Малаві","Малайзія","Малі","Мальдіви","Мальта","Марокко","Мартініка","Маршаллові Острови","Мексика","Мікронезія","Мозамбік","Молдова","Монако","Монголія","Монтсеррат","Мʼянма (Бірма)","Намібія","Науру","Непал","Нігер","Нігерія","Нідерланди","Нідерландські Карибські острови","Нікараґуа","Німеччина","Ніуе","Нова Зеландія","Нова Каледонія","Норвеґія","Обʼєднані Арабські Емірати","Оман","Острів Буве","Острів Мен","Острів Норфолк","Острів Різдва","Острів Святої Єлени","Острови Герд і Макдоналд","Острови Кука","Острови Піткерн","Острови Теркс і Кайкос","Пакистан","Палау","Палестинські території","Панама","Папуа-Нова Ґвінея","Параґвай","Перу","Південна Джорджія та Південні Сандвічеві Острови","Південна Корея","Південний Судан","Південно-Африканська Республіка","Північна Корея","Північна Македонія","Північні Маріанські Острови","Польща","Портуґалія","Пуерто-Ріко","Реюньйон","Росія","Руанда","Румунія","Сальвадор","Самоа","Сан-Маріно","Сан-Томе і Прінсіпі","Саудівська Аравія","Сейшельські Острови","Сен-Бартельмі","Сен-Мартен","Сен-Пʼєр і Мікелон","Сенегал","Сент-Вінсент і Ґренадіни","Сент-Кітс і Невіс","Сент-Люсія","Сербія","Сирія","Сінгапур","Сінт-Мартен","Словаччина","Словенія","Соломонові Острови","Сомалі","Сполучені Штати","Судан","Сурінам","Сьєрра-Леоне","Таджикистан","Таїланд","Тайвань","Танзанія","Тімор-Лешті","Того","Токелау","Тонґа","Трінідад і Тобаґо","Тувалу","Туніс","Туреччина","Туркменістан","Уганда","Угорщина","Узбекистан","Україна","Уолліс і Футуна","Уруґвай","Фарерські Острови","Фіджі","Філіппіни","Фінляндія","Фолклендські Острови","Франція","Французька Ґвіана","Французька Полінезія","Французькі Південні Території","Хорватія","Центральноафриканська Республіка","Чад","Чехія","Чілі","Чорногорія","Швейцарія","Швеція","Шпіцберген та Ян-Маєн","Шрі-Ланка","Ямайка","Японія"]

app = Flask(__name__)
tmdb.API_KEY = 'a226dc76ef8faffb3de8936a53580b62'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQL("sqlite:///data.db")
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/search", methods=["GET", "POST"])
@helpers.login_required
def search():
    if request.method == "POST":
        input = request.form.get('search')
        if not input:
            return redirect("/")
        search = tmdb.Search()
        response = search.movie(query=input,language=iso_lang)
        res = response["results"]
        return render_template("search.html", res=res, search=input)
    else:
        return render_template("search.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        login = request.form.get('login')
        passw1 = request.form.get('passw1')
        passw2 = request.form.get('passw2')
        name = request.form.get("name")
        surname = request.form.get("surname")
        nick = request.form.get("nick")
        if not nick:
            nick = login
        failure1 = "Чогось не вистачає"
        failure2 = "Паролі не співпали"
        failure3 = "Користувач з таким логіном або ніком вже є"
        failure4 = "Пароль не відповідає вимогам" 
        failure5 = "Занадто довгий логін"
        if not login or not passw1 or not passw2:
            return render_template("register.html", error=failure1)
        if passw1 != passw2:
            return render_template("register.html", error=failure2)
        if len(passw1) > 21 or len(passw1) < 8:
            return render_template("register.html", error=failure4)
        if len(login) > 21:
            return render_template("register.html", error=failure5)
        if not db.execute("SELECT login FROM user WHERE login=?", login) and not db.execute("SELECT nick FROM user WHERE nick=?", nick):
            db.execute("INSERT INTO user (nick, name, surname, password, login) VALUES (?,?,?,?,?)", nick, name, surname, generate_password_hash(passw1), login)
            data = db.execute("SELECT * FROM user WHERE login=?", login)
            session_id = data[0]['user_id']
            session['user_id'] = session_id
            return redirect("/additional")
        else:
            return render_template("register.html", error=failure3)
    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form.get('login')
        passw = request.form.get('passw')
        failure1 = "Чогось не вистачає"
        failure2 = "Неправильний логін чи пароль"
        if not login or not passw:
            return render_template("login.html", error=failure1)
        data = db.execute("SELECT * FROM user WHERE login=?", login)
        if len(data) != 1 or not check_password_hash(data[0]['password'], passw):
            return render_template("login.html", error=failure2)
        session['user_id'] = data[0]['user_id']
        return redirect('/')
    else: 
        return render_template("login.html")

@app.route("/logout")
@helpers.login_required
def logout():
    session.clear()
    return redirect("/login")

@app.route("/", methods=["GET", "POST"])
@helpers.login_required
def index():
    if request.method == "POST":
        edit = True
        id = request.form.get("id")
        if id:
            db.execute("DELETE FROM watched WHERE user_id=? AND film_id=?", session["user_id"], id)
        user_data = db.execute("SELECT * FROM user WHERE user_id=?", session['user_id'])
        user = user_data[0]
        response = db.execute("SELECT * FROM watched WHERE user_id=?", session['user_id'])
        return render_template("index.html", edit=edit, user=user, response=response)
    else:  
        code1 = request.args.get("code1")
        success1 = "Ви успішно додали фільм!"
        user_data = db.execute("SELECT * FROM user WHERE user_id=?", session['user_id'])
        user = user_data[0]
        response = db.execute("SELECT * FROM watched WHERE user_id=?", session['user_id'])
        if code1:
            return render_template("index.html", success=success1, response=response, user=user)
        elif not code1:
            return render_template("index.html", response=response, user=user)

@app.route("/movie")
@helpers.login_required
def movie():
    error = request.args.get("error")
    id = request.args.get("id")
    movie = tmdb.Movies(id)
    result = movie.info(language=iso_lang)
    runtime = time.strftime("%H год. %M хв.", time.gmtime(int(result["runtime"]) * 60))
    return render_template("movie.html", res=result, runtime=runtime, error=error)

@app.route("/add", methods=["GET", "POST"])
@helpers.login_required
def add():
    if request.method == "GET":
        id = request.args.get("id")
        movie = tmdb.Movies(id)
        result = movie.info(language=iso_lang)
        check = db.execute("SELECT * FROM watched WHERE film_id=? AND user_id=?", id, session['user_id'])
        failure = "Схоже ви вже додали цей фільм!"
        if not check:
            return render_template("add.html", res=result)
        else:
            return redirect(f"/movie?id={id}&error={failure}")
    else:
        id = request.form.get("id")
        rate = request.form.get("rate")
        if rate:
            rate = int(rate)
        movie = tmdb.Movies(id)
        result = movie.info(language=iso_lang)
        comment = request.form.get("comment")
        if len(comment) > 21:
            return render_template("add.html", res=result, error="Занадто довгий коментар")
        db.execute("INSERT INTO watched (user_id, film_id, rating, film_comment, film_title, poster_path) VALUES (?,?,?,?,?,?)", session['user_id'], id, rate, comment, result['title'], result['poster_path'])
        return redirect("/?code1=1")

@app.route("/add_thread", methods=["GET", "POST"])
@helpers.login_required
def add_thread():
    if request.method == "GET":
        id = request.args.get("id")
        movie = tmdb.Movies(id)
        result = movie.info(language=iso_lang)
        return render_template("add_thread.html", res=result)
    else: 
        id = request.form.get("id")
        movie = tmdb.Movies(id)
        result = movie.info(language=iso_lang)
        theme = request.form.get("theme")
        question = request.form.get("question")
        failure1 = "Тема занадто довга"
        failure2 = "Питання занадто довге"
        failure3 = "Задайте якесь питання"
        if len(theme) > 21:
            return render_template("add_thread.html", res=result, error=failure1)
        if not theme:
            return render_template("add_thread.html", res=result, error=failure3)
        if not question:
            question = "Без запитання"
        if len(question) > 140:
            return render_template("add_thread.html", res=result, error=failure2)
        db.execute("INSERT INTO thread (film_id, author_id, question, theme, poster_path, film_title) VALUES (?,?,?,?,?,?)", id, session["user_id"], question, theme, result["poster_path"], result["title"])
        return redirect("/forum?code1=1")

@app.route("/forum", methods=["GET", "POST"])
@helpers.login_required
def forum():
    success_code = request.args.get("code1")
    success = ""
    if success_code:
        success = "Ви успішно створили обговорення!"
    result = db.execute("SELECT * FROM thread")
    return render_template("forum.html", res=result, success=success)

@app.route("/thread", methods=["GET", "POST"])
@helpers.login_required
def thread():
    if request.method == "GET":
        id = request.args.get("id")
        delete = request.args.get("del")
        result = db.execute("SELECT * FROM thread WHERE thread_id=?", id)
        comments = db.execute("SELECT * FROM comment JOIN user ON comment.author_id = user.user_id WHERE thread_id=?", id)
        user_id = result[0]["author_id"]
        username_unf = db.execute("SELECT nick FROM user WHERE user_id=?", user_id)
        if delete:
            db.execute("DELETE FROM thread WHERE thread_id=?", id)
            db.execute("DELETE FROM commenе WHERE thread_id=?", id)
            return redirect("/forum")
        return render_template("thread.html", result=result[0], comments=comments, author=username_unf[0])
    else:
        id = request.form.get("id")
        author_id = request.form.get("author_id")
        thread_id = request.form.get("thread_id")
        comment = request.form.get("comment")
        failure1 = "Будь ласка, залиште коментар"
        failure2 = "Занадто довгий коментар"
        if not comment:
            return redirect(f"/thread?id={thread_id}")
        if len(comment) > 140: 
            return redirect(f"/thread?id={thread_id}")
        db.execute("INSERT INTO comment (thread_id, author_id, comment_text) VALUES (?,?,?)", thread_id, author_id, comment)
        return redirect(f"/thread?id={thread_id}")

@app.route("/reccomendation", methods=["GET", "POST"])
@helpers.login_required
def reccomendation():
        return render_template("reccomendation.html")

@app.route("/discover", methods=["GET", "POST"])
@helpers.login_required
def discover():
    if request.method == "POST":
        mood = request.form.get("choice")
        genre_list = [28, 12, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 9648, 10749, 878, 10770, 53, 10752, 37]
        genres = []
        if mood == "angry_1":
            genres.append(35)
        elif mood == "angry_2":
            genres.append(80)
        elif mood == "funny_1":
            genres.append(35)
        elif mood == "funny_2":
            genres.append(27)
        elif mood == "coquettish_1":
            genres.append(10749)
        elif mood == "sad_1":
            genres.append(18)
        elif mood == "sad_2":
            genres.append(35)
        elif mood == "neutral":
            genres.append(random.choice(genre_list))
        discover = tmdb.Discover()
        response = discover.movie(language=iso_lang, with_genres=genres, sort_by='popularity.desc')
        print(response)
        response = response["results"]
    return render_template("discover.html", res=response)

@app.route("/additional", methods=["GET", "POST"])
@helpers.login_required
def additional():
    if request.method == "POST":
        origin_country = request.form.get("origin_country")
        if len(origin_country) > 58:
            return render_template("additional.html", error="Занадто довга назва країни")
        year = request.form.get("year")
        month = request.form.get("month")
        day = request.form.get("day")
        gender = request.form.get("gender")
        if gender == "Інше":
            gender = request.form.get("gender_another")
        db.execute("UPDATE user SET origin_country=?, gender=?, birth_year=?, birth_month=?, birth_day=? WHERE user_id=?", origin_country, gender, year, month, day, session["user_id"])
        return redirect("/")
    else:
        return render_template("additional.html", year=year_list, month=month_list, day=day_list, countries=country_list)

@app.route("/edit_profile", methods=["GET", "POST"])
@helpers.login_required
def edit_profile():
    if request.method == "POST":
        nick = request.form.get("nick")
        name = request.form.get("name")
        surname = request.form.get("surname")
        origin_country = request.form.get("origin_country")
        year = request.form.get("year")
        month = request.form.get("month")
        day = request.form.get("day")
        gender = request.form.get("gender")
        if len(nick) > 21:
            return render_template("register.html", error="Занадто довгий логін")
        if len(origin_country) > 58:
            return render_template("edit_profile", error ="Занадто довга назва країни")
        if not nick:
            user = db.execute("SELECT login FROM user WHERE user_id=?", session["user_id"])
            nick = user[0]["login"]
        if not gender:
            gender = "Не вказано"
        if gender == "Інше":
            gender = request.form.get("gender_another")
            if not gender:
                gender = "Інше"
        db.execute("UPDATE user SET nick=?, name=?, surname=?, origin_country=?, gender=?, birth_year=?, birth_month=?, birth_day=? WHERE user_id=?", nick, name, surname, origin_country, gender, year, month, day, session["user_id"])
        return redirect("/")

    else:
        response = db.execute("SELECT * FROM user WHERE user_id=?", session["user_id"])
        return render_template("edit_profile.html", res=response[0], year=year_list, month=month_list, day=day_list, countries=country_list)