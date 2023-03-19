def count_positives_sum_negatives(arr):
    if arr == []:
        print([])
    else:
        positive = 0
        negative = 0
        for x in arr:
            if x > 0:
                positive += 1
            elif x < 0:
                negative += x
        print([positive, negative])




count_positives_sum_negatives([])
