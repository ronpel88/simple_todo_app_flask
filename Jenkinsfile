//noinspection GroovyAssignabilityCheck
pipeline {
    agent any

    parameters {
        string(name: 'VERSION', defaultValue: '1', description: 'image version')
        string(name: 'IMAGE_NAME', defaultValue: 'simple_todo_app_flask', description: 'base image name')
    }


    options {
        disableConcurrentBuilds()
        timestamps()
    }

    environment {
        GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
    }

    stages {

        stage('echo ron') {
            steps {
                sh 'echo "OMRIKI"'
            }
        }

        stage('Build image') {
            steps {
                sh 'scripts/build.sh build ${params.IMAGE_NAME}'
            }
        }

        stage('Tag image') {
            steps {
                sh 'scripts/build.sh tag ${params.IMAGE_NAME} ${params.REPO_NAME} ${params.VERSION} ${params.COMMIT_ID}'
            }
        }

        stage('Push image') {
            steps {
                sh 'scripts/build.sh push ${params.IMAGE_NAME} ${params.REPO_NAME} ${params.VERSION} ${params.COMMIT_ID}'
            }
        }

    }
}