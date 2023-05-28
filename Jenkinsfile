def scannerHome = tool 'SonarScanner';

pipeline {
    agent any
    stages {
        stage('SCM') {
            steps {
                sh 'echo "hello"'
            }
        }
        stage('build && SonarQube analysis') {
            steps {
                withSonarQubeEnv('gaurav-sonar') {
                    // Optionally use a Maven environment you've configured already
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
