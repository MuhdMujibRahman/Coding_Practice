from collections import OrderedDict, defaultdict
import json

def sort_by_price_ascending(json_string):
    price_sort = []
    test_dict = json.loads(json_string)
    itemDict = OrderedDict([(eachItem['name'],eachItem['price'],) for eachItem in test_dict])
    # res = defaultdict(list)
    # for i, v in test_dict.items():
    #     res[v] = [i] if v not in res.keys() else res[v] + [i]
    soretedItem = sorted(itemDict, key=lambda p: (itemDict[p],p))
    for d in soretedItem:
        for eachItem in test_dict:
            if eachItem['name'] == d:
                price_sort.append(eachItem)
    return json.dumps(price_sort)

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))