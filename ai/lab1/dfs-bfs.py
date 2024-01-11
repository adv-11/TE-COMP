#dfs 

graph = { 
    'A' : ['E' , 'B'],
    'B' : ['C' , 'D' , 'A'],
    'C' : ['E' , 'D'],
    'D' : ['C' , 'B'],
    'E' : ['A', 'C']
}
visited = set()

def dfs (visited , graph , s):
    
    if s not in visited:
        print(s)
        visited.add(s)
        
        for child in graph[s]:
                dfs(visited , graph , child)
            
print('dfs:')            
dfs(visited , graph , 'A')

#bfs

vis =[]
queue = []

def bfs(vis , graph , s):
    
    vis.append(s)
    queue.append(s)
    
    while queue :
        element = queue.pop(0)
        print(element)
        
        for child in graph[element]:
            if child not in vis:
                vis.append(child)
                queue.append(child)
                

print('bfs:')            
bfs(vis , graph , 'A')
    
    