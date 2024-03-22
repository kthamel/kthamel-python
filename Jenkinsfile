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

        stage('Demo Data Structures') {
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

        stage('Demo Data Types') {
            steps {
                sh '''
                    python demo-data-types/data-types.py
                '''
            }
        }

        stage('Demo Error Handling') {
            steps {
                sh '''
                    python demo-error-handling/custom_exceptions.py
                    python demo-error-handling/exceptions.py
                '''
            }
        }
    }
}