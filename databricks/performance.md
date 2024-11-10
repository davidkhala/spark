# Optimize methods
- Prewarm clusters
  - by using [Databricks Pool](https://docs.databricks.com/en/compute/pool-index.html)
  - target: reduce cluster start and auto-scaling times
- Prewarm caches
  - by running specific queries to initialize caches

# Benchmarks 
[Benchmark on aws](https://www.databricks.com/blog/2017/07/12/benchmarking-big-data-sql-platforms-in-the-cloud.html)
- TPC-DS v2.4 (1000 scale factor)
- aws machine
  - 44 vcpu, 336 GB memory
  - 11 r3.xlarge (1 driver, 10 workers) 
- Databricks Runtime 3.0