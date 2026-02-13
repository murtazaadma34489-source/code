#include<iostream>

using namespace std;

int main (){
	
	int arr [6] ={3,5,6,7,9,6,};
	
	int n = sizeof(arr) / sizeof(0);
	int smallest=arr[0],largest= arr [0];
	
	for (int i=1;i<n;i++){
		
		if(arr[i] < smallest) smallest = arr[i];
		if (arr[i]>largest) largest= arr[i];
		
	}
	
	cout<<"smallest number "<<smallest<<endl;
	cout<<"largest number"<<largest<<endl;
	return 0;
}
