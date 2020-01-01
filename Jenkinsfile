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
          deleteDir()
      }
      success {
          echo 'This will run only if successful'
      }
      failure {
          echo 'This will run only if failed'
      }
      unstable {
          echo 'This will run only if the run was marked as unstable'
      }
      changed {
          echo 'This will run only if the state of the Pipeline has changed'
          echo 'For example, if the Pipeline was previously failing but is now successful'
      }
  }
}