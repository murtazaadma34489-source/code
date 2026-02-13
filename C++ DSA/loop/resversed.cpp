#include<iostream>

using namespace std;

int main (){
	
int num,reversed=0;
cout<<"Enter of number ";
cin>>num;
for (;num!=0;num/=10){
	
	int digit = num % 10;
	reversed = reversed * 10 + digit;
}	
	cout<<"Reversed number "<<reversed<<endl;
	return 0;
}
