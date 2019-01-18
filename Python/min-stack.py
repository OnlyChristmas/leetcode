'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''


# 构造基础类和基础操作的时候，使用多个栈以保证时效性

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 直接建立两个栈，每次在增添、删除元素的时候，挑选出最小的，如不是最后对所有元素一起排序，提高效率
        self.data = []
        self.min = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if not self.min or self.min[-1] >= x:   # 注意将相同的最小元素都添加进去，否则经过pop函数之后，有可能出错。
            self.min.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if self.data:
            if self.data[-1] == self.min[-1]:
                self.min.pop()
            self.data.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
