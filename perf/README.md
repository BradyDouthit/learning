# Performance
Taking some time to get a better handle on performance by comparing languages and common techniques to speed up algorithms. While not a perfect analog for the real world (since it is lacking real complexity), each script will read in a text file and calculate the word frequency. The text file is not in this repo because it would be too big but any text file will do.

I write a lot of JS so I start there writing the algorithm in a way that is most reasonable to a person, rather than focusing on performance. From there I simply iterate to make it faster. Each step is a new script.

## Benchmark Results

| Implementation | Mean Time | Std Dev | Range | Runs |
|---------------|-----------|---------|-------|------|
| Go Concurrent | 21.2 ms | 1.0 ms | 19.6 ms … 25.3 ms | 108 |
| Go (compiled binary) | 28.4 ms | 0.9 ms | 26.4 ms … 31.3 ms | 85 |
| Node.js | 131.3 ms | 3.7 ms | 127.4 ms … 145.4 ms | 19 |

### Summary

The Go Concurrent implementation uses goroutines and channels to split the word array in half and process each chunk in parallel, achieving ~25% faster performance than the sequential Go version. Unsurprisingly, the compiled Go binary substantially faster than the Node.js implementation for the word frequency calculation task. 
