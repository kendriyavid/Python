
// // // tasks and deadlines
// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // int main(){
// // //     int n;
// // //     cin>>n;
// // //     vector<pair<int,int>> vec(n);
// // //     for(int i=0;i<n;i++){
// // //         cin>>vec[i].first>>vec[i].second;
// // //     }
// // //     sort(vec.begin(),vec.end());
// // //     long long ctime=0;
// // //     long long profit=0;
// // //     for(int i=0;i<n;i++){
// // //         ctime+=vec[i].first;
// // //         profit = profit+(vec[i].second-ctime);
// // //     }
// // //     cout<<profit<<endl;
// // //     return 0;
// // // }

// // #include <bits/stdc++.h>
// // using namespace std;

// // int main(){
// //     int n;
// //     cin>>n;
// //     vector<int> vec(n);
// //     for(int i=0;i<n;i++){
// //         cin>>vec[i];
// //     }
// //     int i=0;
// //     int j=0;
// //     int t1=0;
// //     int t2=0;
// //     while(i<n && j>=0){
// //         if(t1>t2){
            
// //         }
// //         else{
            
// //         }

// //     }
// //     return 0;
// // }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     vector<int> vec(n);
//     vector<int> vec2(n);
//     for(int i=0;i<n;i++){
//         cin>>vec[i];
//     }
//     vector<int> stack;
//     for(int i=n-1;i>=0;i--){
//         while(stack.size()!=0 && stack[stack.size()-1]<vec[i]){
//             stack.pop_back();
//         }
//         if(stack.size()==0){
//             vec2[i]=-1;
//         }
//         else{
//             vec2[i] = stack.back();
//         }
//         stack.emplace_back(vec[i]);
//     }

//     int count=0;
//     for(int i=1;i<vec2.size();i++){
//         if(vec2[i]!=-1 && vec2[i]!=vec2[i-1]){
//             count++;
//         }
//     }

//     if(count<2){
//         cout<<false<<endl;
//     }
//     else{
//         cout<<true<<endl;
//     }
//     cout<<count;
//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int a,b,c;
//         cin>>a>>b>>c;
//         int anna=0;
//         int katie=0;
//         int ah;
//         if(c%2!=0){
//             ah =int(c/2)+1;
//         }
//         else{
//             ah = c/2;
//         }
//         anna = ah+a;
//         katie = b+ c-ah;
//         cout<<anna<<" "<<katie<<endl;
//         if(anna>katie){
//             cout<<"First"<<endl;
//         }
//         else if (anna<=katie){
//             cout<<"Second"<<endl;
//         }
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int cases;
//     cin >> cases;
//     while (cases--) {
//         int n;
//         cin >> n;  // Read the size of the array
//         vector<int> vec(n);
//         for (int i = 0; i < n; i++) {
//             cin >> vec[i];
//         }
        
//         int ec = 0, oc = 0; // Initialize even and odd counters
//         for (int i = 0; i < n; i++) {
//             if (vec[i] % 2 == 0) {
//                 ec++;
//             } else {
//                 oc++;
//             }
//         }
//         // 
//         if (ec == 0) {
//             if (oc % 2 != 0) {
//                 cout << "NO\n";
//             } else {
//                 cout << "YES\n";
//             }
//         } else if (oc % 2 == 0) {
//             cout << "YES\n";
//         } else {
//             cout << "NO\n";
//         }
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int cases;
//     cin >> cases;
//     while (cases--) {
//         int n;
//         cin >> n;
//         vector<int> vec(n);
//         for (int i = 0; i < n; i++) {
//             cin >> vec[i];
//         }
//         int mindiff = INT_MAX;
//         bool issorted = true;

//         for (int i = 1; i < n; i++) {
//             if (vec[i] - vec[i - 1] >= 0) {
//                 mindiff = min(mindiff, vec[i] - vec[i - 1]);
//             } else {
//                 issorted = false;
//                 break;
//             }
//         }

//         if (!issorted) {
//             cout << 0 << endl;
//         } else {
//             cout << (mindiff / 2) + 1 << endl;
//         }
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int n,k;
//         cin>>n>>k;
//         vector<int> vec(k);
//         for(int i=0;i<n;i++){
//             cin>>vec[i];
//         }
//         int last = 0;
//         int count=1;
//         int lcount=1;
//         sort(vec.begin(),vec.end());
//         for(int i=1;i<n;i++){
//             if(abs(vec[last]-vec[i])>k){
//                 lcount=1;
//             }
//             else{
//                 lcount++;
//             }
//             count = max(count,lcount);

//         }
//         cout<<n-lcount<<endl;
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
//         vector<char> vec(n);
//         for(int i=0;i<n;i++){
//             cin>>vec[i];
//         }
//         int count=1;
//         int maxconsecutive=1;
//         for(int i=1;i<n;i++){
//             if(vec[i]==vec[i-1]){
//                 count++;
//             }
//             else{
//                 count = 1;
//             }
//             maxconsecutive = max(maxconsecutive,count);

//         }
//         cout<<maxconsecutive+1<<endl;
//     }
//     return 0;
// }

