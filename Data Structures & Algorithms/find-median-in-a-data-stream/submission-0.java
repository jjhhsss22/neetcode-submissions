class MedianFinder {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    public MedianFinder() {

    }

    public void addNum(int num) {
        maxHeap.add(num);

        if (maxHeap.size() - minHeap.size() > 1 || !minHeap.isEmpty() && maxHeap.peek() > minHeap.peek()) {
            minHeap.add(maxHeap.poll());
        }

        if (minHeap.size() - maxHeap.size() > 1) {
            maxHeap.add(minHeap.poll());
        }
    }

    public double findMedian() {
        if (minHeap.size() == maxHeap.size()) {
            return (minHeap.peek() + maxHeap.peek()) / 2.0;
        } else if (minHeap.size() > maxHeap.size()) {
            return minHeap.peek();
        } else return maxHeap.peek();
    }
}
