pipeline{
    agent {
        docker { image 'python:latest'}
    }

    stages{
        stage('Test'){
            steps{
                sh 'python --version'
            }
        }
    }
}