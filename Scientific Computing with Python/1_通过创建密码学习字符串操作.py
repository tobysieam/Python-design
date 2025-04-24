# ======================
# Vigenère Cipher 实现
# =核心知识点：字符串操作、循环控制、模运算、函数封装
# ======================

def vigenere_cipher(message, key, mode = 'encrypt'):
    """
    Vigenère密码核心算法
    :param message: 要加密/解密的字符串
    :param key: 密钥字符串
    :param mode: 模式：'encrypt' 或 'decrypt'
    :return: 处理后的字符串
    """
    #知识点1：字符串预处理
    key = key.lower() #统一密钥为小写
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 字母表定义
    processed = []  #使用列表保存结果
    key_index = 0  #密钥字符索引

    # 知识点2：方向系数计算（加密+1，解密-1）
    direction = 1 if mode == 'encrypt' else -1

    # 知识点3：遍历字符串中的每个字符
    for char in message.lower():
        if not char.isalpha():
            # Python isalpha() 方法检测字符串是否只由字母组成。
            # 知识点4：非字母字符直接保留
            processed.append(char)  # append() 方法用于在列表末尾添加新的对象。该方法无返回值，但是会修改原来的列表。
            continue

        # 知识点5：密钥字符循环获取（使用模运算实现循环）
        key_char = key[key_index % len(key)]  # key_index % len(key)：通过模运算实现密钥循环复用 示例：密钥长度5时，索引0→1→2→3→4→0→1→...
        key_index += 1

        # 知识点6：字符偏移量计算
        char_pos = alphabet.index(char)  # 原始字符位置（已过滤非字母字符，可以直接用index),index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
        # index()方法：精确查找字符位置（比find()更严格）
        key_pos = alphabet.index(key_char)  #  密钥字符位置
        new_pos = (char_pos + direction * key_pos) % 26  # 模26保证不越界
        #         模26运算：保证计算结果在字母表范围内（0 - 25）
        #         数学公式：加密时(char_pos + key_pos) mod 26，解密时(char_pos - key_pos) mod 26

        processed.append(alphabet[new_pos])
    # 知识点7：列表转字符串的高效转换
    return ''.join(processed)  # Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    ##!/usr/bin/python
    # -*- coding: UTF-8 -*-

    # symbol = "-";
    # seq = ("a", "b", "c"); # 字符串序列
    # print symbol.join( seq );
# 结果为a-b-c


def encrypt(plaintext,key):
    '''加密函数'''
    return vigenere_cipher(plaintext, key, 'encrypt')

def decrypt(ciphertext,key):
    return vigenere_cipher(ciphertext, key, 'decrypt')

# ======================
# 测试用例
# ======================
if __name__ == '__main__':
    # 示例参数
    test_key = 'happycoding'
    original_text = 'hello python!'
    encrypted_text = 'mrttaqrhknsw ih puggrur'

    # 知识点8：f-string格式化输出
    print(f"[加密测试]\n原始文本: {original_text}")
    cipher = encrypt(original_text, test_key)
    print(f"加密结果: {cipher}")

    print(f"\n[解密测试]\n加密文本: {encrypted_text}")
    plain = decrypt(encrypted_text, test_key)
    print(f"解密结果: {plain}")

'''
1、多表替代密码
每个明文字符使用不同凯撒密码加密（密钥字母决定偏移量）

2、模运算控制范围
公式：加密：(p + k) mod 26，解密：(c - k) mod 26
（p=明文位置，k=密钥位置，c=密文位置）

3、密钥循环机制
通过 key_index % len(key) 实现密钥循环使用

4、非字母保留规则
空格、标点等非字母字符保持原样，不参与加密

5、大小写统一处理
所有字符统一转为小写处理（也可扩展支持大小写保留）
'''
