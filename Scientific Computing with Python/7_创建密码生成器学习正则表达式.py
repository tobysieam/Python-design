import secrets
import string
import re  # 支持正则表达式操作

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # 这些参数用于后续实现约束密码的生成逻辑
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    # Generate password
    while True:
        # 这样可以在后续添加逻辑时，通过检查生成的密码是否符合约束条件来决定是否退出循环。
        password = ''
        for _ in range(length):
            password += secrets.choice(all_characters)
            return password
        # 添加新的约束元组，匹配单个小写字母、大写字母和特殊字符
        constraints = [
            (nums, r'\d'),           # 使用 \d 匹配单个数字
            (lowercase, r'[a-z]'),   # 匹配单个小写字母
            (uppercase, r'[A-Z]'),   # 匹配单个大写字母
            (special_chars, fr'[^{symbols}]')  # 使用 f-string 插入 symbols 变量
        ]

        # 使用 all() 函数检查所有约束是否满足
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            '''
            生成器表达式的优点：
            不会创建整个列表，而是逐个生成元素并进行评估。
            节省内存，尤其是在处理大型数据时。
            '''
            break  # 如果所有约束都满足，退出 while 循环

# 测试函数
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)  # 调用函数并打印生成的密码
    # 这是Python的惯用语法，用于确保代码仅在直接运行脚本时执行，而在模块被导入时不会执行。