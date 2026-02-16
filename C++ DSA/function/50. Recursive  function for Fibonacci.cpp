#include<iostream>

using namespace std;

unsigned long long fibonacci(int n){
	
	if (n ==0){
		
		return 0;
		
	} else if (n==1){
		
		return 1;
	} else {
		
		return fibonacci(n -1  ) + fibonacci(n-2);
	}
}





int main (){
	
	
	int num ;
	
	std::cout<<"Enter of number  :";
	std::cin>>num;
	std::cout<<"Fibonacci is number  at  position "<<num<<" = "<<fibonacci(num)<<std::endl;
	
	
	
	
	return 0;
}
