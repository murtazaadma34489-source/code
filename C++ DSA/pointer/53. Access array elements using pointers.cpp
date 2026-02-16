#include<iostream>

using namespace std;

int main (){
	
	int arr[5]= {1,2,3,4,5};
	
	int *ptr = arr;
	
	cout<<"Enter of Element :"<<endl;
	
	for (int i=0;i<5;i++){
		
	cout << "arr[" << i << "] = " << *(ptr + i) <<endl;
	
	}
	
	  // Access array elements using array notation
    cout << "\nArray elements (array notation):" <<endl;
    for (int i = 0; i < 5; i++) {
        cout << "arr[" << i << "] = " << arr[i] <<endl;
    }
	
	    // Access array elements using pointer arithmetic
    cout << "\nArray elements (pointer arithmetic):" <<endl;
    for (int i = 0; i < 5; i++) {
        cout << "arr[" << i << "] = " << *ptr <<endl;
        ptr++;
    }
	
	
	return 0;
	
	
}
