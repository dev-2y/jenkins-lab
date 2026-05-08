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
                sh 'docker compose build --no-cache'
            }
        }

        stage('Start Services') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Check Containers') {
            steps {
                sh 'docker compose ps'
                sh 'docker ps -a'
                sh 'docker compose logs --no-color app || true'
                sh 'docker inspect jenkins-lab-app || true'
            }
        }

        stage('Wait DB') {
            steps {
                sh 'docker compose exec -T db pg_isready -U app_user -d app_db'
            }
        }

        stage('Integration Test') {
            steps {
		echo 'Executando teste apenas se a app estiver rodando...'
        	sh '''docker compose exec -T app python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5000/').read().decode())"'''
            }
        }
    }

    post {
        always {
            sh 'docker compose logs --no-color || true'
            sh 'docker compose down -v || true'
        }
    }
}
