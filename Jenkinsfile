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
                sh 'docker compose exec -T db pg_isready -U app_user -d app_db'
            }
        }

        stage('Check App') {
            steps {
                echo 'Verificando status da aplicação...'
                sh 'docker compose ps'
                sh 'docker compose logs --no-color app || true'
                sh 'docker compose ps app'
            }
        }

        stage('Integration Test') {
            steps {
                echo 'Executando teste apenas se a app estiver rodando...'
                sh 'docker compose exec -T app python -c "import urllib.request; print(urllib.request.urlopen(\'http://127.0.0.1:5000/\').read().decode())"'
            }
        }
    }

    post {
        always {
            echo 'Logs finais dos serviços...'
            sh 'docker compose logs --no-color || true'
            echo 'Limpando ambiente...'
            sh 'docker compose down -v || true'
        }
    }
}
