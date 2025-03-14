pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/dzvinochok/--------' 
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
