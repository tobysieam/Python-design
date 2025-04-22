import secrets
import string
import re #支持正则表达式操作

def generate_password(length, nums, special_chars, uppercase, lowercase):
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
        constraints = [(nums,'')]  #为后续实现密码约束逻辑提供了基础
    


# new_password = generate_password(8)
# print(new_password)
pattern = re.compile('l+')  
# 1. 将正则表达式模式从 `'l'` 修改为 `'l+'`，以匹配一个或多个连续的字符 `'l'`。
# 2. `pattern.search(quote)` 将返回第一个匹配的结果，如果字符串中有连续的 `'l'`，它会匹配整个连续的部分。
quote = 'Not all those who wander are lost.'
print(pattern.search(quote))

