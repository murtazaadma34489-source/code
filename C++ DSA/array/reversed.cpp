#include <iostream>

using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Print reversed array
    for(int i = n-1; i >= 0; i--) {
        cout << arr[i] << " ";
    }

int arr [5] ={1,2,3,4,5};
int n = sizeof(arr)/ sizeof(arr[0]);

for (int i = n-1;i>=0;i--){
	
	cout<<arr[i]<<"";
}

    return 0;
}
