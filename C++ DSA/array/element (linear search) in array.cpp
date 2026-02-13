#include<iostream>

using namespace std;

int main (){
	
	int arr []= {10, 20, 30, 40, 50 };
	
	int n = sizeof (arr) / sizeof(arr[0]);
	int target= 30;
	int found= -1;
	
	for (int i = 0; i<n;i++){
		
		if(arr[i]==target){
	
			found =i;
			break;
		}
	}
	   if (found != -1)
	   
	   cout<<"Enter of Element"<<target<<"found of index"<<found<<endl;
	   
	   else 
	      
	       cout <<"Element"<<target<<"not found of index"<<found<<endl;
	
	
	return 0;
}
