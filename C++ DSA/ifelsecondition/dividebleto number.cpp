#include<iostream>

using namespace std;

int main (){
	
	int num;
	cout<<"Enter of number ";
	cin>>num;
	if(num%5==0 && num % 11==0){
		
	cout<<num<<"is dividble by in both 5 to 11"<<endl;
	} else if(num % 5 ==0){
		
		cout<<num<<"is divsible by 5in but not 11"<<endl;
	}else if (num%11==0){
		
		cout<<num<<"is divisble by 11 but not 5"<<endl;	
	} else{
		
		cout<<num<<"is not divisble by 5 to 11"<<endl;
	}
	
	return 0;
}
