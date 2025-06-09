# Gmail Account Guide 📧

This project provides a complete manual and toolset to assist in the creation and tracking of multiple Gmail business accounts (e.g., 250 accounts). It includes:

- 📘 A step-by-step illustrated PDF guide to manually create Gmail accounts
- 📊 A sample Excel file to track created accounts
- 🐍 An optional Python script to auto-generate account lists

---

## 📘 Guide Contents

The PDF manual includes:

1. Preparing your account list
2. Navigating to the Gmail sign-up page
3. Filling out the registration form
4. Handling phone/recovery email options
5. Finishing account setup
6. Tracking progress using Excel
7. Tips to avoid verification blocks

---

## 📊 Sample Excel Format

| Account Number | Email Address         | Password    | Creation Date       | Status |
|----------------|-----------------------|-------------|----------------------|--------|
| Account 1      | business1@gmail.com   | Passw0rd1!  | 2025-06-09 00:00:00  | Active |
| ...            | ...                   | ...         | ...                  | ...    |

You can manually fill or generate the list using the Python script provided.

---

## 🐍 Python Script (Optional)

The script `generate_accounts.py` can generate a full list of 250 accounts with automatic dates and export them into an Excel file.

### 🔧 How to Use

```bash
python generate_accounts.py
