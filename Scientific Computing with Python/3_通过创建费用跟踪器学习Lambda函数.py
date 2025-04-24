# 知识点1：列表与字典的复合数据结构
# 使用列表存储支出记录，每个记录是包含金额和类别的字典
from unicodedata import category


def add_expense(expenses, amount,category):
    expenses.append({'amount': amount, 'category': category})


# 知识点2：字符串格式化（f-string）
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount:{expense["amount"]}, Category:{expense["category"]}')


# 知识点3：Lambda函数与map高阶函数
def total_expenses(expenses):
    # 使用map提取金额，sum计算总和
    return sum(map(lambda expense: expense['amount'], expenses))

# 知识点4：Filter函数与条件过滤
def filter_expenses_by_category(expenses, category):
    # 使用lambda创建过滤条件
    return filter(lambda expense: expense['category'] == category, expenses)
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。


def main():
    expenses = []  # 知识点5：列表初始化

    # 知识点6：无限循环与菜单驱动界面
    while True:
        print('\nExpense Tracker')  # 转义字符
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        # 知识点7：用户输入处理
        choice = input('Enter your choice: ')  # 字符串输入

        # 知识点8：条件分支控制
        if choice == '1':
            # 类型转换与错误处理（潜在改进点）
            amount = float(input('Enter the amount of the expense: '))  # 字符串转浮点数
            category = input('Enter the category of the expense: ')
            add_expense(expenses, amount, category)


        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)  # 函数调用


        elif choice == '3':
            # 知识点9：函数返回值使用
            print('\nTotal Expenses: ', total_expenses(expenses))


        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            # 知识点10：filter对象迭代
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)  # 遍历filter对象


        elif choice == '5':
            print('\nExit')
            break  # 退出循环

# 知识点11：主程序入口约定
if __name__ == '__main__':
    main()



'''
1、添加支出记录

对应知识点1：使用列表存储字典结构数据
功能：通过 add_expense 函数将金额和类别以字典形式添加到列表中
示例输入：金额 100，类别 food → 列表添加 {'amount':100, 'category':'food'}


2、列出所有支出

对应知识点2：使用 f-string 格式化输出
功能：通过 print_expenses 函数遍历列表并打印每条记录的金额和类别
示例输出：Amount: 100.0, Category: foodAmount: 50.0, Category: transport


3、显示总支出

对应知识点3：Lambda + map 高阶函数
功能：通过 total_expenses 函数计算所有支出金额的总和
示例数据：[100, 50, 200] → 总和 350.0


4、按类别筛选支出

对应知识点4：filter + lambda 条件过滤
功能：通过 filter_expenses_by_category 函数返回指定类别的支出
示例调用：筛选类别 food → 输出所有 category 为 food 的记录


5、初始化数据存储

对应知识点5：列表初始化
功能：在 main() 函数中创建空列表 expenses = []，用于存储所有支出记录
作用：作为整个程序的数据存储核心结构

'''

