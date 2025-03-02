# Balance-calculator
Calculates the expected balance of your account after interests applied

# README

## Overview

This script reads an Excel file containing financial transactions and processes the data by:

- Extracting the first three columns (Date, Amount, Notes)
- Converting the Date column to datetime format
- Converting the Amount column to a numeric format
- Removing rows with missing Amount values
- Sorting transactions by date
- Setting an initial balance and a monthly interest rate

## Requirements

- Python 3.x
- pandas library
- An Excel file named `Kitap1.xlsx` with a sheet named `Sayfa1`

## Installation

1. Install the required Python library:
   ```sh
   pip install pandas openpyxl
   ```
2. Place the `Kitap1.xlsx` file in `C:\Users\Ahmet\Documents\`.

## Usage

Run the script using:

```sh
python script.py
```

Make sure the file path and sheet name match your actual Excel file.

---

# README (Türkçe)

## Genel Bakış

Bu script, finansal işlemleri içeren bir Excel dosyasını okuyarak:

- İlk üç sütunu (Tarih, Miktar, Açıklama) alır
- Tarih sütununu datetime formatına çevirir
- Miktar sütununu sayısal formata dönüştürür
- Eksik Miktar değerlerini içeren satırları siler
- İşlemleri tarihe göre sıralar
- Başlangıç bakiyesini ve aylık faiz oranını belirler

## Gereksinimler

- Python 3.x
- pandas kütüphanesi
- `Sayfa1` adlı sayfaya sahip `Kitap1.xlsx` adlı Excel dosyası

## Kurulum

1. Gerekli Python kütüphanesini yükleyin:
   ```sh
   pip install pandas openpyxl
   ```
2. `Kitap1.xlsx` dosyanızı `C:\Users\Ahmet\Documents\` dizinine yerleştirin.

## Kullanım

Scripti çalıştırmak için:

```sh
python script.py
```

Dosya yolu ve sayfa adının Excel dosyanız ile uyumlu olduğundan emin olun.

