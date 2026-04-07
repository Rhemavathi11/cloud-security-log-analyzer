# Cloud Security Log Analyzer

## 📌 Overview

This project is a Python-based log analyzer that monitors failed login attempts and detects suspicious IP addresses using timestamp filtering.

## 🚀 Features

* Reads logs from file
* Filters recent activity (last 5 minutes)
* Tracks failed login attempts per IP
* Detects suspicious IPs
* Generates report file

## 🛠️ Technologies Used

* Python

## 📊 Sample Output

Recent Failed Login Attempts:
192.168.1.2 : 3
192.168.1.3 : 1

🚨 Suspicious IPs (last 5 minutes):
192.168.1.2 → ALERT!

## 📂 Files

* log_analyzer.py
* logs.txt
* report.txt
