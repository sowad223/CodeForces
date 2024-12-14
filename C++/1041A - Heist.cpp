
#include<bits/stdc++.h>
using namespace std;
#define ll long long
 

 
int main()
{
    int n;
    cin >> n;
    int mini = INT_MAX, maxi = INT_MIN;
    for (int i=0; i<n; i++)
    {
        int x;
        cin >> x;
        mini = min(mini, x);
        maxi = max(maxi, x);
    }
    cout<<max(0, (maxi-mini)-n+1);
    return 0;
}