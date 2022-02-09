# 转置
def transformMatrix(m) -> [tuple]:
    # 逆向参数收集，将矩阵中多个列表转换成多个参数，传给 zip
    return list(zip(*m))
