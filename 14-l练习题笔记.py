#
#
#
#
# 提取字符串中的数字 并进行取值
#     import re
#     a = 'EUR 1.409,00'    # =>1409
#     b = '€ 409,05'    # => 409.05
#     c = '￥ 409.50'  # => 409.5
#     d = 'CNY 1,000'  # => 1000
#
#     print(re.sub(r'EUR (\d+)(\.?)(\d+)(\,)(\d+)' , r'\1\3',a))
#     print(re.sub(r'€ (\d+)(\,)(0?[1-9])(0+)?', r'\1.\3', b))
#     print(re.sub(r'￥ (\d+)(\.)(0?[1-9])(0+)?', r'\1.\3', c))
#     print(re.sub(r'CNY (\d+)(\,)?(\d+)(\.)?(0?[1-9])?(0+)?', r'\1\3\4\5', d))
#
#     # 关键点尾部去 (0?[1-9])?(0+)?