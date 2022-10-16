pipeline {

    agent any
    stages {
        stage('Build') {
            steps {
                if (fileExists('requirements.txt')) {
                    sh """
                    . .env/bin/activate
                    pip3 install -r requirements.txt
                    """
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