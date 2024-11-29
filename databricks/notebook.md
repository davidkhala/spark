# Notebook
用户可以在Notebook中编写Python命令，编辑命令，并执行命令，获得输出的结果，并可以对结果进行可视化处理，
- 类似[Jupiter Notebook](https://github.com/davidkhala/AI/wiki/Jupyter-Notebook)
- 默认语言为Python，并支持Scala，R，[SQL](#sql-in-notebook)

Give the notebook id (presented as `object_id` or `resource_id` in a value format of `3674839001807684`), there is no table/view to query the notebook path
- This uglifies notebook visualization in Microsoft Purview lineage canvas
- Solution [example](https://github.com/davidkhala/databricks-common/blob/main/workspace/path.py)
  - You might need to create a *Global Temp View* or table (for serverless compute) for SQL query, or
  - **Recommend** You can get it by sdk

## SQL in Notebook
aka. Spark SQL
- There is no data function to get current workspace id

## Public examples
- [Load external notebook](https://docs.databricks.com/en/notebooks/index.html#how-to-import-and-run-example-notebooks)
- https://docs.databricks.com/en/_extras/notebooks/source/mlflow/mlflow-quick-start-python.html
- https://www.databricks.com/notebooks/gcp-qs-notebook.html
- https://analyticjeremy.github.io/Databricks_Examples/