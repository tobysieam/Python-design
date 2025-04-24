def verify_card_number(card_number):
    # 知识点1：字符串逆序（用于从右向左处理）
    # card_number[::-1] 通过切片步长-1实现字符串反转
    card_number_reversed = card_number[::-1]

    # 知识点2：字符串切片获取奇偶位
    # [::2] 从索引0开始，步长2取字符（逆序后的奇数位）
    odd_digits = card_number_reversed[::2]  # 原卡号倒数第1、3、5...位
    # [1::2] 从索引1开始，步长2取字符（逆序后的偶数位）
    even_digits = card_number_reversed[1::2]  # 原卡号倒数第2、4、6...位

    sum_of_odd_digits = 0
    for digit in odd_digits:
        # 知识点3：字符转数字处理
        sum_of_odd_digits += int(digit)  # 直接累加奇位数


    sum_of_even_digits = 0
    for digit in even_digits:
        # 知识点4：偶数位处理规则
        number = int(digit) * 2 # 卢恩算法要求偶位数乘2
        if number >= 10:
            # 知识点5：两位数拆分求和（例如14→1+4=5）
            number = (number // 10) + (number % 10)  # 地板除与取模结合
            sum_of_even_digits += number

    # 知识点6：模10校验核心逻辑
    total = sum_of_even_digits + sum_of_odd_digits
    return total % 10 == 0 # 返回布尔值判断有效性


def main():
    # 测试卡号（含格式符号）
    card_number = '4111-1111-4555-1141'  # 有效Visa卡号

    # 知识点7：字符串清理与翻译
    # 创建字符映射表（删除连字符和空格）
    card_translation = str.maketrans({'-': '', ' ': ''})  # 创建替换规则字典
    # 应用字符翻译清理输入
    translated_card_number = card_number.translate(card_translation)

    # 知识点8：逻辑流程控制
    if verify_card_number(translated_card_number):
        print('VALID!')  # 通过校验
    else:
        print('INVALID!')  # 未通过校验


# 知识点9：主程序入口
if __name__ == '__main__':
    main()  # 执行测试用例


'''
关键知识点详解
1、字符串逆序处理
card_number[::-1] 通过切片实现字符串反转，满足算法从右向左处理的要求
示例："1234" → "4321"

2、奇偶位分离技巧

[::2] 获取逆序后的奇数位（原卡号右起第1、3、5...位）
[1::2] 获取逆序后的偶数位（原卡号右起第2、4、6...位）
字符转数字处理
int(digit) 将字符串数字转为整型，进行数学运算

3、偶位数特殊处理

乘2规则：所有偶位数进行 ×2 处理
示例：偶位数5 → 5×2=10 → 1+0=1
两位数拆分算法
(number // 10) + (number % 10) 分解十位和个位相加
数学原理：对任意两位数n，有 n = 10a + b → a + b

4、模10校验机制
total % 10 == 0 是卢恩算法的核心验证条件

5、输入数据清洗
str.maketrans() 和 translate() 组合使用，高效清除无效字符

6、主程序逻辑流程
典型的 if-else 条件判断结构，控制程序输出
'''

'''
卢恩算法（Luhn Algorithm）
卢恩算法，也称为“模 10 算法”，是一种简单的校验和算法，主要用于验证身份识别码，如银行卡号、信用卡号、国际移动设备辨识码（IMEI）、美国国家提供商标识号码、加拿大社会保险号码等。

算法步骤
1、初始化：从右到左（不包括最后一位校验位）对偶数位置的数字进行翻倍，如果翻倍后的数字超过 9，则将这两个数字相加（例如，5 * 2 = 10，取 1 + 0 = 1）。
2、奇数位置：保留原样。
3、总和计算：从右到左，将所有位置上的数字相加（包括最后一位校验位）。
4、校验位计算：如果总和除以 10 的余数为 0，则原始数字（不含校验位）满足卢恩算法，即为有效。如果余数不为 0，可以将 10 减去余数作为缺失的校验位，使得新总和能被 10 整除。
'''
