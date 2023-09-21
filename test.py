import mysql.connector

def main():
    # 建立連接 (修改)
    connection = mysql.connector.connect(
        host="fortune.ckgadenebkdr.ap-northeast-3.rds.amazonaws.com",
        port="3306",  # MySQL 的默認端口
        database="members",
        user="admin",
        password="Aa123456"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT member_name FROM member")
    existing_user = cursor.fetchall()
    print(existing_user)

    # 確保在使用後關閉連接
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
