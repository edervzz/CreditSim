- npm create vite@latest
- npm install bootstrap

  948022990339.dkr.ecr.us-east-2.amazonaws.com/creditsim-backend

docker build -t creditsim-backend .

docker tag creditsim-backend:latest 948022990339.dkr.ecr.us-east-2.amazonaws.com/creditsim-backend:latest

######################################################################################

aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 948022990339.dkr.ecr.us-east-2.amazonaws.com

Build y agrega tag
docker build -t 948022990339.dkr.ecr.us-east-2.amazonaws.com/creditsim-backend:latest .

docker push 948022990339.dkr.ecr.us-east-2.amazonaws.com/creditsim-backend:latest

Redeploy
aws apprunner start-deployment --service-arn arn:aws:apprunner:us-east-2:948022990339:service/creditsim-backend/1e5d80dbebbe4c5d9330cd97a73ab6aa --region us-east-2

######################################################################################

curl -X POST https://kbrh3u5p48.us-east-2.awsapprunner.com/simulate -H "Content-Type: application/json" -d "{\"credit_amount\":10000,\"annual_rate\":12,\"term\":6}"

######################################################################################

npm install

npm run build

aws s3 website s3://creditsim-frontend --index-document index.html --error-document index.html

crear bucket: aws s3 mb s3://creditsim-frontend --region us-east-2

aws s3 website s3://creditsim-frontend --index-document index.html --error-document index.html

aws s3 sync dist s3://creditsim-frontend

aws s3 cp dist s3://creditsim-frontend/ --recursive
