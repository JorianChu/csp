#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int NMAX = 2e5 + 10;
const int MOD = 1e9 + 7;
vector<int> edge[605];
vector<int> info[605];

struct Node
{
	vector<int> info;
	int time;
	int now_node;
	Node(vector<int> a,int b,int c):info(a),time(b),now_node(c){} 
};

int main(int argc, char const *argv[])
{
	int u,v;
	int n,m;
	scanf("%d%d",&n,&m);
	for(register int i = 0;i < m;i++)
	{
		scanf("%d%d",&u,&v);
		edge[u].push_back(v);
		edge[v].push_back(u);
	}
	for(register int i = 0;i < n;i++)
		info[i + 1].push_back(0);
	int t,k;
	scanf("%d%d",&t,&k);
	char ch;
	queue<Node>q;
	getchar();
	for(register int i = 0;i < k;i++)
	{
		int a = 0,b = 0,c = 0;
		ch = getchar();
		while(ch>='0'&&ch<='9'){
			//10*a+(ch-'0')
	        a=(a<<1)+(a<<3)+(ch^48);
	        ch=getchar();
    	}
    	ch = getchar();
		while(ch>='0'&&ch<='9'){
	        b=(b<<1)+(b<<3)+(ch^48);
	        ch=getchar();
    	}
    	if(ch != '\n')
    	{
    		ch = getchar();
			while(ch>='0'&&ch<='9'){
		        c=(c<<1)+(c<<3)+(ch^48);
		        ch=getchar();
	    	}
    	}
		while(!q.empty() && q.front().time + t <= b)
		{
			int now_t = q.front().time;
			u = q.front().now_node;
			vector<int> now_info = q.front().info;
			for(register int j = 0;j < edge[u].size();j++)
			{
				v = edge[u][j];
				if(now_info.size() > info[v].size() || (now_info.size() == info[v].size() && now_info[now_info.size() - 1] < info[v][info[u].size() - 1]))
				{
					info[v] = now_info;
					q.push(Node(info[v],now_t + t,v));
				}
			}
			q.pop();
		}
		if(c == 0)
		{
			printf("%d ",info[a].size());
			for(register int j = 0;j < info[a].size();j++)
				printf("%d%c",info[a][j],j == info[a].size()-1?'\n':' ');
		}
		else{
			info[a].push_back(c);
			q.push(Node(info[a],b,a));

		}
	}
	return 0;
}