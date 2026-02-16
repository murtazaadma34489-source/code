#include<iostream>

using namespace std;

unsigned long long factorial_recursive(int n){
	
	if(n==0||n==1)
	
	return 1;
	
	else 
	        return n * factorial_recursive(n-1);
}

int main (){
	
	int num = 5;
	
	cout<<"Factorials of "<<num<<"="<<factorial_recursive(num)<<endl;
	
	return 0;
	
}
