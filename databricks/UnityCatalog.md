# Unity Catalog
>
> Unity Catalog is not available for feature tier STANDARD_TIER

- [Open source on Github](https://github.com/unitycatalog/unitycatalog)
  - Maturiy: Sandbox
  - Governance: LF AI & Data

[feature enable](https://docs.databricks.com/en/data-governance/unity-catalog/enable-workspaces.html)

## [Type](https://docs.databricks.com/en/catalogs/index.html#catalog-types)

- **Workspace catalog**: default catalog in all new workspaces.
  - Auto provision requires Unity Catalog enabled before workspace provision
  - Access: All users in your workspace have access to it
  - Recommended place for users to manage data objects
  - ?aws is an exception

## Metastores

A metastore is the top-level container for catalog in Unity Catalog. Within a metastore, Unity Catalog provides a 3-level namespace for organizing data: [catalogs](./DBO.md#catelog) > [schemas](./DBO.md#schema) > tables / views.

By default, the **Metastore Admin** is undefined (shown as **System user**)

- It is not related to any workspace principal/identity
- It is not managed in workspace console. It is managed in **Account Console** > **Catalog**
  - [Azure](https://accounts.azuredatabricks.net/data)
