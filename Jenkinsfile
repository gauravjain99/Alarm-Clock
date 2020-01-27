 #!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        /* "Build" and "Test" stages omitted */

        stage('Deploy - Staging') {
            steps {
                sh 'ls'
                sh 'echo me'
            }
        }

        stage('Deploy - Production') {
            steps {
                sh 'ls'
            }
        }
    }
}