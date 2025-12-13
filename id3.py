import pandas as pd
import math

data = pd.read_csv("caunuocngot.csv")
TARGET = "Play"

# Hàm tính Entropy
def entropy(S):
    counts = S.value_counts()
    total = len(S)
    etp = 0

    for c in counts:
        p = c / total
        etp += -p * math.log2(p)

    return round(etp, 3)

# Tính Gain(S, A)
def gain(S, attribute):
    total = len(S)
    values = S[attribute].value_counts()
    info = 0

    for v, count in values.items():
        p = count / total
        subset = S[S[attribute] == v][TARGET]
        info += p * entropy(subset)

    return round(entropy(S[TARGET]) - info, 3)

# Xây dựng cây ID3
def build_tree(S, attributes):
    # Nếu tập mục tiêu chỉ còn 1 loại → lá
    if len(S[TARGET].unique()) == 1:
        return S[TARGET].iloc[0]

    # Nếu hết thuộc tính → chọn nhãn xuất hiện nhiều nhất
    if len(attributes) == 0:
        return S[TARGET].mode()[0]

    # Tính gain cho từng thuộc tính
    gains = {A: gain(S[[A, TARGET]], A) for A in attributes}

    # Chọn thuộc tính có gain cao nhất làm nút
    best_attr = max(gains, key=gains.get)
    tree = {best_attr: {}}

    # Tách nhánh theo từng giá trị của thuộc tính tốt nhất
    for val in S[best_attr].unique():
        subset = S[S[best_attr] == val]
        remain_attrs = [a for a in attributes if a != best_attr]

        tree[best_attr][val] = build_tree(subset, remain_attrs)

    return tree

# In cây quyết định
def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "→ " + str(tree))
        return

    for attr, branches in tree.items():
        print(indent + attr)
        for val, subtree in branches.items():
            print(indent + "|--- " + str(val))
            print_tree(subtree, indent + "     ")

# Main
attributes = list(data.columns.drop(TARGET))

tree = build_tree(data, attributes)

print("\n===== CÂY QUYẾT ĐỊNH ID3 =====")
print_tree(tree)
