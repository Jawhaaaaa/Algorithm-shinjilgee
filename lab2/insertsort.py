def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

def print_(array):
    print("Sorted array:", ' '.join(map(str, array)))

def test_insert_sort_from_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            array = list(map(int, line.split()))  
            if not array:
                continue  
            print("Original array:", ' '.join(map(str, array)))
            insert_sort(array)
            print_(array)

if __name__ == "__main__":

    test_insert_sort_from_file("sorttest.txt")
