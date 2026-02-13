#include<iostream>

using namespace std;

int main (){
	
	int num, count = 0;
	cout<<"Enter of number :";
	cin>>num;
	
	for (; num != 0; num/=10){
		
		count++;
	}
	
	cout<<"number of digits"<<cout<<endl;
	
	return 0;
}
