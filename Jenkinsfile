node { 
    stage("Checkout repo") { 
        dir("repo") {
        git branch: '${BRANCH_NAME}',
            credentialsId: 'GitlabToken',
            url: 'https://gitlab-pub.yadro.com/devops-school-2024/student/a.karimullin.git'
        }
    }

    stage('Build docker image') {
        dir("repo") { 
            withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'HUB_PASSWORD', usernameVariable: 'HUB_USERNAME')]) {
                sh("buildah bud --tag ${HUB_USERNAME}/cbr:latest -f ./Dockerfile .")
                }
                
            }
        }

    stage("Run python tests") {
        dir("repo"){
            sh('python3 -m venv env)
            sh('source env/bin/activate')
            sh('pip install -r requirements.txt')
        }

        dir("repo/src"){
            sh('ln -s ../tests/test_*')
            sh('pytest')
            sh('rm test_*')
        }
            
    }
    
    stage("Push docker image to docker hub") {
        dir("repo") {
            withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'HUB_PASSWORD', usernameVariable: 'HUB_USERNAME')]) {
            sh """
                buildah login -u ${HUB_USERNAME} -p ${HUB_PASSWORD} docker.io
                buildah push ${HUB_USERNAME}/cbr:latest
                buildah logout docker.io
                """
            }
        }
    }
}
