# Data Lineage


## Limit
- Lineage is computed on a one-year rolling window

## Table lineage

## Column lineage 
- Column lineage is supported only when both the source and target are referenced by table name
  - case `select * from delta."s3://<bucket>/<path>"` is not supported
