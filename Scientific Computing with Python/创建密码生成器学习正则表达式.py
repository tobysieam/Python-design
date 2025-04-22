import string
import secrets
letters = string.ascii_letters
'''
`string.ascii_letters` 是 Python 的 `string` 模块中的一个常量，它包含所有的英文字母，包括小写字母和大写字母。具体来说，它等价于：
string.ascii_letters == string.ascii_lowercase + string.ascii_uppercase
它的值是一个字符串，内容为：
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
也就是说，`string.ascii_letters` 包含了从 `a` 到 `z` 的所有小写字母，以及从 `A` 到 `Z` 的所有大写字母。它通常用于需要处理所有英文字母的场景，例如生成随机字符串或验证输入是否为字母。
'''
digits = string.digits
symbols = string.punctuation
# Combine all characters
all_characters = letters + digits + symbols
print(all_characters)