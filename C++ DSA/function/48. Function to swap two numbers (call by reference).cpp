#include<iostream>

using namespace std;

void SwapByReference(int &a,int &b){
	
	
	int temp=a;
	
	a= b;
	b= temp;
}

int main (){
	
		int x = 5, y = 10;
	
	cout<<"Before swap : X = "<<x<<" y = "<<y<<endl;
	
	SwapByReference (x,y);
	
	cout<<"After is  swap  (call by in Reference ): X = "<<x<<", y = "<<y<<endl;
	
	
	return 0;
}
