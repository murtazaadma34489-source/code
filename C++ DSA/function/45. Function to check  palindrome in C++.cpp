#include<iostream>

using namespace std;

bool is_palindrome(int n){
	
	int original = n , reversed = 0;
	
	while(n!=0){
		
		reversed = reversed * 10 + n % 10;
		n /= 10;
		
	}
	
	return  original == reversed ;
}

int main (){
	
	int num =121;
	 
	 if(is_palindrome(num))
        cout<<num<<"is a palindrom."<<endl;
		
		else 
		         
		         cout<<num<<"is not palindrom"<<endl;
		
         return 0;
	
}
