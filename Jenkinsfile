pipeline {
  agent {
    docker {
      image 'python:3.5.1'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'python --version'
        retry(3){
          sh "chmod +x app.py"
          sh "./app.py"
        }
      }
    }

  }
}