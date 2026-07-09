# Extrait de configuration Deployment Kubernetes (YAML)
# Deployment odoo-web
apiVersion: apps/v1
kind: Deployment
metadata:
  name: odoo-web
spec:
  replicas: 4
  template:
    spec:
      containers:
      - name: odoo
        image: custom-odoo-prod:17.0
        env:
        - name: HOST
          value: postgres-db-service
        - name: REDIS_HOST
          value: redis-session-service
        resources:
          limits:
            cpu: "2"
            memory: 4Gi
          requests:
            cpu: "500m"
            memory: 2Gi
