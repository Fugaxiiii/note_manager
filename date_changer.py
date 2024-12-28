from datetime import datetime

created_date = "26-12-24 14:30:00"
issue_date = "26-01-25 09:15:00"

created_date_obj = datetime.strptime(created_date, "%d-%m-%y %H:%M:%S")
issue_date_obj = datetime.strptime(issue_date, "%d-%m-%y %H:%M:%S")

temp_created_date = created_date_obj.strftime("%d-%m")
temp_issue_date = issue_date_obj.strftime("%d-%m")

print(f"created_date: {temp_created_date}")
print(f"issue_date: {temp_issue_date}")