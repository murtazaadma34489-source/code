#include<iostream>

using namespace std;
         
         // Function to find the length of a string using pointers
         int strlen(char* str){
         	
         	int  length = 0;
         	
         	while(*str!='\0'){
         		
         		length ++;
         		str++;
			 }
			 
			 return length;
		 }
		 
int main (){
	
	char str[]=" Muhammad Murtaza ";
	
    int length = strlen(str);
	
	cout<<"String :"<<str<<endl;
	cout<<"length :"<<length<<endl;
	
	
	return 0;
}
