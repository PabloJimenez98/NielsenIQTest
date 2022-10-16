pipeline {

    agent any
    stages {
        stage('Build') {
            steps {
                sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Test'
            }
        }
    }
}