set -e
install(){
  helm repo add ilum https://charts.ilum.cloud
  # you need a k8s cluster 
  helm install ilum ilum/ilum
}
expose(){
    local namespace=${1:-default}
    kubectl port-forward svc/ilum-ui 9777:9777 -n $namespace
}
open(){
  
  xdg-open http://localhost:31777
}
with-SQL(){
  helm upgrade ilum ilum/ilum --set ilum-sql.enabled=true
  
}

"$@"
