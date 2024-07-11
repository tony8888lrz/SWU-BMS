## Introduction
This Python-based university library management system integrates a SQLite database (back-end) with a LayUI web interface (front-end). The database design strictly follows third normal form (3NF) principles to ensure data normalization and minimize redundancy (refer to data.sqlite for the schema).
## Prerequisites
Before running, please ensure the following requirements are met:
- Conda (Python 3.9)
- Other packages are listed in requirements.txt.
## Usage
### Reproduce the system
1. Create a new conda environment:
```{py}
  conda create --name bms python=3.9
  activate bms       # Windows
  conda activate bms # Linux
```
2. Clone this repo:
```
git clone [https://github.com/tony8888lrz/SWU-BMS](https://github.com/tony8888lrz/SWU-BMS/)
cd SWU-BMS
```
3. Install required packages by typing
```
pip install -r requirements.txt
```
It is a university library management system developed with python. It combines a back-end database（Python with Sqlite) and a front-end web interface(LayUI).
I literally define the database(in 3rd normal form) for the entire management system(Seeing the file data.sqlite）
## Test
You can work with the test, which will help you run smoothly with this software.

## demo
![Example Image](Picture1.png)
