pipeline {
    agent any

    environment {
        IMAGE = 'parthikmanoj2/devops-app'
        DOCKERHUB = credentials('dockerhub-creds')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }

        stage('Build & Push') {
            steps {
                sh '''
                    docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .
                    echo "$DOCKERHUB_PSW" | docker login -u "$DOCKERHUB_USR" --password-stdin
                    docker push $IMAGE:$BUILD_NUMBER
                    docker push $IMAGE:latest
                '''
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
    }
}
