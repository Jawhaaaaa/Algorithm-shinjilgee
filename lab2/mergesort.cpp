#include<iostream>
#include<fstream>
#include<sstream>

using namespace std;

void merge(int* array, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int* leftArray = new int[n1];
    int* rightArray = new int[n2];

    for (int i = 0; i < n1; i++)
        leftArray[i] = array[left + i];
    for (int j = 0; j < n2; j++)
        rightArray[j] = array[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (leftArray[i] <= rightArray[j]) {
            array[k] = leftArray[i];
            i++;
        } else {
            array[k] = rightArray[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        array[k] = leftArray[i];
        i++;
        k++;
    }

    while (j < n2) {
        array[k] = rightArray[j];
        j++;
        k++;
    }

    delete[] leftArray;
    delete[] rightArray;
}

void mergeSort(int* array, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(array, left, mid);
        mergeSort(array, mid + 1, right);

        merge(array, left, mid, right);
    }
}

void print(int* array, int n) {
    for (int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

void testMergeSortFromFile(const string& filename) {
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

            mergeSort(array, 0, count - 1);

            cout << "Sorted array: ";
            print(array, count);
            cout << endl;
        }

        delete[] array;  
    }

    infile.close();
}

int main() {
    testMergeSortFromFile("sorttest.txt");
    return 0;
}
