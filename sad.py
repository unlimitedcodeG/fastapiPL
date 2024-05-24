def is_rotational_substring(s1,s2):
    if not s1 or not s2:
        return False
    s1s2 = s1+s2 
    return s1 in s1s2
import torch

# 测试
s1 = "abcd"
s2 = "dabcabc"
print(is_rotational_substring(s1, s2))  # 输出: True