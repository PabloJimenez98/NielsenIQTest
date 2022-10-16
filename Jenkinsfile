pipeline {

    agent any
    stages {
        stage('Build') {
            steps {
                 bat 'virtualenv venv && . venv/Scripts/activate && pip install -r requirements.txt '
            }
        }
        stage('Test') {
            steps {
                echo 'Test'
            }
        }
    }
}