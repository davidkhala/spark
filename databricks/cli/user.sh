group() {
    databricks groups list -o json $@
}
admins() {
    # group "admins"
    group | jq -r '.[] | select(.displayName=="admins") | .id'
}
users() {
    # group "users"
    group | jq -r '.[] | select(.displayName=="users") | .id'
}
whoami() {
    databricks current-user me
}
create-service-principal() {
    databricks service-principals create $@ | jq '{applicationId,id}'
}
list-service-principal() {
    databricks service-principals list -o json
}
$@
