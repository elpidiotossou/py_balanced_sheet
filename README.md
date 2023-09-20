This is a simple Python script to track income and expenditure, and generate a CSV balanced sheet.

To use the script, clone the repository and install the required dependencies:

pip install sqlite3 csv


Then, run the script:

python balanced_sheet.py

The script will prompt you to enter your income or expenditure. You can also choose to generate a CSV balanced sheet.

The CSV balanced sheet will be saved in the balanced_sheet.csv file.

Features:

Add income and expenditure data to a SQLite database.
Generate a CSV balanced sheet.
Usage:

python balanced_sheet.py


**Example:**

Enter your choice (I/E/G): I
Enter your income: 1000
Enter your choice (I/E/G): E
Enter your expenditure: 500
Enter your choice (I/E/G): G


This will generate a CSV balanced sheet with the following contents:

Date,Time,Income,Expenditure,Total Income,Total Expenditure,Grand Total
2023-09-20,20:16:06,1000,500,1000,500,500

Contributions:

This project is open source and contributions are welcome. Please feel free to fork the repository and submit pull requests.

This is just a suggestion, of course. You can customize the repo name, description, and README to your liking.
