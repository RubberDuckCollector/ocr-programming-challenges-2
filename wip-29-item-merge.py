def item_merge(list1, list2):

    unique_items = list(set(list1).symmetric_difference(set(list2)))

    return unique_items, 

fruit1 = ['Apple' , 'Grapes']
fruit2 = ['Grapes' , 'Orange']

print(item_merge(fruit1, fruit2))