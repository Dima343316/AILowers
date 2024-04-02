from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, IntegerField, TelField, EmailField,BooleanField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    Judicial_sector_number = IntegerField("Укажите номер участка МИРОВОГО СУДЬИ",render_kw={"placeholder":"Укажите номер участка МИРОВОГО СУДЬИ"})
    Judicial_sector_adress = StringField("Укажите адрес участка МИРОВОГО СУДЬИ", [validators.Length(min=4, max=150)], render_kw={"placeholder":"Укажите адрес участка МИРОВОГО СУДЬИ"})
    Firstname_plaintiff = StringField("Фамилия", [validators.Length(min=4, max=25, message='Gfhjkm')], render_kw={"placeholder":"Фамилия"})
    Lastname_plaintiff =  StringField("Имя", [validators.Length(min=4, max=25)], render_kw={"placeholder":"Имя"})
    Surname_plaintiff = StringField("Отчество", [validators.Length(min=4, max=25)], render_kw={"placeholder":"Отчество"})
    Plaintiff_place_of_birth =  StringField("Место жительства или пребывания", [validators.Length(min=4, max=200)], render_kw={"placeholder":"Место жительства или пребывания"})
    Plantiff_identificator = StringField("Один из идентификаторов: СНИЛС, ИНН, серия и номер паспорта, серия и номер водительского удостоверения", [validators.Length(min=4, max=200)], render_kw={"placeholder":"Например: ИНН - 123213123, паспорт - 1718624002"})
    Plantiff_number = TelField("Телефон/факс", [validators.Length(min=4, max=15)], render_kw={"placeholder":"+7(999)999-99-99"})
    Plantiff_email = EmailField('Адрес электронной почты', [validators.DataRequired(), validators.Email()], render_kw={"placeholder":"Например: mygre@ema.il"})
    Firstname_plantiffs_representative= StringField("FirstName", [validators.Length(min=4, max=25)],render_kw={"placeholder": "Фамилия"})
    Lastname_plantiffs_representative = StringField("LastName", [validators.Length(min=4, max=25)], render_kw={"placeholder": "Имя"})
    Surname_plantiffs_representative = StringField("SurName", [validators.Length(min=4, max=25)],render_kw={"placeholder": "Отчество"})
    Plantiffs_representative_name = StringField("Наименование", [validators.Length(min=4, max=25)], render_kw={"placeholder":"Наименование"})
    Plantiffs_representative_adress = StringField("Адрес для направления судебных, извещений", [validators.Length(min=4, max=200)], render_kw={"placeholder":"Адрес для направления судебных, извещений"})
    Plantiffs_representative_identificate = StringField("Один из идентификаторов: СНИЛС, ИНН, серия и номер паспорта, серия и номер водительского удостоверения", [validators.Length(min=4, max=200)], render_kw={"placeholder":"Один из идентификаторов"})
    Plantiffs_representative_number = TelField("Телефон", [validators.Length(min=4, max=25)], render_kw={"placeholder":"+7(999)999-99-99"})
    Plantiffs_representative_email = EmailField('Адрес электронной почты', [validators.DataRequired(), validators.Email()], render_kw={"placeholder":"Например: mygre@ema.il"})
    Defendant_name = StringField("Наименование", [validators.Length(min=4, max=30)], render_kw={"placeholder":"Наименование"})
    Defendant_adress = StringField("Адрес для направления судебных, извещений", [validators.Length(min=4, max=150)], render_kw={"placeholder":"Адрес для направления судебных, извещений"})
    Defendant_INN = IntegerField("ИНН", render_kw={"placeholder":"ИНН"})
    Defendant_OGRN = IntegerField("ОГРН", render_kw={"placeholder":"ОГРН"})
    Defendant_number = TelField("Телефон", [validators.Length(min=4, max=30)], render_kw={"placeholder":"+7(999)999-99-99"})
    Defendant_email = EmailField('Адрес электронной почты', [validators.DataRequired(), validators.Email()], render_kw={"placeholder":"Например: mygre@ema.il"})
    Branch_name = StringField("Наименование филиала", [validators.Length(min=4, max=30)], render_kw={"placeholder":"Наименование филиала"})
    Contract_number = IntegerField("Номер договора",render_kw={"placeholder":"Номер договора"})
    Contract_necessary = StringField("Детали договора", [validators.Length(min=4, max=200)], render_kw={"placeholder":"Детали договора"})
    Sum_services = IntegerField("Стоимость услуг сумма цифрами:",  render_kw={"placeholder":"Сумма цифрами(в рублях)"})
    Sum_services_words = StringField("Стоимость услуг сумма прописью:", [validators.Length(min=4, max=200)], render_kw={"placeholder":"Сумма прописью(в рублях)"})
    Sum_credited_account = IntegerField("Сумма платежа цифрами:", render_kw={"placeholder":"Сумма цифрами(в рублях)"})
    Sum_credited_account_words = StringField("Сумма платежа прописью:", [validators.Length(min=4, max=30)], render_kw={"placeholder":"Сумма прописью(в рублях)"})
    Assignment_number = IntegerField("Номер платежного поручения:", render_kw={"placeholder":"Номер платежного поручения"})
    Reconcilation = StringField("Сведения о предпринятых действиях, направленных на примирение:", [validators.Length(min=4, max=200)], render_kw={"placeholder":"Сведения о предпринятых действиях, направленных на примирение:"})
    Flaws = StringField("Обнаруженные недостатки", [validators.Length(min=4, max=200)], render_kw={"placeholder":"Обнаруженные недостатки"})
    Eliminate_deficiency = StringField("Обязать Ответчика безвозмездно устранить существенный недостаток, а именно:", [validators.Length(min=4, max=500)], render_kw={"placeholder":"Обязать Ответчика безвозмездно устранить существенный недостаток, а именно:"})
    Sum_moral_injury = IntegerField("Сумма взысканной неустойки цифрами (пени)", render_kw={"placeholder":"Сумма цифрами(в рублях)"})
    Sum_moral_injury_words = StringField("Сумма взысканной неустойки прописью (пени)", [validators.Length(min=4, max=100)], render_kw={"placeholder":"Сумма прописью(в рублях)"})
    Sum_penalty = IntegerField("Сумма компенсации морального вреда цифрами", render_kw={"placeholder":"Сумма цифрами(в рублях)"})
    Sum_penalty_words = StringField("Сумма компенсации морального вреда прописью", [validators.Length(min=4, max=100)], render_kw={"placeholder":"Сумма прописью(в рублях)"})
    Number_contract = IntegerField("Номер копии договора",  render_kw={"placeholder":"Номер копии договора"})
    Documents_flaws = StringField("Документы, подтверждающие совершение стороной (сторонами) действий, направленных на примирение", [validators.Length(min=4, max=500)], render_kw={"placeholder":"Документы, подтверждающие совершение стороной (сторонами) действий, направленных на примирение"})
    Other_documents = StringField("Другие документы подтверждающие обстоятельства, на которых истец основывает свои требования", [validators.Length(min=4, max=500)], render_kw={"placeholder":"Другие документы подтверждающие обстоятельства, на которых истец основывает свои требования"})
    consent = BooleanField('Согласие на обработку персональных данных', validators=[DataRequired()])
    submit = SubmitField("Отправить")

class LoginForms(FlaskForm):
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    psw = PasswordField("Пароль: ", validators=[DataRequired(),
                                                Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")])
    remember = BooleanField("Запомнить", default = False)
    submit = SubmitField("Войти")

class RegisterForm(FlaskForm):
    name = StringField("Имя: ", validators=[Length(min=4, max=100, message="Имя должно быть от 4 до 100 символов")])
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    psw = PasswordField("Пароль: ", validators=[DataRequired(),
                                                Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")])

    psw2 = PasswordField("Повтор пароля: ", validators=[DataRequired(), EqualTo('psw', message="Пароли не совпадают")])
    submit = SubmitField("Регистрация")

