if ($env:namespace) {
    $namespace = $env:namespace
} else {
    $namespace = "ilum"
}
Write-Output "using namespace $namespace"
function Register {
    # Register the repository
    helm repo add ilum https://charts.ilum.cloud
    helm repo update
}

function Install {
    # You need a k8s cluster
    helm install ilum ilum/ilum -n $namespace --create-namespace
}

function Enable-Sql {
    # Enable SQL
    Update --set ilum-sql.enabled=true --set ilum-core.sql.enabled=true
}

function Enable-Metastore {
    # Enable Table Explorer (Hive Metastore)
    # TODO To be fixed by official
    Update --set ilum-sql.enabled=true --set ilum-core.sql.enabled=true --set ilum-hive-metastore.enabled=true --set ilum-core.hiveMetastore.enabled=true 
}

function Enable-Lineage {
    Update --set global.lineage.enabled=true --set ilum-marquez.web.enabled=true
    kubectl port-forward svc/ilum-marquez-web 9444:9444 -n $namespace

}

function Update {
    # Use splatting for passing arguments to helm upgrade
    $params = @{}
    
    helm upgrade ilum ilum/ilum -n $namespace @params
}

function Expose {
    kubectl port-forward svc/ilum-ui 9777:9777 -n $namespace
    kubectl port-forward svc/ilum-jupyter 8888:8888 -n $namespace
}

function Open {
    Start-Process "http://localhost:31777"
}

function Uninstall {
    # TODO Leakage To be fixed by official
    # helm uninstall ilum -n $namespace
    # kubectl delete pvc gitea-shared-storage
    kubectl delete namespace $namespace
}


if ($args.Count -gt 0) {
    Invoke-Expression ($args -join " ")
}