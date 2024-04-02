from sqlalchemy import Column, DateTime, func
from sweater import db,manager
from datetime import datetime
from flask_login import UserMixin


class Date(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer,primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    Firstname_plaintiff = db.Column(db.String(40))
    Lastname_plaintiff = db.Column(db.String(40))
    Surname_plaintiff = db.Column(db.String(40))
    Plaintiff_place_of_birth = db.Column(db.String(150))
    Plantiff_identificator = db.Column(db.String(150))
    Plantiff_number = db.Column(db.String(15))
    Plantiff_email = db.Column(db.String(59))
    Date_discovered = db.Column(db.String(60))
    Judicial_sector_number = db.Column(db.String(15))
    Judicial_sector_adress = db.Column(db.String(15))
    Plantiffs_representative_name = db.Column(db.String(60))
    Plantiffs_representative_adress = db.Column(db.String(150))
    Plantiffs_representative_identificate = db.Column(db.String(100))
    Plantiffs_representative_number = db.Column(db.String(15))
    Plantiffs_representative_email = db.Column(db.String(60))
    Defendant_name = db.Column(db.String(15))
    Defendant_adress = db.Column(db.String(60))
    Defendant_INN = db.Column(db.String(60))
    Defendant_OGRN = db.Column(db.String(60))
    Defendant_number = db.Column(db.String(15))
    Defendant_email = db.Column(db.String(60))
    Data_main = db.Column(db.String(50))
    Branch_name = db.Column(db.String(60))
    Contract_number = db.Column(db.String(40))
    Contract_necessary = db.Column(db.String(40))
    Sum_services = db.Column(db.String(150))
    Sum_services_words = db.Column(db.String(150))
    PaymentDate = db.Column(db.String(15))
    Sum_credited_account = db.Column(db.String(60))
    Sum_credited_account_words = db.Column(db.String(50))
    PaymentProof = db.Column(db.String(15))
    Assignment_number = db.Column(db.String(25))
    Notification_date = db.Column(db.String(15))
    Flaws = db.Column(db.String(300))
    Date_discovered_two = db.Column(db.String(15))
    Sum_moral_injury = db.Column(db.String(40))
    Sum_moral_injury_words = db.Column(db.String(40))
    Sum_penalty = db.Column(db.String(150))
    Sum_penalty_words = db.Column(db.String(150))
    Reconcilation = db.Column(db.String(150))
    Eliminate_deficiency = db.Column(db.String(50))
    Date_contract = db.Column(db.String(15))
    Documents_flaws = db.Column(db.String(150))
    Date_copy = db.Column(db.String(15))
    Number_contract = db.Column(db.String(15))
    Other_documents = db.Column(db.String(300))



    def __init__(self,Firstname_plaintiff, Lastname_plaintiff, Plantiff_identificator,
                 Plaintiff_place_of_birth, Surname_plaintiff, Plantiff_number,
                 Plantiff_email,Date_discovered,Judicial_sector_number,Judicial_sector_adress,Plantiffs_representative_name,
                 Plantiffs_representative_adress, Plantiffs_representative_identificate, Plantiffs_representative_number,
                 Plantiffs_representative_email, Defendant_name, Defendant_adress, Defendant_INN, Defendant_OGRN, Defendant_number, Defendant_email,Data_main,
                 Notification_date, Branch_name, Contract_number, Contract_necessary, Sum_services, Sum_services_words, PaymentDate, Sum_credited_account,
                 Sum_credited_account_words, PaymentProof, Assignment_number, Flaws, Date_discovered_two, Sum_moral_injury, Sum_moral_injury_words, Sum_penalty, Sum_penalty_words,
                 Reconcilation, Eliminate_deficiency, Date_contract, Documents_flaws, Date_copy, Number_contract, Other_documents):

        self.Defendant_OGRN = Defendant_OGRN
        self.Date_discovered_two = Date_discovered_two
        self.Notification_date = Notification_date
        self.Data_main = Data_main
        self.Other_documents = Other_documents
        self.Number_contract = Number_contract
        self.Date_copy = Date_copy
        self.Documents_flaws = Documents_flaws
        self.Date_contract = Date_contract
        self.Eliminate_deficiency = Eliminate_deficiency
        self.Reconcilation = Reconcilation
        self.Sum_penalty_words = Sum_penalty_words
        self.Sum_penalty = Sum_penalty
        self.Sum_moral_injury = Sum_moral_injury
        self.Flaws = Flaws
        self.Assignment_number = Assignment_number
        self.PaymentProof = PaymentProof
        self.Sum_credited_account_words = Sum_credited_account_words
        self.Sum_credited_account = Sum_credited_account
        self.PaymentDate = PaymentDate
        self.Sum_moral_injury_words = Sum_moral_injury_words
        self.Sum_services_words = Sum_services_words
        self.Sum_services = Sum_services
        self.Contract_necessary = Contract_necessary
        self.Contract_number = Contract_number
        self.Branch_name = Branch_name
        self.Notification_date = Notification_date
        self.Defendant_email = Defendant_email
        self.Defendant_number = Defendant_number
        self.Defendant_INN = Defendant_INN
        self.Defendant_adress = Defendant_adress
        self.Defendant_name = Defendant_name
        self.Plantiffs_representative_email = Plantiffs_representative_email
        self.Plantiffs_representative_number = Plantiffs_representative_number
        self.Plantiffs_representative_identificate = Plantiffs_representative_identificate
        self.Plantiffs_representative_adress = Plantiffs_representative_adress
        self.Plantiffs_representative_name = Plantiffs_representative_name
        self.Judicial_sector_adress = Judicial_sector_adress
        self.Judicial_sector_number = Judicial_sector_number
        self.Date_discovered = Date_discovered
        self.Plantiff_email = Plantiff_email
        self.Plantiff_number = Plantiff_number
        self.Surname_plaintiff = Surname_plaintiff
        self.Lastname_plaintiff = Lastname_plaintiff
        self.Firstname_plaintiff = Firstname_plaintiff
        self.Plaintiff_place_of_birth = Plaintiff_place_of_birth
        self.Plantiff_identificator = Plantiff_identificator


class User (UserMixin, db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer,primary_key=True)
    login = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(150),nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
