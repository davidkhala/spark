
# [Task](https://docs.databricks.com/en/jobs/index.html#what-is-a-task)
A task represents a unit of logic(最小业务逻辑单元) in a job.
- task scope is isolated

A task can be
- A notebook
- A JAR
- A SQL query
- A DLT pipeline
- **Another job**: choreography
- **Control flow tasks**: ochestrate


## Notebook
用户可以在Notebook中编写Python命令，编辑命令，并执行命令，获得输出的结果，并可以对结果进行可视化处理，
- 类似Jupiter Notebook
