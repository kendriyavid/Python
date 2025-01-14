// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n,q;
//     cin>>n>>q;
//     vector<int> vec(n);
//     for(int i=0;i<n;i++){
//         cin>>vec[i];
//     }
//     // preprocessing
//     for(int i=1;i<n;i++){
//         vec[i]= vec[i-1]+vec[i];
//     }
//     while(q--){
//         int l,r;
//         cin>>l>>r;
//         int result = vec[r-1];
//         if(l-2>=0){
//             result-=vec[l-2];
//         }
//         cout<<result;
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     string input;
//     int q;
//     cin>>input>>q;
//     vector<int> vec(input.size(),0);
//     if(input[0]=='a'){
//         vec[0]=1;
//     }
//     for(int i=1;i<vec.size();i++){
//         if(input[i]=='a'){
//             vec[i] = vec[i-1]+1;
//         }
//         else{
//             vec[i] = vec[i-1];
//         }
//     }
//     while(q--){
//         int l,r;
//         cin>>l>>r;
//         int result= vec[r-1];
//         if(l-2>=0){
//             result-=vec[l-2];
//         } 
//         cout<<result<<endl;
//     }
// }

// b fence codeforces div2 211 round

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n,k;
//     cin>>n>>k;
//     vector<int> heights(n,0);
//     for(int i=0;i<n;i++){
//         cin>>heights[i];
//     }
//     // prefixing
//     for(int i=1;i<n;i++){
//         heights[i]+=heights[i-1];
//     }
//     int minimum = heights[k-1];
//     int index=1;
//     for(int i=k;i<n;i++){
//         // removing
//         int temp = heights[i]-heights[i-k];
//         if(minimum>temp){
//             minimum = temp;
//             index = i-k+2;
//         }
//     }
//     cout<< index;
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     vector<int> vec(n,0);
//     for(int i=0;i<n;i++){
//         cin>>vec[i];
//     }
//     // precomputation
//     for(int i=1;i<n;i++){
//         vec[i] += vec[i-1];
//     }
//     //hmap sum --> index
//     unordered_map<int,int> mp;
//     int maxsize=0;
//     for(int i=0;i<n;i++){
//         int remainder = vec[i]%7;
//         if(mp.find(remainder)!=mp.end()){
//             maxsize = max(maxsize,i-mp[remainder]+1);
//         }
//         mp[vec[i]]=i;
//     }
//     cout<<maxsize;
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int cases;
//     cin >> cases;
//     while (cases--) {
//         int n, k;
//         cin >> n >> k;
//         vector<int> lastK(k, 0);
//         for (int i = 0; i < k; i++) {
//             cin >> lastK[i];
//         }
//         vector<int> original(n, 0);

//         // Compute the last `k` elements
//         int pointer = n - 1;
//         for (int i = k - 1; i > 0; i--) {
//             original[pointer] = lastK[i] - lastK[i - 1];
//             pointer--;
//         }

//         // Compute the remaining elements
//         int remaining = lastK[0];
//         for (int i = pointer; i >= 0; i--) {
//             if (i == 0) {
//                 original[i] = remaining; // Assign leftover remaining value
//                 break;
//             }
//             original[i] = max(0, original[i + 1] - 1); // Ensure non-negative values
//             remaining -= original[i];
//         }

//         // Check if the array is non-decreasing
//         bool isValid = true;
//         for (int i = 1; i < n; i++) {
//             if (original[i] < original[i - 1]) {
//                 isValid = false;
//                 break;
//             }
//         }

