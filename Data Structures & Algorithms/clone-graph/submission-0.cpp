/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        std::unordered_map<Node*, Node*> map;

        if (!node) {
            return nullptr;
        }

        return dfs(node, map);

    }

    Node* dfs(Node* node, std::unordered_map<Node*, Node*>& map) {
        
        if (map.count(node)) {
            return map[node];
        }

        Node* newNode = new Node(node->val);
        map[node] = newNode;

        for (auto neighbor : node->neighbors) {
            newNode->neighbors.push_back(dfs(neighbor, map));
        }

        return newNode;
    }
};
