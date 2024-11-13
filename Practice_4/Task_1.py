from datetime import datetime

date = (input("Please write the date in the format dd/mm/yyyy:"))
date_object = datetime.strptime(date, "%d/%m/%Y")
new_format = date_object.strftime("%Y-%m-%d")
print(new_format)
