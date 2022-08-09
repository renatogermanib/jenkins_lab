pipeline {
    agent any

    stages {
        stage('docker build') {
            steps {
                script {
                    sh "docker build -t germanib/primer-pipeline:1.0.0-${BUILD_ID} ."
                }
            }
        }
        stage('docker push') {
            steps {
                script {
                    sh "docker push germanib/primer-pipeline:1.0.0-${BUILD_ID}"
                    //sh "docker"
                }
            }
        }
    }
}
