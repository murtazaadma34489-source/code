#include<iostream>

using namespace std;

int main (){
	float units,bill=0;
	
	cout<<"Enter of electricity units consumed.";
	cin>>units;
	
	if (units<=100)
	
		bill= units * 1.20;
     else if(units <=300)
		
	bill=100*1.20+(units - 100)* 2.00;	
	else
	
		bill=100 * 1.20 + 200*2.00 +(units- 300)*3.00;
		
		cout<<"Electricity Bills : RS."<<bill<<endl;
		




	return 0;
}
