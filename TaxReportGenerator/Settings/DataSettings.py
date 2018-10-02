thousands = "."



customers_file_path = "data/real_data/KUPCI.xlsx"
customers = "customers"
customers_skip_footer = 0

name_customers = "Naziv"
state_customers = "Država/regija"
tax_number_customers = "Porezni broj"
customers_columns = [("B", name_customers, "U"),
                     ("D", state_customers, "U"),
                     ("G", tax_number_customers, "U"),
                    ]

                    
                    
vendors_file_path = "data/real_data/DOBAVLJAČI.xlsx"
vendors = "vendors"
vendors_skip_footer = 0

state_vendors = "Država/regija"
tax_number_vendors = "Porezni broj"
vendors_columns = [("D", state_vendors, "U"),
                   ("G", tax_number_vendors, "U"),
                  ]



invoices_file_path = "data/real_data/Invoices.xls"
invoices = "invoices"
invoices_skip_footer = 1

posting_date_invoices = "Posting date"
posting_currency_invoices = "Posting Currency"
open_amount_invoices = "Open Amount Company Curr"
invoice_number_invoices = "Invoice Nr"
due_date_invoices = "Due Date"
invoice_amount_invoices = "Invoice Amount Company Curr"
customer_name_invoices = "Customer Name"
invoices_columns = [("W", posting_date_invoices, "M"),
                    ("N", posting_currency_invoices, "U"),
                    ("Q", open_amount_invoices, "f"),
                    ("I", invoice_number_invoices, "U"),
                    ("V", due_date_invoices, "M"),
                    ("O", invoice_amount_invoices, "f"),
                    ("C", customer_name_invoices, "U"),
                   ]

                   

IRA_EU_file_path = "data/real_data/IRA_EU.xlsx"
IRA_EU = "IRA_EU"
IRA_EU_skip_footer = 1

customer_id_IRA_EU = "Kupac - OIB/PDV ID"
goods_sold_IRA_EU = "Isporuke dobara unutar EU"
services_sold_IRA_EU = "Obavljene usluge unutar EU"
exports_IRA_EU = "Izvozne isporuke"
taxable_base_IRA_EU = "Oporezivo 25% - osnovica"
taxable_tax_IRA_EU = "Oporezivo 25% - porez"
IRA_EU_columns = [("V", taxable_tax_IRA_EU, "f"),
                  ("O", exports_IRA_EU, "f"),
                  ("I", goods_sold_IRA_EU, "f"),
                  ("U", taxable_base_IRA_EU, "f"),
                  ("J", services_sold_IRA_EU, "f"),
                  ("E", customer_id_IRA_EU, "U"),
                 ]

                 
                 
URA_EU_DC_file_path = "data/real_data/URA_EU_DC.xlsx"
URA_EU_DC = "URA_EU_DC"
URA_EU_DC_skip_footer = 1

vendors_id_URA_EU_DC = "Dobavljač - OIB"
tax_base_URA_EU_DC = "Porezna osnovica 25%"
total_URA_EU_DC = "Ukupno"
URA_EU_DC_columns = [("E", vendors_id_URA_EU_DC, "U"),
                     ("H", tax_base_URA_EU_DC, "f"),
                     ("J", total_URA_EU_DC, "f"),
                    ]

                    

URA_EU_DOM_file_path = "data/real_data/URA_EU_DOM.xlsx"
URA_EU_DOM = "URA_EU_DOM"
URA_EU_DOM_skip_footer = 1

refundable_URA_EU_DOM = "Pretporez 25% - može se odbiti"
URA_EU_DOM_columns = [("O", refundable_URA_EU_DOM, "f"),
                     ]
                    


URA_EU_UVOZ_file_path = "data/real_data/URA_EU_UVOZ.xlsx"
URA_EU_UVOZ = "URA_EU_UVOZ"
URA_EU_UVOZ_skip_footer = 1
                                  
total_URA_EU_UVOZ = "Ukupno"
URA_EU_UVOZ_columns = [("J", total_URA_EU_UVOZ, "f"),
                      ]
