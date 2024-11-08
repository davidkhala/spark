# Data Lineage


## [Limit](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/data-lineage#limitations)
- Lineage is computed on a one-year rolling window
- lineage is not captured when:
  - table/view, schema or catalog is renamed
  - you use Spark SQL dataset checkpointing
  - you want to cover Global temp views, Stack function
  - you want to cover tables under `system.information_schema`

## Table lineage

## Column lineage 
- Column lineage is supported only when both the source and target are referenced by table name
  - case `select * from delta."s3://<bucket>/<path>"` is not supported
