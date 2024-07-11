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

登录页面:  账号：202201  密码：123456，后续页面增加路由保护功能，以下为登录页面演示：
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/login.gif)

在主菜单栏点击查询图书信息，选择查询方式（书名，ISBN，作者，类别），并且输入查询内容，进行模糊搜索，渲染表格显示搜索结果；若无查询结果，则提示无结果：
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/searchbook.gif)

在主菜单栏点击查询学生信息，输入学生借阅卡号码，进行查询，显示学生基本信息，并且渲染表格显示该学生的借阅记录：
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/searchstudent.gif)

在主菜单栏点击图书管理，展开二级菜单，点击新书入库，新书入库功能又分为两个子功能，如果采购的书之前图书馆没有，则先点击“新书登记”填写新书的信息，在对该书进行编号，在库存补充子功能里填写图书编号、位置等信息：
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/newbook.gif)

点击图书管理下的“学生借书”，输入要借书的学生借阅卡号码，提供按书名查找、显示可借的图书列表，点击搜索，渲染表格，选中某一行进行借出操作，确认后，表格进行重载，可连续进行借出操作（如果该借阅卡欠费、到期或者已挂失，会给出相应提示信息）：
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/borrow.gif)

点击图书管理下的“学生还书”，输入要还书的学生借阅卡号码，点击，显示该学生未还的图书列表，选中某一行进行归还操作，确认后，表格重载，可连续进行归还操作：
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/return.gif)

在侧边主菜单点击信息设置，可修改现在登录的管理员的信息，在顶端导航栏，光标移到管理员姓名或头像上，选择查看个人信息或者修改密码：
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/changepw.gif)

# 普通用户功能使用说明
在登录页面顶端导航栏上选择，查询图书信息或者查询学生信息，页面及使用与管理员功能说明一致：
![image](https://github.com/tony8888lrz/SWU-BMS/blob/main/gif/common.gif)
