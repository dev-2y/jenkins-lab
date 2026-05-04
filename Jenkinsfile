pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Construindo a imagem da aplicação...'
                    dockerImage = docker.build("lab-app:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Teste') {
            steps {
                echo 'Executando testes básicos...'
                sh 'docker run --rm lab-app:${env.BUILD_NUMBER} python --version'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Simulando deploy...'
                sh 'docker run --rm lab-app:${env.BUILD_NUMBER}'
            }
        }
    }
}
