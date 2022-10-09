import pymysql

db = pymysql.connect(host='localhost',
                     user='8888',
                     password='111111',
                     database='bookmanage') #连接我的数据库
 
cursor = db.cursor()

#执行query
book = cursor.execute("SELECT ISBN, book_name, author, press, class_name FROM book")
student = cursor.execute("SELECT student_name, sex, valid_date, dept, barcode, book_name, in_date, out_date FROM book, student, inventory")

#赋值到变量中更好对数据操作
admin_id = db.Column(db.String(6), primary_key=True)
admin_name = db.Column(db.String(32))
password = db.Column(db.String(24))
right = db.Column(db.String(32))

barcode = db.Column(db.String(6), primary_key=True)
isbn = db.Column(db.ForeignKey('book.isbn'))
storage_date = db.Column(db.String(13))
location = db.Column(db.String(32))
withdraw = db.Column(db.Boolean, default=False)  # 是否注销
status = db.Column(db.Boolean, default=True)  # 是否在馆
admin = db.Column(db.ForeignKey('admin.admin_id'))  # 入库操作员

card_id = db.Column(db.ForeignKey('student.card_id'), index=True)
start_date = db.Column(db.String(13))
borrow_admin = db.Column(db.ForeignKey('admin.admin_id'))  # 借书操作员
end_date = db.Column(db.String(13), nullable=True)
return_admin = db.Column(db.ForeignKey('admin.admin_id'))  # 还书操作员
due_date = db.Column(db.String(13))  # 应还日

db.close()