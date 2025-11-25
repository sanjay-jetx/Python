import statistics
def mean_median_mode(list):
    return [statistics.mean(list),statistics.median(list),statistics.mode(list)]

print(mean_median_mode([1,2,3,4,5,5]))