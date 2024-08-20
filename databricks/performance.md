# Optimize methods
- Prewarm clusters
  - by using [Databricks Pool](https://docs.databricks.com/en/compute/pool-index.html)
  - target: reduce cluster start and auto-scaling times
- Prewarm caches
  - by running specific queries to initialize caches
