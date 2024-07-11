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
4. Run book_management_sys.py to reproduce the management system.
```
python book_management_sys.py runserver
```
5. Go to http://127.0.0.1:5000/ or enter the localhost in the browser

## Demo
You can work with the test, which will help you run smoothly with this software.
Login Page:  Account：202201  Password：123456，Subsequent pages will include route protection functionality. Below is a demonstration of the login page:
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/Picture1.png)

In the main menu bar, click on "Query Book Information," select the query method (Title, ISBN, Author, Category), and enter the search content for a fuzzy search. The results will be displayed in a table. If no results are found, a no results message will be displayed:
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/searchbook.gif)

In the main menu bar, click on "Query Student Information," enter the student's library card number, and the basic information of the student along with their borrowing records will be displayed in a table:
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/searchstudent.gif)

In the main menu bar, click on "Book Management" to expand the secondary menu, then click "New Book Entry." This function is divided into two sub-functions. If the purchased book is not already in the library, first click "New Book Registration" to fill in the book's information, then assign a number to the book. In the "Stock Replenishment" sub-function, fill in the book's number, location, etc.:
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/newbook.gif)

Under "Book Management," click "Student Borrowing." Enter the student's library card number, search for books by title, display the list of available books, and click search. The results will be rendered in a table. Select a row to perform the borrowing operation. After confirmation, the table will reload, allowing continuous borrowing operations. (If the card has overdue fees, is expired, or reported lost, an appropriate message will be displayed):
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/borrow.gif)

Click on "Information Settings" in the side main menu to modify the currently logged-in administrator's information. In the top navigation bar, hover over the administrator's name or avatar to select "View Personal Information" or "Change Password":
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/return.gif)

In the top navigation bar of the login page, select "Query Book Information" or "Query Student Information." The pages and usage are the same as those for administrators:
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/changepw.gif)

