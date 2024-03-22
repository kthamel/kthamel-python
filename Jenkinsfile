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

        stage('Demo Comprehension') {
            steps {
                sh '''
                    python demo-comprehension/comprehension.py
                '''
            }
        }

        stage('Demo Conditions') {
            steps {
                sh '''
                    python demo-conditions/conditional-statement.py
                '''
            }
        }

        stage('Demo Conditions') {
            steps {
                sh '''
                    python demo-data-structures/dictionary.py
                    python demo-data-structures/list.py
                    python demo-data-structures/sets.py
                    python demo-data-structures/slicing.py
                    python demo-data-structures/tuple.py
                '''
            }
        }
    }
}