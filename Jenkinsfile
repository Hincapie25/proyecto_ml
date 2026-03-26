pipeline {
    agent any

    stages {

        stage('Ejecutar Python desde contenedor manual') {
            steps {
                sh '''
                echo "Ejecutando proceso..."
                ls
                '''
            }
        }

        stage('Guardar resultados') {
            steps {
                archiveArtifacts artifacts: 'outputs/*', allowEmptyArchive: true
            }
        }
    }
}