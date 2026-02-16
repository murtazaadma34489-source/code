#include<iostream>

using namespace std;

int sumArry(int* arr, int size ){
	
	int sum = 0;
	
	for (int i = 0; i< size ;i++ ){
		
		sum+= *arr;
		
		arr++;
	}
	
	return sum;
}


int main (){
	
	int arr[]={1,2,3,4,5};
	
	int  size = sizeof (arr) / sizeof (arr[0]);
	
	int sum = sumArry(arr,size);
	
	cout<<" Array is  Element "<<endl;
	
	for (int i= 0;i<size;i++){
		
		cout<<arr[i]<<" ";
	}
	
	cout << endl;
    cout << "Sum of array elements: " << sum <<endl;
	
	return  0;
}