//         // Output result
//         if (isValid) {
//             cout << "YES\n";
//         } else {
//             cout << "NO\n";
//         }
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     //inputted the vectors
//     int i,j,k=0;
//     while(i<vec1.size() and j<vec2.size()){
//         if(vec1[i]>vec2[j]){
//             resvec[k] = vec2[j];
//             j++;
//             k++;
//         }
//         else{
//             resvec[k] = vec1[j];
//             i++;
//             k++;
//         }
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n,m;
//     cin>>n>>m;
//     vector<int> a(n);
//     vector<int> b(m);
//     for(int i=0;i<n;i++){
//         cin>>a[i];
//     }
//     for(int i=0;i<m;i++){
//         cin>>b[i];
//     }
//     // result vector
//     vector<int> result(n+m,0);
//     int i=0;
//     int j=0;
//     int k=0;
//     while (i < a.size() || j < b.size()) {
//         if ((j == b.size() || a[i] <= b[j])) {
//             result[k] = a[i];
//             i++;
//         } else {
//             result[k] = b[j];
//             j++;
//         }
//         k++;
//     }
//     for(int i=0;i<n+m;i++){
//         cout<<result[i]<<" ";
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n,m;
//     cin>>n>>m;
//     vector<int> a(n);
//     vector<int> b(m);
//     for(int i=0;i<n;i++){
//         cin>>a[i];
//     }
//     for(int i=0;i<m;i++){
//         cin>>b[i];
//     }
//     vector<int> result(m);
//     int i=0;
//     for(int j=0;j<m;j++){
//         while(a[i]<b[j] and i<a.size()){
//             i++;
//         }
//         result[j] = i; 
//     }
//     for(int k=0;k<m;k++){
//         cout<<result[k]<<" ";
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n,m;
//     cin>>n>>m;
//     vector<int> a(n);
//     vector<int> b(m);
//     for(int i=0;i<n;i++){
//         cin>>a[i];
//     }
//     for(int i=0;i<m;i++){
//         cin>>b[i];
//     }
//     int total=0;
//     int i=0;
//     int j=0;
//     while(j<m){
//         int count=0;
//         while(a[i]==b[j] and i<a.size()){
//             count++;
//             i++;
//         }
//         if(count>1){
//         int count2=1;
//         while(b[j]==b[j+1]){
//             count2+=1;
//             j++;
//         }
//         total+=count*count2;}
//         j++;
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n,m;
//     cin>>n>>m;
//     vector<int> a(n);
//     vector<int> b(m);
//     for(int i=0;i<n;i++){
//         cin>>a[i];
//     }
//     for(int i=0;i<m;i++){
//         cin>>b[i];
//     }
//     if (n == 0 || m == 0) {
//     cout << 0 << endl;
//     return 0;
// }
//     long long total=0;
//     int i=0;int j=0;
//     while(i<a.size() and j<b.size()){
//         if(a[i]>b[j]){
//             j++;
//         }
//         else if(a[i]<b[j]){
//             i++;
//         }
//         else{
//             int number=a[i];
//             long long c1 =0;
//             while(number==a[i] && i<a.size()){
//                 i++;
//                 c1++;
//             }
//             long long c2=0;
//             while(number==b[j] && j<b.size()){
//                 j++;
//                 c2++;
//             }
//             total+=c1*c2;
//         }
//     }
//     cout<<total<<endl;
//     return 0;
// }


// segment with good sum

// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int n;
//     long long s;
//     cin>>n>>s;
//     vector<int> vec(n);
//     for(int i=0;i<n;i++){
//         cin>>vec[i];
//     }
//     int j=0;
//     int maximum=0;
//     long long currsum=0;
//     for(int i=0;i<n;i++){
//         currsum+=vec[i];
//         while(currsum>s and j<n){
//             currsum-=vec[j];
//             j++;
//         }
//         if(currsum<=s){
//             maximum=max(maximum,i-j+1);
//         }
//     }
//     cout<< maximum<<endl;
//     return 0;
// }


// SEGMENT WITH BIGSUM

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n;
//     long long s;
//     cin>>n>>s;
//     vector<int> vec(n);
//     for(int i=0;i<n;i++){
//         cin>>vec[i];
//     }
//     int minimum = INT_MAX;
//     int j=0;
//     long long csum=0;
//     for(int i=0;i<n;i++){
//         csum+=vec[i];
//         if(csum>=s){
//             while(j<n and csum>=s){
//                 minimum = min(minimum,i-j+1);
//                 csum-=vec[j];
//                 j++;
//             }
//         }
//     }
//     cout<<minimum<<endl;
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n;
//     long long s;
//     cin>>n>>s;
//     vector<int> dataArr(n);
//     for(int i=0;i<n;i++){
//         cin>>dataArr[i];
//     }
//     int j=0;
//     int total=0;
//     long long csum=0;
//     for(int i=0;i<n;i++){
//         csum+=dataArr[i];
//         if (csum>=s){
//             while(csum>=s and j<=i){
//                 total+=(i+1)-(i-j+1)+1;
//                 csum-=dataArr[j];
//                 j++;
//             }
//         }
//     }
//     cout<<total<<endl;
//     return 0;
// }

