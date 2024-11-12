#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int findMax(int* array, int left, int right) {
    if (left == right) {
        return array[left];
    }
    
    int mid = left + (right - left) / 2;

    int leftMax = findMax(array, left, mid);
    int rightMax = findMax(array, mid + 1, right);

    return max(leftMax, rightMax);
}

void print(int* array, int n) {
    for (int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

void testMaxFromFile(const string& filename) {
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
            cout << "Original array: ";
            print(array, count);

            int max_value = findMax(array, 0, count - 1);
            cout << "Maximum value: " << max_value << endl;
            cout << endl;
        }

        delete[] array;  
    }

    infile.close();
}

int main() {
    testMaxFromFile("sorttest.txt");
    return 0;
}
