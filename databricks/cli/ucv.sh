# Unity Catalog volumes
set -e
schema=${schema:-default}
catalog=${catalog:-$(sed 's/-/_/' <<<$workspace_name)}
create-managed() {
    local volume=$1
    databricks volumes create $catalog $schema $volume MANAGED

    databricks grants update volume $catalog.$schema.$volume --json '{"changes": [{"principal": "account users", "add": ["READ_VOLUME"]}]}'
}

volumes() {
    databricks volumes list $catalog $schema
}
$@
