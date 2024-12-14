
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
 


bool isHard(int a[], int n)
{
    for(int i=0;i<n;i++)
    {
        if(a[i]==1)
        return true;
    }
    return false;
}

int main()
{
    int n;
    cin>>n;
    int qL[n];
    for(int i = 0;i<n;i++)
    {
        cin>>qL[i];
    }
    if(isHard(qL,n))
    cout<<"HARD"<<endl;
    else
    cout<<"EASY"<<endl;
    return 0;
}