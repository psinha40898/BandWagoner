import statistics

def sort_by_avg_diff_abs(lst):
    n = len(lst)
    diffs = [abs(statistics.mean(lst) - lst[i]) for i in range(n)]
    sorted_diffs = sorted(diffs)
    sorted_lst = [x for _, x in sorted(zip(diffs, lst))]
    return sorted_lst, sorted_diffs

lst = [.99, .98, .92, -.99, -.78, -.55, 0, 0, .60, .68, -.38, .35]
sorted_lst, sorted_diffs = sort_by_avg_diff_abs(lst)

print(f"Original List: {lst}")
print(f"Differences List: {sorted_diffs}")
print(f"Sorted List: {sorted_lst}")