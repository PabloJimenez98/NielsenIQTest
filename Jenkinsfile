pipeline {

    agent any
    stages {
        stage('Build') {
            steps {
                 bat 'pip install virtualenv && virtualenv venv && . venv/Scripts/activate && pip install -r requirements.txt '
            }
        }
        stage('Test') {
            steps {
                echo 'Test'
            }
        }
    }
}