label 'Windows'
stage "Checkout"
    node {
        checkout scm
    }
stage "Update version"
    node {
        AUTHOR_NAME = bat (
                script: "git show -s --format='%%an' HEAD",
                returnStdout: true
                ).split('\r\n')[2].trim()

    echo "The last commit was written by ${AUTHOR_NAME}."
    }
stage "Update version"
    node {
        set PATH=c:\\python35\\;c:\\python35\\scripts\\;%PATH%
        bat 'python --file "vesion.h" '
    }

stage "Commit changes"
    node {
        echo "Done"
    }
