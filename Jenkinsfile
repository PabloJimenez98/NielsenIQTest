pipeline {

    agent none
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'test'
            }
        }
    }
}