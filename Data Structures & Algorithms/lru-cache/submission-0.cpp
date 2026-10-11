struct Node {
    int key;
    int val;
    Node *next;
    Node *prev;
    Node() : key(-1), val(-1), next(nullptr), prev(nullptr) {}
    Node(int x) : key(x), val(-1), next(nullptr), prev(nullptr) {}
    Node(int x, int y) : key(x), val(y), next(nullptr), prev(nullptr) {}
};

class LRUCache {
public:
    int cap;
    std::unordered_map<int, Node *> cache;
    Node* left;
    Node* right;


    LRUCache(int capacity) {
        cap = capacity;
        left = new Node();
        right = new Node();
        left->next = right;
        right->prev = left;
    }

    void remove(Node *node) {
        Node *prev = node->prev;
        Node *next = node->next;
        prev->next = next;
        next->prev = prev;
    }

    void insert(Node *node) {
        Node *prev = right->prev;
        prev->next = node;
        node->prev = prev;
        node->next = right;
        right->prev = node;

    }

    int get(int key) {
        if (!cache.count(key)) {
            return -1;
        }

        Node *node = cache[key];
        remove(node);
        insert(node);

        return node->val;
    }

    void put(int key, int value) {
        Node *node = new Node(key, value);

        if (cache.count(key)) {
            Node *existing = cache[key];
            remove(existing);
            delete existing;
        }

        cache[key] = node;
        insert(node);

        if (cache.size() > cap) {
            Node *last = left->next;
            cache.erase(last->key);
            remove(last);
            delete last;
        }

    }
};
