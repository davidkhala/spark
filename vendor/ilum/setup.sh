set -e
namespace=${1:-default}
install(){
  helm repo add ilum https://charts.ilum.cloud
  # you need a k8s cluster 
  helm install ilum ilum/ilum
}
setup-sql(){
  # Enable SQL
  helm upgrade ilum ilum/ilum --set ilum-sql.enabled=true --set ilum-core.sql.enabled=true
}
setup-metastore(){
  # Enable Table Explorer (Hive Metastore)
  # TODO To be fixed by official
  helm upgrade ilum ilum/ilum --set ilum-hive-metastore.enabled=true --set ilum-core.hiveMetastore.enabled=true
}
setup-lineage(){
  helm upgrade ilum ilum/ilum --set global.lineage.enabled=true --set ilum-marquez.web.enabled=true
  kubectl port-forward svc/ilum-marquez-web 9444:9444
}

expose(){
    kubectl port-forward svc/ilum-ui 9777:9777 -n $namespace
    kubectl port-forward svc/ilum-jupyter 8888:8888 -n $namespace
}
open(){
  xdg-open http://localhost:31777
}
uninstall(){
  helm uninstall ilum
}

"$@"
