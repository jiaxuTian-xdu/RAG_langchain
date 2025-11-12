import mysql.connector
from mysql.connector import Error


def create_database():
    """创建数据库和表"""
    try:
        # 第一步：连接到MySQL服务器（不指定数据库）
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # 默认root用户
            password='123456789'  # 你安装时设置的root密码
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # 创建数据库
            cursor.execute("CREATE DATABASE IF NOT EXISTS school")
            print("数据库创建成功!")

            # 切换到新数据库
            cursor.execute("USE school")

            # 创建学生表
            create_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(50) NOT NULL,
                age INT,
                class VARCHAR(20),
                score DECIMAL(4,2),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_table_query)
            print("学生表创建成功!")

            # 插入示例数据
            insert_queries = [
                "INSERT INTO students (name, age, class, score) VALUES ('张三', 18, '一班', 85.5)",
                "INSERT INTO students (name, age, class, score) VALUES ('李四', 19, '二班', 92.0)",
                "INSERT INTO students (name, age, class, score) VALUES ('王五', 17, '一班', 78.5)",
                "INSERT INTO students (name, age, class, score) VALUES ('赵六', 18, '三班', 88.0)"
            ]

            for query in insert_queries:
                cursor.execute(query)

            connection.commit()
            print("示例数据插入成功!")

    except Error as e:
        print(f"错误: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL连接已关闭")


def test_connection():
    """测试数据库连接和查询"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456789',
            database='school'
        )

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()

        print("\n学生数据:")
        print("ID | 姓名 | 年龄 | 班级 | 分数")
        print("-" * 30)
        for row in results:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

    except Error as e:
        print(f"连接测试失败: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def add_some_new():
    return None


if __name__ == "__main__":
    # 创建数据库和表
    create_database()

    # 测试连接和查询
    test_connection()
