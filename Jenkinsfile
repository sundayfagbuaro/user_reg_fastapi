pipeline {
    agent any

    stages {
        stage('SCM Checkout') {
            steps {
                script {
                    git branch: 'k8_deploy_test', credentialsId: 'git_cred', url: 'https://github.com/sundayfagbuaro/user_reg_fastapi.git'
                
                }
            }
        }
        stage('Build docker image for fastapi'){
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
                    credentialsId: 'docker-hub-cred', 
                    passwordVariable: 'docker_pass', 
                    usernameVariable: 'docker_user')]) {
                    
                sh 'docker login -u ${docker_user} -p ${docker_pass}'
                }

                sh 'docker push sundayfagbuaro/fastapi_custom_img:v1'
            }
        }
        stage('Deploy the pods') {
            steps{
                echo "Deploying Pods to K8s Cluster"
                script{
                    withKubeCredentials(kubectlCredentials: [[caCertificate: '', clusterName: '', contextName: '', credentialsId: 'k8s-credentials', namespace: 'default', serverUrl: 'https://192.168.1.94:6443']]) {
                        sh 'kubectl apply -f deployment_files/postgres/config_secret_storage.yml'
                        sh 'kubectl apply -f deployment_files/postgres/svc_deployment.yml'
                    }
                }

            }
        }
    }
}


