
#include<bits/stdc++.h>
using namespace std;
#define ll long long
 

 
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int a,b,n;
        cin>>a>>b>>n;
        int t = a;
        int c =0;
        if(a<b)
        {
            t = a;
            a = b;
            b = t;
        }
        while(true)
        {
            if(c%2==0)
            {
                b += a;
                t = b;
            }
            else
            {
                a += b;
                t = a;
            }
            c++;
            if(t>n)
            break;
            
        }
        cout<<c<<endl;
    }
    return 0;
}

