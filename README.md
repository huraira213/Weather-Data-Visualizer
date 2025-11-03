#  Weather Data Visualizer

A **Python-based CLI application** that reads, cleans, analyzes, and visualizes weather data from CSV files.  
It generates insightful reports, calculates weather statistics, and plots visual trends using `matplotlib`.

---

##  Project Overview

The **Weather Data Visualizer** is designed to help you understand how to turn **raw CSV data into insights and visuals**.

It demonstrates:
- Clean code structure and modular design
- Data parsing, processing, and summarization
- CLI-based interaction with report generation
- Data visualization using **matplotlib**

---

##  Project Structure


```
Weather-Data-Visualizer/
│
├── main.py
├── core/
│   ├── reader.py          → handles all file reading
│   ├── processor.py       → cleans and normalizes raw data
│   ├── analyzer.py        → performs calculations and summaries
│   ├── visualizer.py      → generates plots using matplotlib
│   └── report.py          → generates reports (text, json, chart)
│
├── ui/
│   └── cli.py             → handles user interaction
│
├── utils/
│   ├── paths.py           → manages directories and constants
│   └── io_utils.py        → file helpers, logging
│
├── data/
│   ├── input/
│   │   ├── sample.csv
│   │   └── sample2.csv 
│   └── output/
│       ├── report.txt
│       ├── summary.json 
│       ├── humidity_trend.png 
│       ├── rainfall_pattern.png 
│       └── temperature_trend.png
│
└── README.md
         
```


---

##  Features

**CSV Reader** — Loads weather data from CSV files  
 **Data Processor** — Cleans and normalizes raw data  
 **Analyzer** — Calculates:
- Average temperature & humidity  
- Total rainfall  
- Hottest & coldest days  

 **Report Generator** — Exports analysis as:
- Text report (`report.txt`)
- JSON summary (`summary.json`)

 **Visualizer** — Plots:
- ️ Temperature trend  
-  Humidity trend  
-  Rainfall pattern  

 **CLI Menu System** — Easy-to-use terminal interface for interaction  

---

##  Setup Instructions

### 1️ Clone the repository
```bash
  git clone https://github.com/yourusername/Weather-Data-Visualizer.git
  cd Weather-Data-Visualizer
```

### 2 Create a virtual environment (recommended)
```bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows
```

### 3 Install dependencies
``` bash
    pip install matplotlib

```
---
### 4 Usage Guide
Run the CLI
```
python main.py
```

Example Menu
```
-- Weather Data Visualizer --
==============================
1. Read CSV
2. Analyze Data
3. Generate Report
4. Exit
------------------------------
```
---

### Key Learnings

* How to structure a modular Python project
* How to parse and clean CSV data
* How to design CLI-based data tools
* Basics of data visualization with matplotlib
* Writing clean, maintainable code with separation of concerns

---

##  Author

**Huraira Khurshid**
 Python Developer & Intern at SKAI Worldwide
 Completed: November 2025
 Goal: Building clean, modular, and maintainable Python software.

---

##  License

This project is licensed under the MIT License — feel free to use and modify it.