import calendar
import openpyxl
from openpyxl import Workbook


class Style:
    def create_months(self, wb=Workbook()):
        months = [calendar.month_name[i] for i in range(1, 13)]

        for worksheet in months:
            wb.create_sheet(worksheet)

        del wb["Sheet"]
        wb.save("card.xlsx")

    def merge_cells(self):
        wb = openpyxl.load_workbook("card.xlsx")
        ws = wb["January"]
        #  ustaw zmiena sheet np na luty.
        ws.merge_cells("A1:E1")
        ws.merge_cells("A3:C3")
        ws.merge_cells("A4:B4")
        ws.merge_cells("A1:B1")
        ws.merge_cells("A6:C6")
        ws.merge_cells("A7:C7")
        ws.merge_cells("A8:C8")
        ws.merge_cells("A9:C9")
        ws.merge_cells("A10:C10")
        ws.merge_cells("A11:C11")

        wb.save("card.xlsx")


template = Style()
template.create_months()
template.merge_cells()
