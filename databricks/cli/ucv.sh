# Unity Catalog volumes
set -e
create-managed() {
    databricks volumes create $catalog $schema $volume MANAGED

    databricks grants update volume $catalog.$schema.$volume --json '{"changes": [{"principal": "account users", "add": ["READ_VOLUME"]}]}'
}

$@
