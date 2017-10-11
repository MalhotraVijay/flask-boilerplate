#!/usr/bin/env groovy

node {
    try {
        properties([
                parameters([
                    booleanParam(
                        defaultValue: false,
                        description: 'Run setup',
                        name: 'run_setup'),
                    booleanParam(
                        defaultValue: false,
                        description: 'Build Image Only',
                        name: 'build_image_only')
                ])])
            def build_image_only = params["build_image_only"] ? "true" : ""
            stage('Build') {
                try {
                    sh '''#!/bin/bash
                        echo hello
                        '''
                        echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL} with ${env.BRANCH_NAME} "
                        script{
                            if(env.BRANCH_NAME == "master"){
                                sh '''
                                    echo I am performing further
                                    '''
                            }
                        }
                } catch (exc) {
                    echo "Error when waiting for user input to promote to production. ${exc}"
                        throw exc
                }
            }

        if(build_image_only){
            echo "Building only image and now exiting"
            currentBuild.result = 'SUCCESS'
            return
        }

        if(env.BRANCH_NAME != "master"){
            echo "Found branch ${env.BRANCH_NAME}  here and exiting after build"
                currentBuild.result = 'SUCCESS'
                return
        }

        stage('Test'){
            try{
                echo "In the test branch"
            }catch (exc){
                echo "Error in Job, ${exc}"
                    throw exc
            }
        }
    } catch (exc) {
        echo "Error in Job. ${exc}"
            throw exc
    }
}
