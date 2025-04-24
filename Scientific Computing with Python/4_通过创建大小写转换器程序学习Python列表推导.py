from numpy import char


def convert_case(pascal_or_camel_cased_string):
    # 核心知识点：待条件分支的列表推导式
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()   # 条件表达式在前
        else char
        for char in pascal_or_camel_cased_string  # 遍历原始字符串
    ]

    # 知识点：字符串拼接与修正
    return ''.join(snake_cased_char_list).strip('_')  # 合并列表为字符串，去除首尾多余下划线

def main():
    # 知识点：入口函数模式
    print(convert_case('aLongAndComplexString'))  # 预期输出：a_long_and_complex_string


'''
1、列表推导式结构
[表达式 if 条件 else 默认值 for 迭代变量 in 可迭代对象]
与普通循环等效：

result = []
for char in s:
    if char.isupper():
        result.append('_' + char.lower())
    else:
        result.append(char)


2、条件表达式顺序
条件判断必须放在表达式前面，这与常规的if过滤（放在末尾）不同。例如：

# 过滤式（仅保留大写字符）
[c for c in s if c.isupper()]  
# 条件分支式（处理不同情况）
[f(c) if cond else g(c) for c in s]


3、字符串处理方法

.lower()：字母转小写（仅对字母有效）
''.join()：高效连接字符列表（时间复杂度O(n)）
.strip('_')：移除首尾指定字符（处理首字母大写的情况，如MyVar→_my_var→my_var）


4、命名转换逻辑

遇到大写字母时添加下划线前缀（如Long→_long）
最终字符串会包含连续下划线（如ABTest→_a_b_test）
使用strip('_')确保不会出现开头下划线（如_a_b_test→a_b_test）


5、函数设计模式

独立转换函数：提高代码复用性（可被其他模块调用）
main入口函数：符合Python最佳实践（便于单元测试/模块化）
'''


'''
1、遍历每个字符：
['a', 'L', 'o', 'n', 'g', 'A', 'n', 'd', ...]


2、转换处理：
['a', '_l', 'o', 'n', 'g', '_a', 'n', 'd', ...]


3、拼接结果：
'a_lon_g_a_nd...'


4、去除首尾_：
'a_long_and_complex_string'
'''