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
    local name=$1
    databricks service-principals create --active --display-name $name $@ | jq '{applicationId,id}' 

}
$@
