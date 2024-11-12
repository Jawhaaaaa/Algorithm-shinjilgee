#include<iostream>
#include<fstream>
#include<sstream>

using namespace std;

int binarySearch(int* array, int left, int right, int target) {
    if (left <= right) {
        int mid = left + (right - left) / 2;

        if (array[mid] == target)
            return mid;

        if (array[mid] > target)
            return binarySearch(array, left, mid - 1, target);

        return binarySearch(array, mid + 1, right, target);
    }

    return -1;
}

void print(int* array, int n) {
    for (int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

void testBinarySearchFromFile(const string& filename, int target) {
    ifstream infile(filename);

    if (!infile.is_open()) {
        cout << "Error opening file: " << filename << endl;
        return;
    }

    string line;
    while (getline(infile, line)) {
        istringstream iss(line);
        int count = 0;

        int num;
        while (iss >> num) {
            count++;
        }

        iss.clear();
        iss.seekg(0, ios::beg);

        int* array = new int[count];
        for (int i = 0; i < count; i++) {
            iss >> array[i];
        }

        if (count > 0) {
            cout << "Array: ";
            print(array, count);

            int result = binarySearch(array, 0, count - 1, target);

            if (result != -1)
                cout << "Element " << target << " found at index " << result << endl;
            else
                cout << "Element " << target << " not found in the array" << endl;

            cout << endl;
        }

        delete[] array;  
    }

    infile.close();
}

int main() {
    int target = 5; 
    testBinarySearchFromFile("searchtest.txt", target);
    return 0;
}
