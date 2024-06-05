pipeline {

    agent { label 'jenkins-worker' }

    environment {
        customTag = "$BUILD_NUMBER-$GIT_HASH"
        repo = "vault-creds-updater"
        ecr = "795145148370.dkr.ecr.eu-central-1.amazonaws.com"
        region = "eu-central-1"
        accountId = "partida-ecr-user"
        tag = "latest"

        GIT_HASH = sh(
            script: "printf \$(git rev-parse --short ${GIT_COMMIT})",
            returnStdout: true
        )
    }

    stages {
        stage('Build image') {
            steps {
                script {
                    println("Building image...")
                    // Set current build name
                    currentBuild.displayName = "#${tag}"
                    dockerImage = docker.build(repo +':' + tag, " -f Dockerfile .")
                }
            }
        }

        stage('Pushing to ECR') {
            steps{
                script {
                    timeout(time: 15, unit: "MINUTES") {
	                    input message: 'Do you want to push image to ECR?', ok: 'Yes'
	                }
                    println('Pushing image to aws ecr...')
                    docker.withRegistry("https://$ecr","ecr:$region:$accountId") {
                        println "Docker image: $dockerImage.id"
                        dockerImage.push()
                    }
                }
            }
        }
    }
}