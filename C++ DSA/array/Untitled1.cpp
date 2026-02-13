#include <iostream>
using namespace std;

int main() {
    int arr[] = {5, 2, 8, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    int smallest = arr[0], largest = arr[0];
    
    for(int i = 1; i < n; i++) {
        if(arr[i] < smallest) smallest = arr[i];
        if(arr[i] > largest) largest = arr[i];
    }
    
    cout << "Smallest: " << smallest << endl;
    cout << "Largest: " << largest << endl;
    
    return 0;
}
