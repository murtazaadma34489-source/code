#include<iostream>

using namespace std;

int main (){
	
	int num;
	unsigned long long factorial = 1;
	cout<<"Enter of number :";
	cin>>num;
	
	for(int i=1;i<=num;i++){
		
		factorial *=i;
		
	}
	
	cout<<"factorials of "<<num<<"="<<factorial<<endl;
	
	return 0;
}
