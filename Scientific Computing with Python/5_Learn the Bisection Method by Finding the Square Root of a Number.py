def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
    # 知识点1：初始异常值处理（实数域无解情况）
    if square_target < 0:
        raise ValueError("Square target cannot be negative")

    # 知识点2：特殊值优化（0和1直接返回结果）
    if square_target == 1:
        return 1
    elif square_target == 0:
        return 0

    # 知识点3：初始区间选择（兼容0<target<1的情况）
    low = 0
    high = max(1,square_target)  # 例如target=0.25时，high=1而非0.25
    root = None


    # 知识点4：有限迭代次数防止无限循环
    for _ in range(max_iterations):
        mid = (low + high) / 2
        square_mid = mid**2

        # 知识点5：收敛条件（绝对误差小于容忍度）
        if abs(square_mid - square_target) < tolerance:
            root = mid
            break

        # 知识点6：区间更新规则（基于单调递增特性）
        elif square_mid < square_target:
            low = mid  # 目标值在右半区间

        else:
            high = mid


    # 知识点7：收敛失败处理
    if root is None:
        print(f"Failed to converge within {max_iterations} iterations.")
    return root


# 测试案例
# 输入: 16 → 预期输出: ~4.0 (误差<1e-7)
# 输入: 2 → 预期输出: ~1.41421356
print(square_root_bisection(16))    # 输出: 4.0
print(square_root_bisection(2))     # 输出: 1.41421356237...


'''
1. 初始区间选择
high = max(1, square_target) 解决了 target∈(0,1) 时初始区间无效的问题（如 target=0.25，若 high=0.25，则 0.25²=0.0625 <0.25，导致区间无法更新）3。

2. 浮点精度问题
误差累积：多次浮点运算可能导致精度损失，但二分法对此相对鲁棒。
避免死循环：必须设置 max_iterations，防止因误差无法满足 tolerance 导致的无限循环1。

3. 函数扩展性
若改为求其他单调函数的根（如 x³ - target），只需修改 square_mid = mid**2 处的表达式，其余逻辑通用。
'''

'''
1、实数域限制
负数平方根在实数域无解，直接抛出异常

2、边界优化
避免对已知结果（0和1）进行无意义迭代

3、初始区间策略
high = max(1, target) 保证当 0 < target < 1 时区间有效
示例：target=0.25时初始区间为[0,1]，而非[0,0.25]

4、安全迭代机制
设置最大迭代次数（默认100次），防止无法收敛的死循环

5、收敛条件
|mid² - target| < tolerance 基于绝对误差判断（非相对误差）

6、区间更新逻辑
利用平方函数的单调性：
若 mid² < target → 目标在右区间 [mid, high]
若 mid² > target → 目标在左区间 [low, mid]
容错处理
当迭代未达到精度要求时给出明确警告


特性         说明                             
时间复杂度   O(log₂((high-low)/tolerance))  
空间复杂度   O(1)                           
收敛性      保证收敛（若函数连续且单调）                 
适用函数类型  单调连续函数（如x², eˣ, lnx等）

以target=2为例
初始区间：low=0, high=2
第1次迭代：mid=1.0 → 1.0²=1.0 <2 → 更新low=1.0
第2次迭代：mid=1.5 → 2.25 >2 → 更新high=1.5
第3次迭代：mid=1.25 → 1.5625 <2 → 更新low=1.25
继续迭代直到 |mid²-2| <1e-7，最终输出≈1.41421356 

二分法的步骤
1、确定初始区间：选择一个区间 [a, b]，使得函数 f(x) 在该区间两端点的取值异号，即 f(a) * f(b) < 0。
2、计算中点：计算区间的中点 c = (a + b) / 2。
3、判断根的位置：计算 f(c) 的值，如果 f(c) = 0，则 c 就是方程的根；如果 f(c) 与 f(a) 同号，则根在区间 [c, b] 内，令 a = c；否则，根在区间 [a, c] 内，令 b = c。
4、重复步骤2和3：不断重复上述步骤，直到区间的长度小于某个预先给定的精度要求，此时中点 c 即为方程的近似根。
'''