// 

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int n,k;
//         cin>>n>>k;
//         vector<int> vec(n);
//         for(int i=0;i<n;i++){
//             cin>>vec[i];
//         }
//         //sorting
//         sort(vec.begin(),vec.end(),greater<int>());
//         vector<int> prefix(n);
//         prefix[0] = vec[0];
//         for(int i=1;i<n;i++){
//             prefix[i] = prefix[i-1]+vec[i];
//         }
//         auto value = lower_bound(vec.begin(), vec.end(), k)-prefix.begin();
//         if(prefix[value]==k){
//             cout<<0<<endl;
//         }
//         else if (prefix[value]>k){
//             cout<<k-prefix[value-1]<<endl;
//         }
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
//         vector<int> vec(n);
//         for(int i=0;i<n;i++){
//             cin>>vec[i];
//         }
//         map<int,int> mp;
//         // parsing making map
//         for(int i=0;i<n;i++){
//             mp[vec[i]]++;
//         }
//         int alice=0;
//         bool alturn=true;
//         for(auto &it:mp){
//             if(alturn){
//                 if(it.second ==1){
//                     alice+=2;
//                 }
//                 else{
//                     alice++;
//                 }
//                 alturn = false;
//             }
//             else{
//                 alturn = true;
//                 continue;
//             }
//         }
//         cout<<alice<<endl;
//     }
//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int t;
//     cin >> t;
//     while(t--) {
//         int n;
//         cin >> n;
//         vector<int> marbles(n);
//         map<int, int> color_count;
        
//         for(int i = 0; i < n; i++) {
//             cin >> marbles[i];
//             color_count[marbles[i]]++;
//         }

//         priority_queue<int> pq;
        
//         for(auto& entry : color_count) {
//             pq.push(entry.second);
//         }

//         int alice_score = 0;
//         bool alice_turn = true;
        
//         while(!pq.empty()) {
//             int count = pq.top();
//             pq.pop();
            
//             if(alice_turn) {
//                 alice_score++;
//                 if(count==1) {
//                     alice_score++;
//                 }
//             }
//             if(count > 1) {
//                 pq.push(count - 1);  // Bob will leave some marbles
//             }
//             alice_turn = !alice_turn;
//         }

//         cout << alice_score << endl;
//     }

//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int t;
//     cin >> t;
//     while(t--) {
//         int n;
//         cin >> n;
//         vector<int> marbles(n);
//         map<int, int> color_count;
        
//         for(int i = 0; i < n; i++) {
//             cin >> marbles[i];
//             color_count[marbles[i]]++;
//         }

//         priority_queue<int> pq;
        
//         for(auto& entry : color_count) {
//             pq.push(entry.second);
//         }

//         int alice_score = 0;
//         bool alice_turn = true;
        
//         while(!pq.empty()) {
//             int count = pq.top();
//             pq.pop();
            
//             if(alice_turn) {
//                 alice_score++;
//                 if(count == 1) {
//                     alice_score++;
//                 }
//                 if(count > 1) {
//                     pq.push(count - 1);
//                 }
//             }
//             else {
//                 if(count > 1) {
//                     pq.push(count - 1);
//                 }
//             }
            
//             alice_turn = !alice_turn;
//         }

//         cout << alice_score << endl;
//     }

//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int t;
//     cin >> t;
//     while(t--) {
//         int n;
//         cin >> n;
//         vector<int> marbles(n);
//         map<int, int> color_count;

//         for(int i = 0; i < n; i++) {
//             cin >> marbles[i];
//             color_count[marbles[i]]++;
//         }

//         priority_queue<pair<int, int>> pq;
        
//         for(auto& entry : color_count) {
//             pq.push({entry.second, entry.first});
//         }

//         int alice_score = 0;
//         bool alice_turn = true;
        
//         while(!pq.empty()) {
//             int count = pq.top().first;
//             int color = pq.top().second;
//             pq.pop();
            
//             if(alice_turn) {
//                 alice_score++;
//                 if(count == 1) {
//                     alice_score++;
//                 }
//                 if(count > 1) {
//                     pq.push({count - 1, color});
//                 }
//             }
//             else {
//                 if(count > 1) {
//                     pq.push({count - 1, color});
//                 }
//             }
            
//             alice_turn = !alice_turn;
//         }

//         cout << alice_score << endl;
//     }

//     return 0;
// }


// prime factorization
// #include<bits/stdc++.h>
// using namespace std;
// int main(){
//     int n;
//     cin>>n;
//     map<int,int> mp;
//     for(int i=2;i*i<=n;i++){
//         if(n%i==0){
//             int count=0;
//             while(n%i==0){
//                 count++;
//                 n/=i;
//             }
//             mp[i] = count;
//         }
//     }
//     if(n>1){
//         mp[n]=1;
//     }    

//     return 0;
// }

// binary exponentiation
// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n,power;
//     cin>>n>>power;
//     int result=1;
//     while(power!=0){
//         if(power%2!=0){
//             result = power*result;
//             power--;
//         }
//         else{   
//             result = result*result;
//             power/=2;
//         }
//     }
//     cout<<result;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int gcd(int  a,int b){
//     while(b!=0){
//         int temp = b;
//         b = a % b;
//         a = temp;
//     }
//     return a;
// }

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int a,b;
//         cin>>a>>b;
//         long long multiplication = a*b;
//         long long greatest = gcd(a,b);
//         long long lcm = multiplication/greatest;
//         if(lcm==max(a,b)){
//             cout<<lcm*lcm<<endl;
//         }
//         else{
//             cout<<lcm<<endl;
//         }
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int t; // Number of test cases
//     cin >> t;
//     while (t--) {
//         int a, b;
//         cin >> a >> b;
        
//         long long x;
//         if()
//         long long x = 1LL * a * b;
        
//         // Since a < b < x is guaranteed, directly output x
//         cout << x << endl;
//     }
//     return 0;
// }
