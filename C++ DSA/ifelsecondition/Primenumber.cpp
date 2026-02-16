#include<iostream>

using namespace std;

int main (){
	
	int num;
	int i = 2;
	cout<<"Enter of number ";
	cin>>num;
    if (num%i==0){
    	
    	cout<<num<<"is prime number :"<<endl;
	} else{
		
		cout<<num<<"number not prime number: "<<endl;
	}

	return 0;
}
