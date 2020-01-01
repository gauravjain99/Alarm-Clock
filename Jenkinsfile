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
      }
    }
  }

  post {
      always {
          echo 'One way or another, I have finished'
          deleteDir() /* clean up our workspace */
      }
      success {
          echo 'I succeeeded!'
      }
      unstable {
          echo 'I am unstable :/'
      }
      failure {
          echo 'I failed :('
      }
      changed {
          echo 'Things were different before...'
      }
  }
}