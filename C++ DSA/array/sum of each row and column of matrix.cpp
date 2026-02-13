#include <iostream>
using namespace std;

int main() {

    int rows = 2, cols = 3;
    int mat[2][3] = {{1, 2, 3}, {4, 5, 6}};
    
    int sumrow[rows]={0};
     for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            sumrow[i] += mat[i][j];
        }
    }
    int sumcol[cols]={0};
      for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            sumcol[i] += mat[i][j];
        }
    }

    cout << "Matrix:\n";
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) cout << mat[i][j] << " ";
        cout << endl;
}
    cout << "Row sum:\n";
    for(int i=0;i<rows;i++) cout<<sumrow[i]<<" ";
      cout<<endl;
      
 cout << "Column Sums: ";
    for(int i = 0; i < cols; i++) cout <<sumcol[i] << " ";
    cout << endl;
 return 0;


}
