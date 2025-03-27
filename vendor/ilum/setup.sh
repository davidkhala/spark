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
  echo "You can use default credentials admin:admin to log in."
  xdg-open http://localhost:31777
}
"$@"
