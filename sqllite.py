# 테이블 생성 및 삽입
import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print("now :", now)
#now_date_time = now.strftime("%Y-%m-%d")
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("now date time", now_date_time)

# sqllite3
print("sqllite3.version :", sqlite3.version)
print("sqllite3.sqlite_version", sqlite3.sqlite_version)

# DB 생성 & Auto Commit
# Auto Commit은 그때그때 바로 Commit을 한다는 의미임
# Auto Commit : isolation_level= None
conn = sqlite3.connect("C:/Users/onycom/PycharmProjects/dataBusiness/crawling_practice/db/database.db", isolation_level= None)

# Cursor 커서가 이동해서 다음부터 데이터를 가지고 옮
c = conn.cursor()

print("Cursor Type : ", type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
# 테이블이 없으면 만듦
#c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
#c.execute("INSERT INTO users VALUES(4, 'kim', 'kim@gmail.com', '010-0000-0000', 'www.naver.com', ?)", [now_date_time])
#c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", [5, "Lee", "lee@gmail.com", "010-1234-5678", "www.naver.com", now_date_time])

# Many 삽입(튜플, 리스트)
"""user_list = [[6, "Lee", "lee@gmail.com", "010-1234-5678", "lee.com", now_date_time],
             [7, "Park", "park@gmail.com", "010-3456-5678", "park.com", now_date_time],
             [8, "Kim", "kim@gmail.com", "010-2345-5678", "kim.com", now_date_time]]
"""

#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", user_list)

# 테이블 데이터 삭제
#conn.execute("DELETE FROM users")
#print("user db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isloation_level = None 일 경우 자동 반영(오토 커밋)
#conn.commit()

# 롤백
#conn.rollback()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
#print("One -> \n", c.fetchone())

# 지정 로우 선택
#print("Three -> \n", c.fetchmany(size=3))

# 전체 로우 선택
#print("All -> \n", c.fetchall())

# 순회1
rows = c.fetchall()
"""for row in rows:
    print("retrieve1 >", row)
"""

# 순회2
"""for row in rows:
    print("retrieve2 >", row)
"""

# 순회3
"""for row in c.execute("SELECT * FROM users ORDER BY id asc"):
    print("retrieve3 >", row)
"""

# 데이터 수정 1
#c.execute("UPDATE users SET username = ? WHERE id =?", ("HO", 6))

# 데이터 수정 2
#c.execute("UPDATE users SET username = :name WHERE id = :id", {"name" : "goodman", "id" : 6})

# 데이터 수정 3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'"%("badboy", 7))

# 테이블 전체 삭제
print("users db deleted :", conn.execute("DELETE FROM users").rowcount, " rows")

# Row Delete1
#c.execute("DELETE FROM users WHERE id = ?", (6,))
conn.commit()

# WHERE Retrieve1
param1 = (6,)
c.execute("SELECT * FROM users WHERE id=?", param1)
print("param1", c.fetchone())
print("param1", c.fetchall())

# 접속 해제
conn.close()

