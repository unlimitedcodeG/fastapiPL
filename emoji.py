man_list = ['\U0001F466', '\U0001F467', '\U0001F468', '\U0001F469']
# skin_color_list 分别是: 空字符串,表示默认  白种人 -->(不断加深肤色)  黑种人
skin_color_list = ['', '\U0001F3FB', '\U0001F3FC', '\U0001F3FD', '\U0001F3FE', '\U0001F3FF']
for man in man_list:
    for color in skin_color_list:
        print(man + color, end=' ')
    print()
    print('-' * 20)

# Emoji的连接符<U+200D>  (英文名为: ZERO WIDTH JOINER, 简写ZWJ )
# 如果系统支持: 连接(男人 + ZWJ + 女人 + ZWJ + 女孩)
print('\U0001F468\u200D\U0001F469\u200D\U0001F467')
# 如果系统不支持: 连接(狗 + ZWJ + 猫 + ZWJ + 老鼠)
print('\U0001f436\u200D\U0001f431\u200D\U0001f42d')
