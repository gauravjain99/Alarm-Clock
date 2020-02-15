pipeline {
  agent {
    docker {
      image 'centos:latest'
    }

  }
  stages {
    stage('test') {
      steps {
        sh 'echo "hello"'
      }
    }

  }
}