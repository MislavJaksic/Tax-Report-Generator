from TaxReportGenerator.Settings import DataSettings



sample_data_file_path = "data/test_data/TestData.xlsx"
sample_data_excel_columns = "B,C,D,E,F,G"
sample_data_renaming_labels = ["name_one", "name_two", "name_three", "name_four", "name_five", "name_six"]
sample_data_info = [("B", "integers", "i4"),
                    ("C", "float_integers", "f"),
                    ("D", "integer_floats", "i4"),
                    ("E", "floats", "f"),
                    ("F", "strings", "U"),
                    ("G", "dates", "M")]
sample_data_footer_rows = 1



customers_file_path = "data/test_data/TestKupci.xlsx"
vendors_file_path = "data/test_data/TestDobavljači.xlsx"



invoices_file_path = "data/test_data/TestInvoices.xls"
invoices_info = [("F", DataSettings.posting_date_invoices, "M"),
                ("G", DataSettings.posting_currency_invoices, "U"),
                ("D", DataSettings.open_amount_invoices, "f"),
                ("B", DataSettings.invoice_number_invoices, "U"),
                ("E", DataSettings.due_date_invoices, "M"),
                ("C", DataSettings.invoice_amount_invoices, "f"),
                ("A", DataSettings.customer_name_invoices, "U")]
invoices_footer_rows = 1
invoices_empty_cell_value = "nan"



IRA_EU_file_path = "data/test_data/TestIRA_EU.xlsx"
URA_EU_DC_file_path = "data/test_data/TestURA_EU_DC.xlsx"
URA_EU_DOM_file_path = "data/test_data/TestURA_EU_DOM.xlsx"
URA_EU_UVOZ_file_path = "data/test_data/TestURA_EU_UVOZ.xlsx"
