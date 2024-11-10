# Unity Catalog
> Unity Catalog is not available for feature tier STANDARD_TIER
- [Open source on Github](https://github.com/unitycatalog/unitycatalog)
    - Maturiy: Sandbox
    - Governance: LF AI & Data

## Metastores
A metastore is the top-level container for catalog in Unity Catalog. Within a metastore, Unity Catalog provides a 3-level namespace for organizing data: [catalogs](./DBO.md#catelog) > [schemas](./DBO.md#schema) > tables / views.

By default, the **Metastore Admin** is a pseudo **System user**
- It is not related to any workspace principal/identity
- It is not managed in workspace console. It is managed in **Account Console**
    - [Azure](https://github.com/davidkhala/azure-utils/blob/main/data/bricks/README.md)


