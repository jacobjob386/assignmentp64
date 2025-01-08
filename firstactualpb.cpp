#include<iostream>
using namespace std;
//does not take into account for decimal inputs or inputs of any other datatype other than integer
int main(){
    int n , p , q;
    cout<<"enter an integer :"<<endl;
    cin>>n;
   
    if(n<1)
    {
        cout<<"it is not a power of 2";
        exit(0);
    }
    for(int i = n;i>=2; i=i/2)
    {
        p = i % 2;
       
    }
if(p==0)
{
    cout<<"the number is a power of 2"<<endl;
}
else
{
    cout<<"it is not a power of 2"<<endl;
}
return 0;
}
//should try it with bitwise operators
