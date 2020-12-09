import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

shoppingCartData = pd.read_csv('shopping_cart_data.csv', header = None)
purchaseHistory =  pd.read_csv('purchase_history_data.csv', header = None)

result = {}
for i in range(len(purchaseHistory)):

    if purchaseHistory[1][i] in result:

        user_dict = result[purchaseHistory[1][i]]
        if purchaseHistory[0][i] in user_dict:
            order_array = user_dict[purchaseHistory[0][i]]
            product_id = purchaseHistory[8][i]
            order_array.append(product_id)
        else:
            user_dict[purchaseHistory[0][i]] = [purchaseHistory[8][i]]

    else:
        result[purchaseHistory[1][i]] = {purchaseHistory[0][i]: [purchaseHistory[8][i]]}


new_result = {}
for k, v in result.items():
    array_of_arrays = []
    for m, n in v.items():
        array_of_arrays.append(n)
    new_result[k] = array_of_arrays




group_purchase = purchaseHistory.groupby(0)
record = []
order_array = {}
for id, df in group_purchase:
    if id == "order_id":
        continue

    else:
        # print(df[8].tolist())
        tmp_list = df[8].tolist()
        # for item in tmp_list:
        # item = int(item)
        for i in range(len(tmp_list)):
            tmp_list[i] = str(tmp_list[i])
        order_array[id] = tmp_list
        record.append(tmp_list)