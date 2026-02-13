#include<iostream>

using namespace std;

int main (){
	
	int arr[]={1,24, 5l,67,};
	int n= sizeof(arr)/ sizeof(arr[0]);
	int sum = 0;
	
	for (int i=0;i<n;i++){
		
		sum+= arr[i];
	}
	
    double  avg = (double) sum /n;
    cout<<"Sum"<<sum<<endl;
    cout<<"aversages"<<avg<<endl;
	
	return 0;
}
