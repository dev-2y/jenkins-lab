pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 25, unit: 'MINUTES')
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
                echo 'Build dos serviços...'
                sh 'docker compose build'
            }
        }

        stage('Start Services') {
            steps {
                echo 'Subindo banco e app...'
                sh 'docker compose up -d'
            }
        }

        stage('Wait DB') {
            steps {
                echo 'Aguardando o PostgreSQL ficar pronto...'
                sh 'docker compose ps'
                sh 'docker compose exec -T db pg_isready -U app_user -d app_db'
            }
        }

        stage('Integration Test') {
            steps {
                echo 'Testando app + banco na rede do Compose...'
                sh 'docker run --rm --network ${COMPOSE_PROJECT_NAME}_default curlimages/curl:8.10.1 curl -fsS http://app:5000/'
            }
        }

        stage('Logs') {
            steps {
                echo 'Coletando logs...'
                sh 'docker compose logs --no-color'
            }
        }
    }

    post {
        always {
            echo 'Limpando ambiente...'
            sh 'docker compose down -v || true'
        }
    }
}
