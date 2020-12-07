#include<bits/stdc++.h>
using namespace std;
#define ll long long
const ll MAXN = 5e5+5;
//string s[50005];
string ans[500005];
string s;
int w;
void del_sp(int tot){  // 去首尾空格
    int len = s.size();
    int idx1 = 1,idx2 = 0;
    for(int i=0;i<len;i++){
        if(s[i]!=' '){
            idx1 = i;break;
        }
    }
    for(int i=len-1;i>=0;i--){
        if(s[i] != ' '){
            idx2 = i;break;
        }
    }
    string k = "";
    for(int i=idx1;i<=idx2;i++){
        k += s[i];
    }
    s = k;
}
int num = 0,all = 0;
string k = "";
void add(char c)  //添加字符
{
    k += c; //  <--this
    num++;
    if(num == w){   //  1.
        ans[++all] = k;
        //all++;
        k = "";
        num = 0;
    }
}
void enter(int h)    //2. 切行
{
    //cout<<h<<" ^ "<<endl;
    if(num!=0){
        ans[++all] = k;
        //all++;
    }
    //all++;
    ans[++all] = "";
    k = "";
    num = 0;
}
bool check_sp(int x,int idx)   //判空行
{
    for(int i=idx;i<s.size();i++){
        if(s[i] != ' ')return false;
    }
    return true;
}
int main()
{
    ios::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    cin>>w;
    getline(cin,s);
    int fg = 0,i=0;
    int flag = 0;// 0 段落  1 列表  3空行 上一行是什么
    while(getline(cin,s) != NULL){
        int len = s.size();
        if(check_sp(i,0)){ // 空行
            flag = 3;
            continue;
        }
        if(flag == 3&&fg){
            enter(i);
        }
 
        int flag2 = 0; // 本行是什么   1 列表  0 段落
        if(len>=2 && s[0] == '*' && s[1] == ' '){
            flag2 = 1;
            s = s.substr(2,len-2);
            if(flag == 1 && num!=0){
               // all++;
                ans[++all] = k;        //3.
               k = "";
                num = 0;
            }
            if(flag == 0 ){
                if(fg!=0)enter(i);
            }
            add('.');add('.');add('.');
        }
        else if(len >=2 && s[0] == ' ' && s[1] == ' '){
            if(flag == 1){ // 列表
                s = s.substr(2,len-2);
                flag2 = 1;
                if(num == 0){
                    add('+');add('+');add('+');
                }
            }
 
        }
 
        del_sp(i),len = s.size();
        if(flag == 0){
            if(flag2 == 0 && num!=0)add(' ');
        }
        if(flag == 1){
            if(flag2 == 0){
                enter(i);
            }
            if(flag2 == 1){
                if(num>3)add(' ');
            }
        }
        //cout<<i<<" * "<<flag<<" * "<<flag2<<endl;
        for(int j=0;j<len;j++){
            if(num == 0 && flag2 == 1){
                add('+');add('+');add('+');
            }
            if(flag2 == 0){
                if(num == 0 && s[j] == ' ')continue;
            }
            if(flag2 == 1){
                if(num == 3 && s[j] == ' ')continue;
            }
 
            add(s[j]);
        }
        flag = flag2;
        fg = 1;
    }
    if(num!=0){   //4.
        //all++;
        ans[++all] = k;
    }
    cout<<"------------"<<endl;
    for(int i=1;i<=all;i++){
        cout<<ans[i]<<endl;
    }
    cout<<all<<endl;
}
 
 
 
/*
4
asjcaojca
aaa
a
*/
 
/*
10
CSP
CSP is
a real realrealrealrealreal
     competition.
Come   and   join   us
*/
 
/*
10
* CSP
*   CSP is
  * a real
     competition.
* 
  * Come!   and   join.
*Tel:
* 12345
* 
*/
 
/*
4
* aaaa
*bbb
  ccc
* dd
    eee
*ff
*/