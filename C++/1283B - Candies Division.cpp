
#include<bits/stdc++.h>
using namespace std;
#define ll long long
 

 
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        if(n%k==0)
        cout<<n<<endl;
        else
        {
           int a=n/k*k;
            cout<<min(n,a+k/2)<<endl;
        } 
    }
    return 0;
}