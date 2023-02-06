public HashMap<Vertex<V>,Integer> ShortestPathSearch(Vertex<V> s){
    HashMap<Vertex<V>,Integer> visited = new HashMap<>();
    HeapAdaptablePriorityQueue<Integer,Vertex<V>> unvisited = new
    HeapAdaptablePriorityQueue<>();
    
    HashMap<Vertex<V>,HeapAdaptablePriorityQueue.AdaptableEntry<Integer,Vertex<V>>>
    v2pos = new HashMap<>();
    for (Vertex<V> v: vertices){
    if(v==s){
    v2pos.put(v, unvisited.insert(0, v));
    }
    else{
    v2pos.put(v,unvisited.insert(Integer.MAX_VALUE,v));
    }
    }
    while (unvisited.isEmpty()==false){
    Vertex<V> curV = unvisited.min().v;
    Integer curD = unvisited.min().k;
    visited.put(curV, curD);
    unvisited.removeMin();
    for(Vertex<V> u:curV.outgoing.keySet()){
    if(!visited.containsKey(u)){
    if(v2pos.get(u).k > curD + getEdge(curV,u).element){
    unvisited.replaceKey(v2pos.get(u),curD +
    getEdge(curV,u).element);
    }
    }
    }
    }
    return visited;
    }