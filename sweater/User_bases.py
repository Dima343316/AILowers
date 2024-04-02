from sqlalchemy import exc, desc
from complementary_functionality import PasteValues

engine = 'postgresql://constantine:dox123456@localhost/data_peoples'

class Data_Base:
    def __init__(self, postgres_database):
        self.postgres_database = postgres_database

    def execute_query(self):
        try:
            return self.postgres_database.query.first()

        except exc.SQLAlchemyError as e:
            print(type(e))


    def processing_data_into_document(self):
        try:
            # Получаем последний выполненный запрос
            query = self.postgres_database.query.order_by(desc(self.postgres_database.created_at)).first()
            result_dict = {
                "judicial_sector_number": f"{query.Judicial_sector_number}",
                "judicial_sector_adress": f"{query.Judicial_sector_adress}",
                "firstname_plaintiff": f"{query.Firstname_plaintiff}",
                "lastname_plaintiff": f"{query.Lastname_plaintiff}",
                "surname_plaintiff": f"{query.Surname_plaintiff}",
                "plaintiff_place_of_birth": f"{query.Plaintiff_place_of_birth}",
                "plantiff_identificator": f"{query.Plantiff_identificator}",
                "plantiff_number": f"{query.Plantiff_number}",
                "plantiff_email": f"{query.Plantiff_email}",
                "data_discovered": f"{query.Date_discovered}",
                "plantiffs_representative_name": f"{query.Plantiffs_representative_name}",
                "lastname_plantiffs_representative": f"{query.Plantiffs_representative_name}",
                "surname_plantiffs_representative": f"{query.Plantiffs_representative_name}",
                "plantiffs_representative_adress": f"{query.Plantiffs_representative_adress}",
                "Plantiffs_representative_identificate": f"{query.Plantiffs_representative_identificate}",
                "plantiffs_representative_number": f"{query.Plantiffs_representative_number}",
                "plantiffs_representative_email": f"{query.Plantiffs_representative_email}",
                "defendant_name": f"{query.Defendant_name}",
                "defendant_adress": f"{query.Defendant_adress}",
                "defendant_INN": f"{query.Defendant_INN}",
                "defendant_OGRN": f"{query.Defendant_OGRN}",
                "defendant_number": f"{query.Defendant_number}",
                "defendant_email": f"{query.Defendant_email}",
                "day_month_year": f"{query.Data_main}",
                "branch_name": f"{query.Branch_name}",
                "contract_number": f"{query.Contract_number}",
                "contract_necessary": f"{query.Contract_necessary}",
                "sum_services": f"{query.Sum_services}",
                "sum_services_words":f"{query.Sum_services_words}",
                "day_month_year_credited_account": f"{query.PaymentDate}",
                "sum_credited_account": f"{query.Sum_credited_account}",
                "sum_credited_account_words": f"{query.Sum_credited_account_words}",
                "day_month_year_assigment": f"{query.PaymentProof}",
                "assignment_number": f"{query.Assignment_number}",
                "day_month_year_flaws": f"{query.Date_discovered_two}",
                "flaws": f"{query.Flaws}",
                "day_month_year_branch": f"{query.Notification_date}",
                "sum_pinalties": f"{query.Sum_penalty}",
                "sum_pinalties_words": f"{query.Sum_penalty_words}",
                "sum_moral_injury": f"{query.Sum_moral_injury}",
                "sum_moral_injury_words": f"{query.Sum_moral_injury_words}",
                "reconcilation": f"{query.Reconcilation}",
                "eliminate_deficiency": f"{query.Eliminate_deficiency}",
                "sum_penalty": f"{query.Sum_penalty}",
                "sum_penalty_words": f"{query.Sum_penalty_words}",
                "day_month_year_copy_contract": f"{query.Date_copy}",
                "number_contract": f"{query.Number_contract}",
                "documents_flaws": f"{query.Documents_flaws}",
                "day_month_year_copy_defandant": f"{query.Judicial_sector_number}",
                "other_documents": f"{query.Judicial_sector_number}"
            }

            data_insert = PasteValues(result_dict)
            data_insert.change_values()


        except exc.SQLAlchemyError as e:
            print(type(e))



