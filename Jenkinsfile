//noinspection GroovyAssignabilityCheck
pipeline {
    agent any

    parameters {
        booleanParam(name: 'buildImages', defaultValue: true, description: 'Build images')
        string(name: 'VERSION', defaultValue: '1', description: 'image version'),
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

        stage('Build images') {
            when { expression { params.buildImages } }
            steps {
                sh './build.sh'
            }
        }

        stage('Push images') {
            when { expression { params.buildImages } }
            steps {
                sh './build.sh push'
            }
        }

        stage('Deploy to staging') {
            when { expression { BRANCH_NAME == 'master' && params.deployToStaging } }
            agent { label 'staging' } // Execute on staging slave (connected to staging Kubernetes cluster)
            steps {
                script {
                    deploy "staging", "staging"
                }
            }
        }

        stage('Deploy to automation') {
            when { expression { BRANCH_NAME == 'master' && params.deployToAutomation } }
            agent { label 'staging' } // Execute on staging slave (connected to staging Kubernetes cluster)
            steps {
                script {
                    deploy "staging", "automation"
                }
            }
        }

        stage('Deploy to demo') {
            when { expression { BRANCH_NAME == 'master' && (params.deployToDemo || params.deployToDemoAndProd) } }
            agent { label 'staging' } // Execute on staging slave (connected to staging Kubernetes cluster)
            steps {
                script {
                    deploy "staging", "demo"
                }
            }
        }

        stage('Deploy to prod') {
            when { expression { BRANCH_NAME == 'master' && (params.deployToProd || params.deployToDemoAndProd) } }
            agent { label 'build' } // Execute on master (connected to prod Kubernetes cluster)
            steps {
                script {
                    deploy "prod", "prod"
                }
            }
        }

    }
}

def deploy(context, namespace) {
    echo "Going to deploy version $GIT_COMMIT"
    echo "Deploying to Kubernetes context: $context, namespace: $namespace"

    sh """
        BUILD_CONTEXT=$context \
        BUILD_NAMESPACE=$namespace \
        BUILD_TAG=$GIT_COMMIT \
        BUILD_DEBUG=$params.debug \
        ./deploy.sh
        """
}
