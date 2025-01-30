# `SparkContext`
- Initialized by default as `sc`
- Use RDD API only.

`sc.master`
- `local[*,4]`: 
  - `local` mode: Spark runs on a single machine without connecting to a cluster
  - asterisk `*`: use all available CPU cores
  - `4`: maximum number of threads