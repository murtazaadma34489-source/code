#include<iostream>

using namespace std;

int main () {
	
	
	int n = 3;
	
	for(int i = 1; i<=n;i++){
		
		for(int j = 1;j<=n-1;j++){
			
			cout<<" ";
			
		}
		
		for(int k=1; k<=2*i-1;k++){
			
			cout<<"* ";
		}
		cout<<endl;
	}
		
	return 0;
}
