# Unity Catalog
catelogs() {
    databricks catalogs list --include-browse
}
schemas() {
    local catalog=${1:-$catalog}
    databricks schemas list $catalog --include-browse
}
allowlist() {
    # artifact allowlist
    echo ">>> init script"
    databricks artifact-allowlists get INIT_SCRIPT

    echo ">>> JAR"
    databricks artifact-allowlists get LIBRARY_JAR 
    
    echo ">>> maven"
    databricks artifact-allowlists get LIBRARY_MAVEN

}
$@
