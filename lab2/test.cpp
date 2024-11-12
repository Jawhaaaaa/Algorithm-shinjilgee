#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream file("text.txt");  

    if (file) {  
        string line;
        getline(file, line);
        if(line.empty()){
            cout << "Hooson" << endl;
        }else{
            cout << line << endl; 
        } 
    } else {
        cout << "!" << endl;  
    }
    return 0;
}
