# [Databricks Widgets](https://docs.databricks.com/en/notebooks/widgets.html)
Widgets allow you to **add parameters** 
- to your reusable notebooks and dashboards
- by Databricks UI or widget API

keyword: "interactive execution"
## Create widgets using the UI
Select **Edit > Add widget**
- used in **SQL Editor** attached to SQL warehouse
## [Widgets API](https://docs.databricks.com/en/dev-tools/databricks-utils.html)
`dbutils.widgets.help()`
- Used in notebook attached to cluster
- Further advanced control(layout, plot), use [ipywidgets](https://docs.databricks.com/en/notebooks/ipywidgets.html)
