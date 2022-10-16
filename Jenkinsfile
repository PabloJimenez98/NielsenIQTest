pipeline {

    agent any
    stages {
        stage('Build') {
            steps {
                 sh 'virtualenv venv && . venv/Scripts/activate && pip install -r requirements.txt '
            }
        }
        stage('Test') {
            steps {
                sh 'python test_exists.py'
                sh 'python test_metrics.py'
            }
        }
    }
}