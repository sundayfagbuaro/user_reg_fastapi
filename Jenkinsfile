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

        stage('Build Docker Image for The App'){
            steps{
                sh """
                    docker compose build 
                """
            }
        }

        stage('Push Docker Image To DockerHub') {
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'docker-cred', 
                    passwordVariable: 'docker_pass', 
                    usernameVariable: 'docker_user')]) {
                    
                    sh 'docker login -u ${docker_user} -p ${docker_pass}'
                }

                sh 'docker compose push'
            }
        }
        stage('Deploy To Docker Host') {
            steps{
                echo "Deploying App to docker Host"
                script {
                    sshagent(['docker-host-cred']) {
                    
                    sh """ssh -tt -o StrictHostKeyChecking=no bobosunne@10.10.1.42 << EOF
                        
                        docker compose up -d
                        exit

                        EOF"""
                    }
                }
                
            }
        }
    }
}
