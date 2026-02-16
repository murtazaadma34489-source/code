#include<iostream>

using namespace std;
 
 
 int reverse_number(int n){
 	
 	int reverse_n = 0;
 	
 	while(n != 0){
 		
 		reverse_n = reverse_n * 10 + n % 10;
 		
 		n /= 10;
	 }
	 
	 return reverse_n ;
 }
 
 
 int main (){
 	
 	int num = 12345678;
 	cout<<"Reverse of"<<num<<"is "<<reverse_number(num)<<endl;
 	
 	
 	return 0;
 	
 }
