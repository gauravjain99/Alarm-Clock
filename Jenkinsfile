pipeline{
    agent none

    stages{
        stage('Test'){
            agent{
                docker { image 'ubuntu:latest'}
            }
            steps{
                sh 'uname -a'
            }
        }

        stage ('build'){
            agent {
                docker{ image 'centos:latest'}
            }
            steps{
                sh 'uname -a'
            }
        }
    }
}