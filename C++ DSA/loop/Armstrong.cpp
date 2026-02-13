#include<iostream>

using namespace std;

int main (){
	
	int num,sum= 0,tem=num;
	cout<<"Enter a number :";
	cin>>num;
	for (tem=num;tem!=0;tem/=10){
		
		int digit = tem % 10;
		sum+= digit *digit *digit
	}
	
	cout<<(sum==num?"arMstrong ":"not Armstrong")<<endl;
	
	return 0;
}
