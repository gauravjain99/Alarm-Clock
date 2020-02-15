pipeline {
  agent {
    docker {
      image 'centos:latest'
      args 'ls'
    }

  }
  stages {
    stage('Example') {
      parallel {
        stage('Example') {
          input {
            message 'Should we continue?'
            id 'Yes, we should.'
            submitter 'alice,bob'
            parameters {
              string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
            }
          }
          steps {
            echo "Hello, ${PERSON}, nice to meet you."
          }
        }

        stage('test') {
          steps {
            sh 'echo "hello"'
          }
        }

      }
    }

  }
}