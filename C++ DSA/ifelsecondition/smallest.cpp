#include<iostream>

using namespace std;

int main (){
	int a, b, c;
	cout<<"Enter of number :";
	cin>>a>>b>>c;
	
	if(a<=b && a<=c){
		
		cout<<"smallest number"<<a<<endl;
	} else if(b<=a && b<= c ){
		
		cout<<"Smallestnumber"<<b<<endl;
	} else{
		
		cout<<"smallest number"<<c<<endl;
	}
	
	return 0;
}
