pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-cicd-project .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker stop my-cicd-container || true
                docker rm my-cicd-container || true
                docker run -d --name my-cicd-container -p 8080:80 my-cicd-project
                '''
            }
        }
    }
}
