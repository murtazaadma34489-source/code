#include<iostream>
using namespace std;

int main(){
	
int choice;
float num1 , num2, result;
cout <<"Simples Calculator \n";
cout<<"1.Addition \n";
cout<<"2.Subraction\n";
cout<<"3.Multipication\n";
cout<<"4.Division\n";
cin>>choice;
cout <<"Enter of num1:";
cin>>num1;
cout<<"Enter of num2:";
cin>>num2;

switch (choice){

case 1: result =num1+num2; break;
case 2: result =num1-num2; break;
case 3: result=num1*num2 ; break;

case 4:
    if (num1!=0) result = num1 / num2;
	else {
	cout <<"Erro : Divide by zero ! \n";
		
	return 1;
	}	
	
	break;
	
	default:cout<<"Invalid choice!\n";
	return 1;
}
    cout<<"Result:"<<result<<endl;
      
    return 0;
}
