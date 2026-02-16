#include<iostream>

using namespace std;


void swapByValue(int a,int b){
	
	
	int temp = a;
	
	a = b;
	b = temp;
	
	cout<<"Inside swapByvalue : a = "<<a<< ", b = "<<b<<endl;
}


int main (){
	
	int x = 5, y = 10;
	
	cout<<"Before swap : X = "<<x<<" y = "<<y<<endl;
	
	swapByValue (x,y);
	
	cout<<"After is  swap  (call by in value): X = "<<x<<", y = "<<y<<endl;
	
	return 0;
}
