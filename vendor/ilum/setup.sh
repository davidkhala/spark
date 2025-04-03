set -e
namespace=${1:-ilum}
register() {
  # Register the repository
  helm repo add ilum https://charts.ilum.cloud
  helm repo update
}
install() {
  # you need a k8s cluster
  helm install ilum ilum/ilum -n $namespace
}
setup-sql() {
  # Enable SQL
  update --set ilum-sql.enabled=true --set ilum-core.sql.enabled=true
}
setup-metastore() {
  # Enable Table Explorer (Hive Metastore)
  # TODO To be fixed by official
  # sql module will be enabled by default
  update --set ilum-hive-metastore.enabled=true --set ilum-core.hiveMetastore.enabled=true
}
setup-lineage() {
  update --set global.lineage.enabled=true --set ilum-marquez.web.enabled=true
  kubectl port-forward svc/ilum-marquez-web 9444:9444
}
update() {
  helm upgrade ilum ilum/ilum -n $namespace $@
}
expose() {
  kubectl port-forward svc/ilum-ui 9777:9777 -n $namespace
  kubectl port-forward svc/ilum-jupyter 8888:8888 -n $namespace
}
open() {
  xdg-open http://localhost:31777
}
uninstall() {
  helm uninstall ilum -n $namespace
  # TODO leakage To be fixed by official
  kubectl delete service ilum-hive-metastore
  kubectl delete pvc --all -n $namespace
}

"$@"
