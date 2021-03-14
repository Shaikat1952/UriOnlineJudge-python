#include<iostream>
using namespace std;
int main(){
    int n,i,angle=1;
    cin>>n;
    if(n>=3){
        for(i=3;i<n;i++){
            angle++;
        }
    }
    cout<<angle<<endl;
}