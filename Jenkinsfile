pipeline {

    agent any
    stages {
        stage('Build') {
            steps {
                sh 'virtualenv venv && . venv/bin/activate '
            }
        }
        stage('Test') {
            steps {
                echo 'Test'
            }
        }
    }
}