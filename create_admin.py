import sqlite3
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'saga-backend.settings'

# 直接使用sqlite3连接数据库
conn = sqlite3.connect(r'd:\SAGA星光\saga-backend-main\db.sqlite3')
cursor = conn.cursor()

# 检查表结构
cursor.execute('PRAGMA table_info(auth_user)')
columns = cursor.fetchall()
print('auth_user columns:', [col[1] for col in columns])

# 检查是否有admin用户
cursor.execute("SELECT id, username FROM auth_user WHERE username='admin'")
existing = cursor.fetchone()
print('Existing admin:', existing)

if not existing:
    # 手动生成Django密码哈希
    import hashlib
    import base64
    import secrets
    
    # 生成salt
    salt = secrets.token_hex(16)
    # 计算密码哈希
    password = 'XX3pcLhHHNjr87x'
    iterations = 390000
    hash_value = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations)
    password_hash = f'pbkdf2_sha256${iterations}${salt}${base64.b64encode(hash_value).decode()}'
    
    print('Password hash:', password_hash)
    
    # 插入用户
    cursor.execute('''
        INSERT INTO auth_user 
        (password, last_login, is_superuser, username, first_name, last_name, email, 
         is_staff, is_active, date_joined)
        VALUES (?, NULL, 1, ?, '', '', ?, 1, 1, datetime('now'))
    ''', (password_hash, 'admin', 'admin@test.com'))
    conn.commit()
    print('User created successfully!')
else:
    # 更新密码
    import hashlib
    import base64
    import secrets
    
    salt = secrets.token_hex(16)
    password = 'XX3pcLhHHNjr87x'
    iterations = 390000
    hash_value = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations)
    password_hash = f'pbkdf2_sha256${iterations}${salt}${base64.b64encode(hash_value).decode()}'
    
    cursor.execute("UPDATE auth_user SET password = ? WHERE username = 'admin'", (password_hash,))
    conn.commit()
    print('Password reset successfully!')

# 验证
cursor.execute("SELECT id, username, is_superuser FROM auth_user WHERE username='admin'")
user = cursor.fetchone()
print('Verified user:', user)

conn.close()
print('\nLogin credentials:')
print('Username: admin')
print('Password: 123456')
