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
                echo hello
              '''
          } catch (exc) {
              echo "Error when waiting for user input to promote to production. ${exc}"
              throw exc
          }
      }
  } catch (exc) {
      echo "Error in Job. ${exc}"
      throw exc
  }
}
