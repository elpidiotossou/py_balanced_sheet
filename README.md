## Balanced Sheet

A simple Python script to track income and expenditure, and generate a CSV balanced sheet.

### Features

* Add income and expenditure data to a SQLite database.
* Generate a CSV balanced sheet.

### Usage

1. Clone the repository and install the required dependencies:

`git clone https://github.com/username/balanced_sheet.git`
`pip install sqlite3 csv`


2. Run the script:

`python balanced_sheet.py`

The script will prompt you to enter your income or expenditure. You can also choose to generate a CSV balanced sheet.
The CSV balanced sheet will be saved in the balanced_sheet.csv file.

### Example
Enter your choice (I/E/G): I
Enter your income: 1000
Enter your choice (I/E/G): E
Enter your expenditure: 500
Enter your choice (I/E/G): G


This will generate a CSV balanced sheet with the following contents:

Date,Time,Income,Expenditure,Total Income,Total Expenditure,Grand Total
2023-09-20,20:16:06,1000,500,1000,500,500

Contributions
This project is open source and contributions are welcome. Please feel free to fork the repository and submit pull requests.

License
This project is licensed under the MIT License.

You can copy and paste this entire text block into a new file and save it as README.md in the root directory of your GitHub repository.
