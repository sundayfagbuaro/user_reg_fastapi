pipeline {
    agent any

    stages {
        stage('SCM Checkout') {
            steps {
                script {
                    git branch: 'docker_compose', credentialsId: 'git-pat', url: 'https://github.com/sundayfagbuaro/user_reg_fastapi.git'
                
                }
            }
        }
    }
}


