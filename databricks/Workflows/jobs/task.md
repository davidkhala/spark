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

> It does not mean notebook is only a type of task. It means job task can refer to an existing notebook