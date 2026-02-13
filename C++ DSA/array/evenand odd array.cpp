#include<iostream>

using namespace std;

int main (){
	
	int arr []={1,2,3,4,5,6};
	int n = sizeof(arr)/ sizeof(arr[0]);
	int evencount =0, oddcount= 0;
	
	for (int i = 0;i<=n; i++){
		
		if (arr[i]%2==0 ) evencount++;
		
		else oddcount++;
			
	}
	
	cout<<"Enter of number : "<<evencount<<endl;
	cout<<"Enter of number :"<<oddcount<<endl;
	return 0;
	
}
