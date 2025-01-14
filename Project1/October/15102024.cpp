// // #include <bits/stdc++.h>
// // using namespace std;

// // int main() {
// //     int n, q;
// //     cin >> n >> q;
    
// //     vector<vector<int>> mat(n, vector<int>(n, 0));
    
// //     cin.ignore();
    
// //     // Reading the forest grid
// //     for (int i = 0; i < n; i++) {
// //         string ch;
// //         getline(cin, ch);
// //         for (int j = 0; j < n; j++) {
// //             if (ch[j] == '.') {
// //                 mat[i][j] = 0;
// //             } else if (ch[j] == '*') {
// //                 mat[i][j] = 1;
// //             }
// //         }
// //     }

// //     // Computing prefix sum array
// //     vector<vector<int>> pref(n, vector<int>(n, 0));
// //     for (int i = 0; i < n; i++) {
// //         for (int j = 0; j < n; j++) {
// //             pref[i][j] = mat[i][j];
// //             if (i > 0) pref[i][j] += pref[i-1][j];  // Add from top
// //             if (j > 0) pref[i][j] += pref[i][j-1];  // Add from left
// //             if (i > 0 && j > 0) pref[i][j] -= pref[i-1][j-1];  // Remove double-counted area
// //         }
// //     }

// //     // Answering queries
// //     while (q--) {
// //         int y1, x1, y2, x2;
// //         cin >> y1 >> x1 >> y2 >> x2;

// //         y1--; x1--; y2--; x2--;

// //         int result = pref[y2][x2];
// //         if (y1 > 0) result -= pref[y1-1][x2];  
// //         if (x1 > 0) result -= pref[y2][x1-1];  
// //         if (y1 > 0 && x1 > 0) result += pref[y1-1][x1-1];  

// //         cout << result << endl;
// //     }

// //     return 0;
// // }




// // #include <bits/stdc++.h>
// // using namespace std;

// // int main() {
// //     int n, k;
// //     cin >> n >> k;
    
// //     // We initialize a matrix of size 1001x1001 to accommodate 1-based indexing.
// //     vector<vector<int>> mat(1001, vector<int>(1001, 0));
    
// //     for (int i = 0; i < n; i++) {
// //         int x1, y1, x2, y2;
// //         cin >> x1 >> y1 >> x2 >> y2;
// //         x1--; y1--; x2--; y2--;  // Adjust for 0-based indexing
        
// //         // Mark the region by adding 1 at (x1, y1) and subtracting 1 after (x2)
// //         for (int y = y1; y <= y2; y++) {
// //             mat[y][x1] += 1;
// //             if (x2 + 1 <= 1000) {
// //                 mat[y][x2 + 1] -= 1;
// //             }
// //         }
// //     }

// //     // Counting cells covered exactly `k` times
// //     int total = 0;
// //     for (int y = 0; y < 1000; y++) {
// //         int temp = 0;
// //         for (int x = 0; x < 1000; x++) {
// //             temp += mat[y][x];  // Update the running sum
// //             if (temp == k) {
// //                 total++;  // If the current cell is covered exactly `k` times
// //             }
// //         }
// //     }

// //     cout << total << endl;
// //     return 0;
// // }


// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int n,k;
//     cin>>n>>k;
//     vector<vector<int>> mat(n, vector<int>(n, 0));
//     //inputting
//     int total=0;
//     for(int j=0; j<n;j++){
//         for(int i=0; i<n; i++){
//             cin>>mat[j][i];
//         }
//     }

//     vector<vector<int>> pref(n + 1, vector<int>(n + 1, 0));
//     for (int i = 1; i <= n; i++) {
//         for (int j = 1; j <= n; j++) {
//             pref[i][j] = mat[i-1][j-1] + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1];
//         }
//     }

//     cout<<"donee"<<endl;

//     int maximum = INT_MIN;

//     for(int j=k-1; j<=n-k;j++){
//         for(int i=k-1; i<=n-k; i++){
//             int temp=0;
//             temp+=pref[j+k-1][j+k-1];
//             cout<<temp<<' ';
//             if (i+k<n){
//                 temp+=mat[j][i+k];
//             }
//             if (j+k<n){
//                 temp+=mat[j+k][i];
//             }
//             // if (i-k>=0){
//             //     temp-=pref[j][i-k];
//             //     temp+=mat[j][i-k];
//             // }
//             // if (j-k>=0){
//             //     temp-=pref[j-k][i];
//             //     temp+=mat[j-k][i];
//             // }
//             // maximum = max(maximum,temp);
//         }
//         cout<<endl;
//     }

//     cout<<"here"<<endl;

//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n,m,k;
//     cin>>n>>m>>k;
//     vector<int> vec(n,0);
//     for(int i=0; i<n;i++){
//         cin>>vec[i];
//     }
//     //diff array
//     vector<int> diff(n,0);=
//     diff[0] = vec[0];
//     for(int i=1;i<n;i++){
//         diff[i] = vec[i] - vec[i-1];
//     }
//     vector<vector<int>> mp;
//     //operations mapping
//     for(int i=0;i<m;i++){
//         int l,r,d;
//         cin>>l>>r>>d;
//         mp.emplace_back(l--,r--,d);
//     }
//     while (k){
//         int x,y;
//         cin>>x>>y;
//         x--;y--;
//         for(int i=x;i<=y;i++){
//             int l,r,d;
//             l = mp[i][0];
//             r =  mp[i][1];
//             d =  mp[i][2];
//             diff[l]+=d;
//             diff[r+1]-=d;
//         }
//         k--;
//     }
//     // final prefixing
//     for(int i=1; i<n; i++){
//         vec[i] = vec[i-1] + diff[i];
//     }
//     return 0;
// }


