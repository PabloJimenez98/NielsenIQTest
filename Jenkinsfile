pipeline {

    agent any
    stages {
        stage('Build') {
            steps {
                 withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Test'
            }
        }
    }
}