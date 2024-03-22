pipeline {
    agent {label 'ansible'}
    stages {
        stage('Check Versions') {
            steps {
                sh '''
                    python --version
                '''
            }
        }

        stage('Demo Comments') {
            steps {
                sh '''
                    python demo-comments/comments.py
                '''
            }
        }

        stage('Check Versions') {
            steps {
                sh '''
                    python --version
                '''
            }
        }
    }
}