def merge_sort(num):
    """Divides the list into two halves recursively and calls Merge_Sort"""

    if len(num) < 2:
        return
    mid = int(len(num) // 2)

    left = list()
    right = list()

    for i in range(mid):
        left.append(num[i])
    for j in range(len(num) - mid):
        right.append(num[mid + j])
    merge_sort(right)
    merge_sort(left)

    merge(num, right, left)


def merge(num, right, left):
    """Combines left and right sublists in sort order"""
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            num[k] = left[i]
            i += 1
            k += 1
        else:
            num[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        num[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        num[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    x = [2, 8, 3, 6, 1, 7, 3, 23, 12, 54, 375, 78, 34]
    print(f"Before merge sort :\n{x}")
    merge_sort(x)
    print(f"After merge sort :\n{x}")
