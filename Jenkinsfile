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
        stage('Copy docker-compose file to docker host'){
            steps{
                sh "scp -i /var/lib/jenkins/.ssh/id_rsa docker-compose.yml bobosunne@10.10.1.42:/home/bobosunne/deployment/"
            }
        }
    }
}


