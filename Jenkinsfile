pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -c "import flask; print('Flask installation successful')"
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t my-python-app:latest .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop my-python-container || true
                    docker rm my-python-container || true

                    docker run -d \
                        --name my-python-container \
                        -p 5000:5000 \
                        my-python-app:latest
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                    sleep 5
                    curl http://localhost:5000
                '''
            }
        }
    }
}
