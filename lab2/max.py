def find_max(array, left, right):
    if left == right:
        return array[left]

    mid = (left + right) // 2

    left_max = find_max(array, left, mid)
    right_max = find_max(array, mid + 1, right)

    return max(left_max, right_max)

def test_max_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                array = list(map(int, line.split()))

                if array:
                    max_value = find_max(array, 0, len(array) - 1)
                    print("Original array:", ' '.join(map(str, array)))
                    print("Maximum value:", max_value)
                    print()
    except FileNotFoundError:
        print(f"Error opening file: {filename}")

if __name__ == "__main__":
    test_max_from_file("sorttest.txt")
