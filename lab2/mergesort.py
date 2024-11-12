def merge(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_array = array[left:left + n1]
    right_array = array[mid + 1:mid + 1 + n2]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1

def merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)

        merge(array, left, mid, right)

def print_array(array):
    print("Sorted array:", ' '.join(map(str, array)))

def test_merge_sort_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                array = list(map(int, line.split()))
                
                if array:
                    print("Original array:", ' '.join(map(str, array)))

                    merge_sort(array, 0, len(array) - 1)

                    print_array(array)
                    print()
    except FileNotFoundError:
        print(f"Error opening file: {filename}")

if __name__ == "__main__":
    test_merge_sort_from_file("sorttest.txt")
