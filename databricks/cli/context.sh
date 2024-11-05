context() {
    databricks metastores current $@
}
metastore() {
    context | jq -r .metastore_id
}

$@
