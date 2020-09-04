docker build . -t "gcr.io/sym-bizops-bots/public-housekeeper-prod:1.0.0"
docker push "gcr.io/sym-bizops-bots/public-housekeeper-prod:1.0.0"

kubectl apply -f ./deployment.yaml