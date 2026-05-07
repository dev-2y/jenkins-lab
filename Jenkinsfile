pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 20, unit: 'MINUTES')
    }

    environment {
        COMPOSE_PROJECT_NAME = "jenkins-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build da imagem com Docker Compose...'
                sh 'docker compose build'
            }
        }

        stage('Start Services') {
            steps {
                echo 'Subindo os serviços...'
                sh 'docker compose up -d'
            }
        }

        stage('Smoke Test') {
            steps {
                echo 'Validando a aplicação...'
		sh 'docker compose up -d --wait || docker compose up -d'
        	sh 'docker compose ps'
                sh 'curl -fsS http://127.0.0.1:5000/'
            }
        }

        stage('Logs') {
            steps {
                echo 'Coletando logs do serviço...'
                sh 'docker compose logs --no-color'
            }
        }
    }

    post {
        always {
            echo 'Removendo os serviços...'
            sh 'docker compose down -v || true'
        }
    }
}
