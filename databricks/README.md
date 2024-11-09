
[DataGrip integration](https://github.com/davidkhala/code-dev-collection/blob/main/jetbrain/dataGrip/databricks.md)

## Built-in Samples

Delta live tables
- In `Data Engineering/Delta Live Tables`
  - You cannot attach it to your existing compute
  - New Job Compute with massive cost will be created for it.
  - The same job will resuse compute used in previous run if there is no setting change.
  - These type of Job Compute is managed by Databricks
    - > Error: dlt prefixed spark images cannot be used outside of the Delta Live Tables service
  - To save compute cost, configure 
    - In Compute section
      - `Cluster mode` = `Fixed size`, 
      - `Workers` = 1
      - Don't enable Photon Acceleration
    - In Advanced section
      - `Worker type` = `Standard_F4`
Datasets
- In Unity Catalog, Catalog `Shared/samples`
  - It is available only when warehouse is started
