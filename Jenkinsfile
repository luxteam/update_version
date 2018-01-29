label 'Windows'
stage "Checkout"
    node {
        checkout scm
    }
stage "Get author"
    node {
        AUTHOR_NAME = bat (
                script: "git show -s --format='%%an' HEAD",
                returnStdout: true
                ).split('\r\n')[2].trim()
    
    echo "The last commit was written by ${AUTHOR_NAME}."
    echo AUTHOR_NAME
    }
stage "Update version"
    node {
        if (AUTHOR_NAME != 'epozine') {
            bat """
                ls
                cd update_version
                set PATH=c:\\python35\\;c:\\python35\\scripts\\;%PATH%
                python update.py--file "vesion.h"
               """
        }
        else {
            echo "no new commits"
        }
    }

