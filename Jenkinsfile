pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }

        stage('Test in Staging') {
            steps {
                script {
                    try {
                        echo 'Running tests in a new Docker container...'

                        // Pull the latest image from the registry
                        sh '''
                            docker pull mohanpoddar/jenkins-staging-agent:latest
                        '''
                        
                        // Run the Docker container, execute tests, and remove it afterward
                        sh '''
                            docker run --rm mohanpoddar/jenkins-staging-agent:latest python -m unittest discover -s tests -p "*.py"
                        '''
                    } catch (Exception e) {
                        echo "Error occurred during testing: ${e.message}"
                        currentBuild.result = 'FAILURE'  // Mark the build as failed
                    }
                }
            }
        }

        stage('Deploy to Production') {
            agent {
                label 'production'  // Ensure this runs on the production node
            }
            steps {
                script {
                    try {
                        echo 'Deploying to production...'
                        sh '''
                            export ENVIRONMENT=production
                            ./deploy.sh  // Your actual deployment script
                        '''

                        sh '''
                            echo "Waiting...."
                            sleep 240
                        '''

                    } catch (Exception e) {
                        echo "Error occurred during deployment: ${e.message}"
                        currentBuild.result = 'FAILURE'  // Mark the build as failed
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