// CELlelular network

// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int c,t;
//     cin>>c>>t;
//     vector<int> cities(c);
//     vector<int> towers(t);
//     for(int i=0;i<c;i++){
//         cin>>cities[i];
//     }
//     for(int i=0;i<t;i++){
//         cin>>towers[i];
//     }
//     sort(cities.begin(),cities.end());
//     sort(towers.begin(),towers.end());
//     int i=0;
//     int j=0;
//     int minimaxdist = 0;
//     while(i<c && j<t){
//         int tempdiff = abs(towers[j]-cities[i]);
//         while(j+1<t && tempdiff>=abs(towers[j+1]-cities[i])){
//             tempdiff = abs(towers[j+1]-cities[i]);
//             j++;
//         }
//         minimaxdist = max(minimaxdist,tempdiff);
//         i++;
//     }
//     cout<<minimaxdist;
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int n, q;
//         cin>>n>>q;
//         vector<int> dataArr(n);
//         for(int i=0;i<n;i++){
//             cin>>dataArr[i];
//         }
//         // prefixing
//         for(int i=1;i<n;i++){
//             dataArr[i]+=dataArr[i-1];
//         }
//         while(q--){
//             int l,r,k;
//             cin>>l>>r>>k;
//             int segmentsum = dataArr[r-1];
//             if(l-2>=0){
//                 segmentsum-=dataArr[l-2];
//             }
//             int result = dataArr[dataArr.size()-1] - segmentsum;
//             result+=k*(r-l+1);
//             if(result & 1==1){
//                 cout<<"yes"<<endl;
//             }
//             else{
//                 cout<<"no"<<endl;
//             }
//         }
//     }
//     return 0;
// }

// they are everywhere
// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int n;
//     cin >> n;
//     string str;
//     cin >> str;

//     unordered_set<char> seti(str.begin(), str.end());
//     int uniquechar = seti.size(); // Total number of unique characters
//     int j = 0;
//     unordered_map<char, int> mp;
//     int size = INT_MAX;

//     for (int i = 0; i < n; i++) {
//         mp[str[i]]++;

//         while (mp.size() == uniquechar) {
//             size = min(size, i - j + 1); 
//             mp[str[j]]--;
//             if (mp[str[j]] == 0) {
//                 mp.erase(str[j]);
//             }
//             j++;
//         }
//     }

//     cout << size << endl;
//     return 0;
// }

// eating candies
// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases=1;
//     // cin>>cases;
//     while(cases--){
//         int n=3;
//         // cin>>n;
//         vector <int> weights = {10,30,10};
//         // for(int i=0;i<n;i++){
//         //     cin>>weights[i];
//         // }
//         int i=0;
//         int j=n;
//         int total=0;
//         int wb=0;
//         int wa=0;
//         int ta=0;
//         int tb=0;

//         while(i<j){
//             wa+=weights[i];
//             ta++;
//             while( i<j && wa>wb){
//                 j--;
//                 wb+=weights[j];
//                 tb++;
//             }
//             if(wa==wb){
//                 total = max(total,ta+tb);
//             }
//             i++;
//         }

//         cout<<total<<endl;
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int n;
//         cin>>n;
//         vector<int> dataArr(n);
//         for(int i=0;i<n;i++){
//             cin>>dataArr[i];
//         }
//         int i=0;int j=n-1;
//         int ti=dataArr[0];int tj=dataArr[n-1];
//         int total=0;
//         int ci=1;
//         int cj=1;
//         while(i<j){
//             if(ti==tj){
//                 total = max(total,ci+cj);
//             }
//             if(tj>=ti){
//                 ti+=dataArr[i];
//                 ci++;
//                 i++;
//             }
//             else{
//                 tj+=dataArr[j];
//                 cj++;
//                 j--;
//             }
//         }
//         cout<<total<<endl;
//     }
//     return 0;
// }



