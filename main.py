import datetime
import sqlite3
import csv

# Create a SQLite database to store the income and expenditure data.
conn = sqlite3.connect('balanced_sheet.db')

# Create a cursor object to execute SQL statements.
c = conn.cursor()

# Create a table to store the income and expenditure data.
c.execute('CREATE TABLE IF NOT EXISTS balanced_sheet (income TEXT, expenditure TEXT, date TEXT, time TEXT)')

# Define a function to add income to the database.
def add_income():
    income = input('Enter your income: ')
    date, time = datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%H:%M:%S')

    c.execute('INSERT INTO balanced_sheet (income, expenditure, date, time) VALUES (?, ?, ?, ?)', (income, 0, date, time))
    conn.commit()

# Define a function to add expenditure to the database.
def add_expenditure():
    expenditure = input('Enter your expenditure: ')
    date, time = datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%H:%M:%S')

    c.execute('INSERT INTO balanced_sheet (income, expenditure, date, time) VALUES (?, ?, ?, ?)', (0, expenditure, date, time))
    conn.commit()

# Define a function to generate a CSV balanced sheet.
def generate_csv_balanced_sheet():
    writer = csv.writer(open('balanced_sheet.csv', 'w'))

    writer.writerow(['Date', 'Time', 'Income', 'Expenditure', 'Total Income', 'Total Expenditure', 'Grand Total'])

    c.execute('SELECT date, time, income, expenditure FROM balanced_sheet')

    total_income = 0
    total_expenditure = 0
    for row in c.fetchall():
        total_income += float(row[2])
        total_expenditure += float(row[3])

        writer.writerow([row[0], row[1], row[2], row[3], '', '', ''])

    grand_total = total_income - total_expenditure

    writer.writerow(['', '', total_income, total_expenditure, '', '', grand_total])

# Get the user's choice.
choice = input('Enter your choice (I/E/G): ')

# If the user chooses to input income, call the add_income function.
if choice == 'I':
    add_income()

# If the user chooses to input expenditure, call the add_expenditure function.
elif choice == 'E':
    add_expenditure()

# If the user chooses to generate the CSV balanced sheet, call the generate_csv_balanced_sheet function.
elif choice == 'G':
    generate_csv_balanced_sheet()

# Close the database connection.
conn.close()
