install() {
  curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sudo sh
}
login() {
  local url=$1 # workspace url
  local pat=$2 # Personal access token

  databricks configure --token --host https://$url <<<$pat
}
whoami() {
  databricks current-user me
}

$@
