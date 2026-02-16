#include<iostream>
using namespace std;

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
int main (){
	int x=5;
	int y=10;
	
	
	cout<<"BEfore swap :"<<endl;
	cout<<"X = "<<x<<endl;
	cout<<"Y ="<<y<<endl;
	
	// is swap is x and y using pointer 
	
	swap(&x, &y);
	
	cout<<"After swap :"<<endl;
	cout<<"X ="<<x<<endl;
	cout<<"Y ="<<y<<endl;
	
	
	return 0;
}
