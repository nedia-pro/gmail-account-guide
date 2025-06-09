import pandas as pd
from datetime import datetime, timedelta

def generate_gmail_accounts(num_accounts=250, start_date="2025-06-09"):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    data = {
        "Account Number": [],
        "Email Address": [],
        "Password": [],
        "Creation Date": [],
        "Status": []
    }

    for i in range(num_accounts):
        acc_num = f"Account {i+1}"
        email = f"business{i+1}@gmail.com"
        password = f"Passw0rd{i+1}!"
        creation_date = (start + timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
        status = "Active"

        data["Account Number"].append(acc_num)
        data["Email Address"].append(email)
        data["Password"].append(password)
        data["Creation Date"].append(creation_date)
        data["Status"].append(status)

    df = pd.DataFrame(data)
    df.to_excel("Gmail_Accounts_250.xlsx", index=False)
    print("Excel file 'Gmail_Accounts_250.xlsx' generated successfully.")

if __name__ == "__main__":
    generate_gmail_accounts()
