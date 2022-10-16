pipeline {

    agent any
    stages {
        stage('Build') {
            agent {
                docker { image 'python:3' }
            }
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