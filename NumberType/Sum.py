array_list = [1, 10, 5, 17, 59, 76, 99, 49, 38, 21, 15, 88, 91, 9, 37]


# 排序
class SelfSort:

    # 冒泡排序
    def bubbling_sort(arr):
        for i in range(1, len(arr)):
            for j in range(0, len(arr) - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    # 选择排序
    def choose_sort(arr):
        for i in range(len(arr) - 1):
            index_number = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[index_number]:
                    index_number = j

            if i != index_number:
                arr[j], arr[index_number] = arr[index_number], arr[j]
        return arr


print(SelfSort.bubbling_sort(array_list))
print(SelfSort.choose_sort(array_list))
