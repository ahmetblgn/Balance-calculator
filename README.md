# Balance-calculator
Calculates the expected balance of your account after interests applied

README

Overview

This script reads an Excel file containing financial transactions and processes the data by:

Extracting the first three columns (Date, Amount, Notes)

Converting the Date column to datetime format

Converting the Amount column to a numeric format

Removing rows with missing Amount values

Sorting transactions by date

Setting an initial balance and a monthly interest rate

Requirements

Python 3.x

pandas library

An Excel file named Kitap1.xlsx with a sheet named Sayfa1

Installation

Install the required Python library:

pip install pandas openpyxl

Place the Kitap1.xlsx file in C:\Users\Ahmet\Documents\.

Usage

Run the script using:

python script.py

Make sure the file path and sheet name match your actual Excel file.
