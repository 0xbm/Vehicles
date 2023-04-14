import openpyxl
import datetime

wb = openpyxl.load_workbook("style.xlsx")
ws = wb.active


class Text:
    def card_name(self):

        ws['A1'] = 'ROZLICZENIE MIESIĘCZNE ZUŻYCIA PALIWA'
        wb.save("style.xlsx")

    def brand(self):
        wb = openpyxl.load_workbook("style.xlsx")
        ws = wb.active

        ws['A3'] = 'Pojazd służbowy, marka'
        wb.save("style.xlsx")

    def registration_number(self):
        wb = openpyxl.load_workbook("style.xlsx")
        ws = wb.active

        ws['A4'] = 'Nr rejestracyjny'
        wb.save("style.xlsx")

    def month(self):
        wb = openpyxl.load_workbook("style.xlsx")
        ws = wb.active

        ws['A5'] = 'Miesiąc'
        ws['B5'] = wb.sheetnames[0]
        wb.save("style.xlsx")

    def year(self):
        wb = openpyxl.load_workbook("style.xlsx")
        ws = wb.active

        ws['C5'] = 'rok'
        year = datetime.datetime.today().year

        ws['D5'] = year
        wb.save("style.xlsx")

    def count_beginning_month(self):
        wb = openpyxl.load_workbook("style.xlsx")
        ws = wb.active

        ws['A6'] = '1. Stan licznika na początku miesiąca'
        wb.save("style.xlsx")

    def count_ending_month(self):
        wb = openpyxl.load_workbook("style.xlsx")
        ws = wb.active

        ws['A7'] = '2. Stan licznika na końcu miesiąca'
        wb.save("style.xlsx")

    def km_in_month(self):
        wb = openpyxl.load_workbook("style.xlsx")
        ws = wb.active

        ws['A8'] = '3. Przejechano km/mth w miesiącu'
        wb.save("style.xlsx")

    def fuel__reamaining_last_month(self):
        wb = openpyxl.load_workbook("style.xlsx")
        ws = wb.active

        ws['A9'] = '4.	Stan paliwa pozostałego z ubiegłego miesiąca'
        wb.save("style.xlsx")

    def fuel_purchased_in_month(self):
        wb = openpyxl.load_workbook("style.xlsx")
        ws = wb.active

        ws['A10'] = '5.Ilość paliwa zakupionego w miesiącu '
        wb.save("style.xlsx")


text = Text()
text.card_name()
text.brand()
text.registration_number()
text.month()
text.year()
text.count_beginning_month()
text.count_ending_month()
text.fuel__reamaining_last_month()
text.fuel_purchased_in_month()
text.km_in_month()
