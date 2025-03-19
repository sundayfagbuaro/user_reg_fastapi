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
                    docker build -t fastapi_custom_img .
                    docker tag fastapi_custom_img sundayfagbuaro/fastapi_custom_img:v1
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

                sh 'docker push sundayfagbuaro/fastapi_custom_img:v1'
            }
        }
        stage('Copy docker-compose file to docker host'){
            steps{
                sh "scp -i /var/lib/jenkins/.ssh/id_rsa docker-compose.yml bobosunne@10.10.1.42:/home/bobosunne/deployment/"
            }
        }
        stage('Deploy To Docker Host') {
            steps{  
                script{  
                    sshagent(['docker-host-cred']) {
                    sh """
                    ssh -tt -o StrictHostKeyChecking=no bobosunne@10.10.1.42 << EOF
                    cd deployment
                    docker compose up -d
                    docker compose ps
                    
                    """
                    }           
                }
            }
        }
    }
}