// 


// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int target;
//     cin>>target;
//     vector<int> arr;
//     int i=0;
//     int j=arr.size()-1;
//     int index = arr.size()-1;
//     while(i<=j){
//         int mid = i+(i+j)/2;
//         if (arr[mid]>target){
//             index = mid;
//             j = mid-1;
//         }
//         else{
//             i = mid+1;
//         }
//     }
//     cout<<index;
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int target;
//     cin>>target;
//     vector<int> arr;
//     int i=0;
//     int j = arr.size()-1;
//     int index = arr.size();
//     while(i<=j){
//         int mid = i+(j-i)/2;
//         if (arr[mid]<target){
//             index = mid;
//             j = mid-1;
//         }
//         else{
//             i = mid+1;
//         }
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){

//     int target;
//     cin>>target;
//     vector<int> arr;
//     int index = -1;
//     int i=0;
//     int j = arr.size()-1;
//     while (i<=j){
//         int mid = (i+j)/2;
//         if (target==arr[mid]){
//             index = mid;
//             break;
//         }
//         if (arr[i]<=arr[mid]){
//             // left sorted
//             if (arr[i]<=target && target<arr[mid]){
//                 j = mid-1;
//             }
//             else{
//                 i = mid+1;
//             }
//         }
//         else{
//             //right sorted
//             if(arr[j]>=target && target>arr[mid]){
//                 i = mid+1;
//             }
//             else{
//                 j =mid-1;
//             }
//         }
//     }
//     cout<<index;
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){

//     vector<int> arr;
//     int i=0;
//     int j = arr.size();
//     int index = -1;
//     int target;
//     bool flag = false;
//     while(i<=j){
//         int mid = (i+j)/2;
//         //adjusting mid
//         while(arr[mid]==arr[mid-1]){
//             mid--;
//         }
//         if (target==arr[mid]){
//             flag = true;
//             break;
//         }
//         if(arr[i]<=arr[mid]){
//             //left sorted
//             if (arr[i]<=target && target<arr[mid]){
//                 j = mid-1;
//             }else{
//                 i = mid+1;
//             }
//         }
//         else{
//             // right sorted
//             if(arr[j]>= target && target>arr[mid]){
//                 i = mid+1;
//             }
//             else{
//                 j = mid-1;
//             }
//         }
        
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int func(int mid,vector<int> vec,int median,int k){
//     int accumulator = 0;
//     for(int i=(vec.size()-1)/2;i<vec.size();i++){
//         accumulator+=(mid-vec[i]);
//     }
//     return accumulator<=k;
// }

// int main(){

//     int n,k;
//     cin>>n>>k;
//     vector<int> vec(n,0);
//     for(int i=0;i<n;i++){
//         cin>>vec[i];
//     }
//     sort(vec.begin(),vec.end());
//     int median =vec[(0+vec.size()-1)/2];
//     long long i = median;
//     long long j = 2*INT_MAX;
//     long long result = -1;
//     while(i<=j){
//         long long mid = (i+j)/2;
//         if (func(mid,vec,median,k)){
//             result = mid;
//             i = mid+1;
//         }
//         else{
//             j = mid-1;
//         }
//     }
//     cout<<result;
//     return 0;
// }


#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,q;
    cin>>n>>q;
    vector<int> vec(n,0);
    for(int i=0;i<n;i++){
        cin>>vec[i];
    }

    //precomputation
    vector<pair<int,int>> pref;
    pref.emplace_back(vec[0],1);
    for(int i=1;i<n;i++){
        pref.emplace_back(vec[i],pref[i-1].second++);
    }

    while(q){
        int a,b;
        cin>>a>>b;
        cout<<lower_bound(pref.begin(),pref.end(),b)-lower_bound(pref.begin(),pref.end(),a);
        q--;
    }
    
    return 0;
}


#include <bits/stdc++.h>
using namespace std;

int bin(){

}

bool f(int distance,vector<int> cities){
    for(int i=0;i<cities.size();i++){
        if (distance<abs(cities-bin())){
            return false;
        }
    }
    return true;
}

int main(){
    int n,m;
    cin>>n>>m;
    vector<int> cities(n,0);
    vector<int> towers(n,0);
    int i=0; // cities 
    int j=INT_MAX;
    // int maxd = 0;
    // while(i<cities.size()){
    //     while(j+1<towers.size()&& abs(cities[i]-towers[j])>=abs(cities[i]-towers[j+1])){
    //         j++;
    //     }
    //     maxd = max(maxd,abs(cities[i]-towers[j]));
    //     i++;
    // }
    int result = INT_MAX;
    while(i<=j){
        int mid = (i+j)/2;
        if (f(mid,cities)){
            result = mid;
            j--;
        }
        else{
            i++;
        }
    }
    cout<<result;
    i= min(arr);
    while(i<=INT_MAX){
        int total = 0;
        int left_time = i;
        for(auto &j: arr){
            if (total==desired){
                break;
            }
            total+=int(left_time/j);
        }
        if (total==desired){
                break;
        }
        i++;
    }
    return 0;
}