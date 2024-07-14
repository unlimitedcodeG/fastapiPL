pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                script {                   // Run unit tests`
                    sh 'python -m unittest discover -s tests'
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}
