#include <iostream>

using namespace std;

int main (){
	int marks;
	cout<<"enter of number :";
	cin>>marks;
	
	if(marks>=90){
	
	cout<<"Grade of A:"<<marks<<endl; 
	}else if(marks>=70){
		
		cout<<"Grade of B:"<<marks<<endl;
	}else if(marks>=50){
		
		cout<<"Grade of C:"<<marks<<endl;	
	
	}else if (marks>=40){
		
		cout<<"Grade of D:"<<marks<<endl;

	} else{
		
		cout<<"fails"<<endl;
	}
	

	return 0;
}
