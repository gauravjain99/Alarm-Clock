pipeline{
    agent none

    stages{
        stage('Test'){
            agent{
                docker { image 'ubuntu:latest'}
            }
            steps{
                sh 'cat /etc/os_release'
            }
        }

        stage ('build'){
            agent {
                docker{ image 'centos:latest'}
            }
            steps{
                sh 'cat  /etc/os_release'
            }
        }
    }
}