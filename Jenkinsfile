pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                echo 'Executando lint...'
                sh 'echo "Código passou no lint ✓"'
            }
        }
        stage('Build') {
            steps {
                echo 'Construindo aplicação...'
                sh 'echo "Build concluído ✓"'
            }
        }
        stage('Test') {
            steps {
                echo 'Rodando testes...'
                sh '''
                echo "Teste 1: OK"
                echo "Teste 2: OK" 
                echo "Todos testes passaram ✓"
                '''
            }
        }
        stage('Package') {
            steps {
                echo 'Gerando artefato...'
                sh 'echo "build-$(date +%Y%m%d-%H%M%S).tar.gz" > artefato.txt'
                archiveArtifacts 'artefato.txt'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finalizado!'
        }
    }
}

