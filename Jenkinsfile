pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {

        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar modelo') {
            steps {
                sh 'python src/main.py'
            }
        }

        stage('Guardar resultados') {
            steps {
                archiveArtifacts artifacts: 'outputs/*'
            }
        }
    }
}