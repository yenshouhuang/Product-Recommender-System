from datetime import datetime
from apyori import apriori


def checkHistory(user_id,product):
    flat_list = [item for sublist in new_result[user_id] for item in sublist]
    if product in flat_list:
        return True
    else:
        return False



start = datetime.now()

user_generic_apriori = {}
user_generic_rules = apriori(record, min_support=0.0001, min_confidence=0.001, min_lift=1)
user_generic_apriori[user_id] = list(user_generic_rules)
user_prediction_result = {}



for user_id, productList in sc_result.items():
    user_prediction_result[user_id] = []
    # for product in productList[1:]:
    for prev_num, product in enumerate(productList[1:]):
        user_specific_apriori = {}

        if checkHistory(user_id, product) == True:
            user_specific_rules = apriori(new_result[user_id], min_support=0.0001, min_confidence=0.001, min_lift=1)
            user_specific_apriori[user_id] = list(user_specific_rules)
            relation_result = [rr for rr in user_specific_apriori[user_id] if
                               (productList[prev_num] == list(rr.items)[0])]
            relation_result.sort(key=lambda x: x.ordered_statistics[0].confidence, reverse=True)
            relation_result = relation_result[0:9]
            list_of_two = [list(rr.items) for rr in relation_result]
            ret = 0
            for res in list_of_two:
                if product in res:
                    ret = 1
                    break
            user_prediction_result[user_id].append(ret)

        else:

        
            # sort the result and find out the confidence result with item A

            relation_result = [rr for rr in user_generic_apriori[user_id] if
                               (productList[prev_num] == list(rr.items)[0])]
            relation_result.sort(key=lambda x: x.ordered_statistics[0].confidence, reverse=True)
            relation_result = relation_result[0:9]
            list_of_two = [list(rr.items) for rr in relation_result]
            ret = 0
            for res in list_of_two:
                if product in res:
                    ret = 1
                    break
            user_prediction_result[user_id].append(ret)

print(user_prediction_result)

end = datetime.now()
time_taken = end - start
print('Time: ', time_taken)
