#include<iostream>

using namespace std;

int main (){
	int num, rev = 0, orig;
	cout<<"Enter of number : ";
	cin>>num;
	while(num != 0){
		rev = rev * 10 + num % 10;
		num /= 10;	
	}
	if (orig==rev){
		cout<<orig<<"is a Palindrom."<<endl;
	} else{
		cout<<orig<<"is not a Palindrom."<<endl;
	}
	
	return 0;
}
