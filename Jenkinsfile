agent {
        label 'Windows'
    }
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
                set PATH=c:\\python35\\;c:\\python35\\scripts\\;%PATH%
                python update.py --file "version.h"
                git add version.h
                git commit -m "Update version build"
                git push origin HEAD:master --force

               """
        }
        else {
            echo "no new commits"
        }
    }

