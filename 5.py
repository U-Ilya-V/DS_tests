def funcTest5 (lst):
    if type(lst) is not list:
        return print("item is not a list")
    if len(lst) == 0:
        return print("list is empty")
    if not(all(type(item) is str for item in lst)):
        return print("not all elements of type 'str'")
    tempdict = {}
    outputdict = {}
    for i in range(len(lst)):
        if len(lst[i].split()) in tempdict:
            tempdict[len(lst[i].split())] = tempdict[len(lst[i].split())] + 1
        else:
            tempdict[len(lst[i].split())] = 1
    tempdict = dict(sorted(tempdict.items()))
    for i in tempdict:
        match i % 100:
            case num if (num == 1) or (num in range(21,92,10)):
                outputdict[str(i) + " слово"] = str(int(round((tempdict[i]/len(lst)) * 100, 0))) + "%"
            case num if (num == 2) or (num == 3) or (num == 4) or (num in range(22,93,10)) or (num in range(23,94,10)) or (num in range(24,95,10)):
                outputdict[str(i) + " слова"] = str(int(round((tempdict[i]/len(lst)) * 100, 0))) + "%"
            case _:
                outputdict[str(i) + " слов"] = str(int(round((tempdict[i]/len(lst)) * 100, 0))) + "%"
    return outputdict



search_queries = ["watch new movies", 
                  "coffee near me", 
                  "how to find the determinant", 
                  "python", 
                  "data science jobs in UK", 
                  "courses for data science", 
                  "taxi", 
                  "google", 
                  "yandex", 
                  "bing", 
                  "foreign exchange rates USD/BYN", 
                  "Netflix movies watch online free"
                  ]

print(funcTest5(search_queries))


