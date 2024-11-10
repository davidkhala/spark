[DataGrip integration](https://github.com/davidkhala/code-dev-collection/blob/main/jetbrain/dataGrip/databricks.md)



- [Samples](./samples.md)

# [Concept: What is Delta](https://docs.databricks.com/en/introduction/delta-comparison.html)

## [Delta Lake](https://github.com/delta-io)
open-source data management for the lakehouse
- Adding an ACID transactional storage layer on top of object storage
- data versioning, rollback
- handle both batch and streaming data in a unified way
- provide table abstraction for SQL and DataFrame API
- contributed by Databricks

### DeltaLogs
[Delta Lake transaction Log](https://github.com/delta-io/delta/blob/master/PROTOCOL.md)
- **Table Ledger**: single source of truth trackcing table changes
- guarantees atomicity of [Delta Lake](#delta-lake)

## Delta Table
a feature of [Delta Lake](#delta-lake)
- Stored in the Delta Lake format


## Delta Live Tables (DLT): Data pipeline framework
DLT is not a table
- It manage the data flow, task orchestration, **data quality and error handling**
- It offers declarative pipeline development
- It contains pipeline, the main unit of execution
- It manages many [Delta tables](#delta-table)
- is proprietary

## Delta Sharing
An open protocol for secure data sharing

## Delta engine
A query optimizer
- Proprietary to Databricks
- for performance of Spark SQL, Databricks SQL and Dataframe operations
- apply [push down](https://github.com/davidkhala/data-integration/wiki/push-down) design


