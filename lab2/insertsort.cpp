#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

void insertSort(int* array, int n) {
    for (int i = 1; i < n; i++) {
        int key = array[i];
        int j = i - 1;

        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            j = j - 1;
        }
        array[j + 1] = key;
    }
}

void print(int* array, int n) {
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

void testInsertSortFromFile(const string& filename) {
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
            for (int i = 0; i < count; i++) {
                cout << array[i] << " ";
            }
            cout << endl;

            insertSort(array, count);
            print(array, count);
        }

        delete[] array;  
    }

    infile.close();
}

int main() {
    testInsertSortFromFile("sorttest.txt");
    return 0;
}
