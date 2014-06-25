#-*- coding: UTF-8 -*-

# 1，先添加所有城市的node，然后，添加所有的trend的node，两类node最好是有所区别
# 2，之后遍历每个城市中的10个trend，画出edge
# 3，保存图片and 生成gexf导入到gephi

import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

f=file("trend_name.txt")
data=json.load(f)
G=nx.DiGraph()
#cities=[]
#trend=[]
#edges=[]
for (k,v) in data.items():
	#print k
	#print v
	G.add_node(k,size=100)
	#cities.append(k)
	#G[k]['color']='y'
	for i in v:
		G.add_node(i,size=10)
		#trend.append(i)
		G.add_edge(i,k)
		#edges.append(zip(k,i))
#print G.nodes()

#a=150*np.ones([len(trend),])
plt.figure()
#nx.draw_networkx_nodes(G,nodelist=cities,node_color='b')
#nx.draw_networkx_nodes(G,nodelist=trend,node_color='r',node_size=a)
print G.nodes()
print type(G.edges())
print G.edges()
nx.draw(G,node_color='y',node_size=50)
nx.write_gexf(G,'cities_trend.gexf')
#nx.draw_networkx_nodes(cities,pos=nx.spring_layout(G),node_size=300,node_color='r')
plt.show()
f.close()