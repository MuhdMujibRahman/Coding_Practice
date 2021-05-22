def group_by_owners(files):
    # Python3 code to demonstrate working of
    # Grouping dictionary keys by value
    # Using sorted() + items() + defaultdict()
    from collections import defaultdict

    # Initialize dictionary
    test_dict = files

    # printing original dictionary

    # Using sorted() + items() + defaultdict()
    # Grouping dictionary keys by value
    res = defaultdict(list)
    # sort = sorted(test_dict, key=lambda p: (p,test_dict[p]))
    # for key, val in sort:
    #     res[val].append(key)
    for i, v in test_dict.items():
        res[v] = [i] if v not in res.keys() else res[v] + [i]

    # printing result


    return str(dict(res))

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))