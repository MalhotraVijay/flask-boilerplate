#!/usr/bin/env groovy

node {
  try {
      properties([
          parameters([
                  booleanParam(
                          defaultValue: false,
                          description: 'Run setup',
                          name: 'run_setup'),
          ])])
      stage('Build') {
          try {
              sh '''#!/bin/bash
                echo hello $(env.BRANCH_NAME)
              '''
              if($(env.BRANCH_NAME == "master"){
                sh '''
                    echo I am performing further
                ''''
              }
          } catch (exc) {
              echo "Error when waiting for user input to promote to production. ${exc}"
              throw exc
          }
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