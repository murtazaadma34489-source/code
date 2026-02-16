#include<iostream>

using namespace std;

int array_sum(int arr[],int size){
	
	
	int sum = 0;
	
	for (int i = 0;i<=size;i++){
		
		sum+=arr[i];
	}
	
	return sum;
}




int main (){
	
	
	int arr[]= {1,2,3,4,5};
	
	int size = sizeof(arr) / sizeof (arr[0]);
	
	cout<<"sum of arry element :"<<array_sum(arr,size)<<endl;
	
	
	return 0;
}
