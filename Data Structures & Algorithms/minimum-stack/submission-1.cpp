class MinStack {
    
public:
    std::stack<long> stack;
    std::stack<long> minStack;

    MinStack() {

    }

    void push(int val) {
        stack.push(val);

        if (minStack.empty() || val < minStack.top()) {
                minStack.push(val);
        } else minStack.push(minStack.top());
    }


    void pop() {
        stack.pop();
        minStack.pop();
    }

    int top() {
        return stack.top();
    }

    int getMin() {
        return minStack.top();
    }
};
