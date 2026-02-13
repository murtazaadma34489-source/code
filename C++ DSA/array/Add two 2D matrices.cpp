#include<iostream>

using namespace std;

int main (){
	
        int row = 2, cols = 2;
		int mat1[2][2] = {{1,2},{3,4}};
		int mat2[2][2]= {{5,6},{5,6}};
		int sum [2][2];
	    // adding of matrix
	    for (int i= 0; i<row;i++){
	    	
	    	for (int j=0;j<cols;j++){
	    		
	    		sum [i][j] = mat1[i][j] ,mat2[i][j];
			}
		}
		
		cout<<"Matrix1 : \n";
		for (int i = 0; i<row;i++){
			
			for(int j=0;j<cols;j++) cout<<mat1[i][j]<<" ";
			
			cout<<endl;
		}
	         
	    cout<<"Matrix2 : \n";
		for (int i = 0; i<row;i++){
			for(int j=0;j<cols;j++)cout<<mat2[i][j]<<" ";
			
			cout<<endl;
		}
	
	 cout<<"Sum : \n";
		for (int i = 0; i<row;i++){
			for(int j=0;j<cols;j++)cout<<sum[i][j]<<" ";
			
			cout<<endl;
		}
	
	return 0;
}
