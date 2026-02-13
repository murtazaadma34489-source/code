#include<iostream>

using namespace std;

int main (){
	
	 int arr1[] = {1, 2, 3, 4, 5};
    int arr2[] = {6, 7, 8, 9, 10};
    int n = sizeof(arr1) / sizeof(arr1[0]);
    int sum [n];
    
    for (int i = 0;i<n;i++){
    	
    	sum[i] = arr1[i] + arr2[i];
	}
	
	cout<<"Array 1 :";
	
	for (int i= 0;i<n;i++)cout<<arr1[i]<<" ";
	
	cout<< "\n Array2 :";
	
	for(int i =0; i<n;i++)cout<<arr2[i]<<" ";
	
	cout<<"\n Sum :";
	
	for (int i = 0; i<n;i++)cout<<sum[i]<<" ";
	
	return 0;
}
