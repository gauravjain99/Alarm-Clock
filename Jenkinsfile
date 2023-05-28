def scannerHome = tool name: 'SonarScanner'

pipeline {
    agent any
    stages {
        stage('SCM') {
            steps {
                git url: 'https://github.com/gauravjain99/Alarm-Clock'
            }
        }
        stage('build && SonarQube analysis') {
            steps {
                withSonarQubeEnv('gaurav-sonar') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
