#include<iostream>

using namespace std;

int main (){
	
       int a, b, c;
       cout<<"Enter of number :";
       cin>>a>>b>>c;
       
       if(a>=b and a>=c){
        cout<<"largest in number1 "<<a<<endl;
       	
	   } else if(b>=a and b>=c){
	   	cout<<"largest in number2 "<<b<<endl;
	   } else{
	   	
	   	 cout<<"largest number3"<<c<<endl;
	   }
	return 0;
}
