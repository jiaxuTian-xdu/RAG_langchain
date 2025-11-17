import pymysql
from pymysql.cursors import DictCursor
# --- 数据库连接配置 ---
# 强烈建议将以下敏感信息存储在环境变量或配置文件中
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "123456789",  
    "database": "knowledge_base", # 数据库名称
    "charset": "utf8mb4"
}
 
def get_db_connection():
    """创建并返回一个数据库连接"""
    return pymysql.Connect(**DB_CONFIG)
# --- 部门表操作 ---
 
def department_exists(department_name: str) -> bool:
    """检查部门是否已存在"""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            sql = "SELECT id FROM departments WHERE name = %s"
            cursor.execute(sql, (department_name,))
            return cursor.fetchone() is not None
 
def create_department(department_name: str):
    """创建一个新部门"""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            sql = "INSERT INTO departments (name) VALUES (%s)"
            cursor.execute(sql, (department_name,))
            conn.commit()
 
def get_or_create_department(department_name: str) -> int:
    """获取部门ID，如果部门不存在则自动创建并返回新ID"""
    if not department_exists(department_name):
        create_department(department_name)
    
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            sql = "SELECT id FROM departments WHERE name = %s"
            cursor.execute(sql, (department_name,))
            result = cursor.fetchone()
            return result[0] if result else None
# --- 文档表操作 ---
 
def insert_department_doc(filename: str, department_name: str) -> int:
    """在部门文档表中插入一条记录，并返回新记录的ID"""
    department_id = get_or_create_department(department_name)
    
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            sql = "INSERT INTO department_docs (filename, department_id) VALUES (%s, %s)"
            cursor.execute(sql, (filename, department_id))
            conn.commit()
            return cursor.lastrowid
 
def insert_file_master(filename: str, file_type: str,department: str) -> int:
    """在文件总表中插入一条记录，并返回新记录的ID"""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            sql = "INSERT INTO file_master (filename, file_type,department) VALUES (%s, %s, %s)"
            cursor.execute(sql, (filename, file_type,department))
            conn.commit()
            return cursor.lastrowid
        
# --- 表结构初始化 ---
# (此函数只需要在第一次部署时运行一次)
def initialize_database():
    """初始化数据库和表结构"""
    print("正在初始化数据库...")
    
    # 1. 创建数据库 (如果不存在)
    db_name = DB_CONFIG['database']
    conn = pymysql.Connect(host=DB_CONFIG['host'], user=DB_CONFIG['user'], password=DB_CONFIG['password'])
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        conn.commit()
        print(f"数据库 '{db_name}' 已确保存在。")
    finally:
        conn.close()
    
    # 2. 创建表 (使用新创建的数据库连接)
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            # 部门表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS `departments` (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `name` VARCHAR(100) NOT NULL UNIQUE,
                    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            
            # 文件总表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS `file_master` (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `filename` VARCHAR(255) NOT NULL,
                    `file_type` VARCHAR(50) NOT NULL,
                    `department` VARCHAR(50) NOT NULL,
                    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
 
            # 部门文档表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS `department_docs` (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `filename` VARCHAR(255) NOT NULL,
                    `department_id` INT NOT NULL,
                    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (`department_id`) REFERENCES `departments`(`id`) ON DELETE CASCADE
                );
            """)
            
            conn.commit()
            print("数据库表结构初始化完成。")
# --- 使用示例 ---
if __name__ == "__main__":
    # 运行此文件来初始化数据库和表
    # 在部署前，请确保 DB_CONFIG 中的信息正确无误
    initialize_database()