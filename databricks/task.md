
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

Give the notebook id (presented as `object_id` or `resource_id` in a value format of `3674839001807684`), there is no way to query back the notebook path
- This uglifies notebook visualization in Microsoft Purview lineage canvas
- You might need to create a dimentional table for query that information

### SQL in Notebook
- There is no data function to get current workspace id

### Public examples
- https://docs.databricks.com/en/_extras/notebooks/source/mlflow/mlflow-quick-start-python.html
- https://analyticjeremy.github.io/Databricks_Examples/
