#include<iostream>
using namespace std;

int main (){

	char c;
	cout<<"Enter of character:";
	cin>> c;
	if((c>='a'&& c<='z') ||(c>='A' && c<='Z')){	
	 
	 if (c=='a'|| c=='e'||c=='i'||c=='o'||c=='u'||
	    c=='A'||c=='E'||c=='I'||c=='O'||c=='U'){
	    	
	    cout<<c<<" is a Vowel."<<endl;
		}else{
			cout<<c<<"is  a Constonant"<<endl;
		}
		
		}else{
		
		cout<<c<<"is not an alphabet"<<endl;	
	
		}


	return 0;
}
