class MyHashSet {

    boolean ha[][];
    public MyHashSet() {
        ha = new boolean[1000][];
    }

    private int primaryha(int key) {
        return key% 1000;
    }

    private int secondaryha(int key) {
        return key/ 1000;
    }
    
    public void add(int key) {
        int pri = primaryha(key);
        int sec = secondaryha(key);
        if(ha[pri]== null){
            if(pri == 0) {
                ha[pri] = new boolean[1000+1];
            }
            else {
                ha[pri] = new boolean[1000];
            }
        }
        ha[pri][sec] = true;
    }
    
    public void remove(int key) {
        int pri = primaryha(key);
        int sec = secondaryha(key);
        if(ha[pri] != null) {
            ha[pri][sec] = false;
        }
    }
    
    public boolean contains(int key) {
        int pri = primaryha(key);
        int sec = secondaryha(key);
        if(ha[pri] != null)
            return ha[pri][sec];
        return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */