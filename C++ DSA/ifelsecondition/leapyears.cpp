#include<iostream>

using namespace std;

int main (){
	
	int year=10000000000;
	
	if((year% 4 ==0 && year % 100 !=0) ||(year % 400==0)){
		
		cout<<year<<"is a leap Years"<<endl;
	}else{
		
		cout<<year<<"is not leap years."<<endl;
	}
	
	
	return 0;
}
