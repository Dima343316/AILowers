from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, send_file,flash,redirect,url_for
from User_bases import Data_Base
from complementary_functionality import last_file
from forms import LoginForm
from sweater import app,db
from models import Date,User
from flask_login import login_user,login_required,logout_user
from sqlalchemy.exc import IntegrityError
from num_to_rus import Converter

@app.route('/')
@login_required
def index():
    form = LoginForm()
    return render_template('index.html',form=form)


@app.route('/submit', methods=['GET','POST'])
@login_required
def submit():
    form = LoginForm()
    if request.method == 'POST':
        person = Date(Firstname_plaintiff = form.Firstname_plaintiff.data,
                        Lastname_plaintiff = form.Lastname_plaintiff.data,
                        Surname_plaintiff = form.Surname_plaintiff.data,
                        Plaintiff_place_of_birth = form.Plaintiff_place_of_birth.data,
                        Plantiff_identificator = form.Plantiff_identificator.data,
                        Plantiff_number = form.Plantiff_number.data,
                        Plantiff_email = form.Plantiff_email.data,
                        Date_discovered = request.form['date_discovered'],
                        Judicial_sector_number = form.Judicial_sector_number.data,
                        Judicial_sector_adress = form.Judicial_sector_adress.data,
                        Plantiffs_representative_name = form.Plantiffs_representative_name.data,
                        Plantiffs_representative_adress = form.Plantiffs_representative_adress.data,
                        Plantiffs_representative_identificate = form.Plantiffs_representative_identificate.data,
                        Plantiffs_representative_number = form.Plantiffs_representative_number.data,
                        Plantiffs_representative_email = form.Plantiffs_representative_email.data,
                        Defendant_name = form.Defendant_name.data,
                        Defendant_adress = form.Defendant_adress.data,
                        Defendant_INN = form.Defendant_INN.data,
                        Defendant_OGRN = form.Defendant_OGRN.data,
                        Defendant_number = form.Defendant_number.data,
                        Defendant_email = form.Defendant_email.data,
                        Data_main = request.form['date_main'],
                        Branch_name = form.Branch_name.data,
                        Contract_number = form.Contract_number.data,
                        Contract_necessary = form.Contract_necessary.data,
                        Sum_services = request.form['numberInput6'],
                        Sum_services_words = request.form['wordsOutput6'],
                        PaymentDate=request.form["paymentDate"],
                        Sum_credited_account=request.form['numberInput'],
                        Sum_credited_account_words=request.form['wordsOutput'],
                        PaymentProof=request.form['paymentProof'],
                        Assignment_number=form.Assignment_number.data,
                        Notification_date = request.form['notification_date'],
                        Flaws=form.Flaws.data,
                        Date_discovered_two = request.form['date_discovered2'],
                        Sum_moral_injury=request.form['numberInput5'],
                        Sum_moral_injury_words=request.form['wordsOutput5'],
                        Sum_penalty=request.form['numberInput2'],
                        Sum_penalty_words=request.form['wordsOutput2'],
                        Reconcilation=form.Reconcilation.data,
                        Eliminate_deficiency=form.Eliminate_deficiency.data,
                        Date_contract= request.form['date_contract'],
                        Documents_flaws=form.Documents_flaws.data,
                        Date_copy=request.form['date_copy'],
                        Number_contract=form.Number_contract.data,
                        Other_documents=form.Other_documents.data,
                      )
        db.session.add(person)
        db.session.commit()
        data_transformation = Data_Base(Date)
        data_transformation.processing_data_into_document()
    return render_template('loader.html', form=form)


@app.route('/loader')
@login_required
def loader():
    return render_template('loader.html')


@app.route('/success')
@login_required
def success():
    data = Date.query.order_by(Date.id.desc()).first()
    filename = last_file('sweater/docs/result/*')
    return render_template('success.html',data=data, filename=filename)



@app.route('/download/<path:filename>', methods=['GET'])
@login_required
def download(filename):
    return send_file(filename, as_attachment=True)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('email')
    password = request.form.get('password')
    #Если данные есть в бд
    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)


            return redirect(url_for('index'))
        else:
            flash('Login or password is not correct')
    else:
        flash('Please fill login and password fields')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    try:
        if request.method == 'POST':
            if not (login or password or password2):
                flash('Please, fill all fields!')
            elif password != password2:
                flash('Passwords are not equal!')
            else:
                hash_pwd = generate_password_hash(password)
                new_user = User(login=login, password=hash_pwd)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('login_page'))
    except IntegrityError:
        flash('Этот логи уже занят')
    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


#Проверка если пользователь хочет попасть на страницу которая не открываетс без входа
@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)
    return response



