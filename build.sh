docker build -t hw1_grading .
docker tag hw1_grading:latest 283760322754.dkr.ecr.us-east-1.amazonaws.com/hw1_grading:latest
docker push 283760322754.dkr.ecr.us-east-1.amazonaws.com/hw1_grading:latest
