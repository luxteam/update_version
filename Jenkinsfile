node ("Deploy")
{
    stage "Checkout"
    checkout scm

    stage "Get author"
    
    AUTHOR_NAME = bat (
            script: "git show -s --format='%%an' HEAD",
            returnStdout: true
            ).split('\r\n')[2].trim()

    echo "The last commit was written by ${AUTHOR_NAME}."
    
    stage "Update version"
    
    if (AUTHOR_NAME != "'radeonprorender'") {
        OLD_VERSION = bat (
            script: """set PATH=c:\\python35\\;c:\\python35\\scripts\\;%PATH%
                       python read_version.py --file version.h --prefix "#define version_build" """,
            returnStdout: true
            )
        NEW_VERSION = bat (
            script: """set PATH=c:\\python35\\;c:\\python35\\scripts\\;%PATH%
                       python inc_version.py --version ${VERSION} """,
            returnStdout: true
            )
        bat """         
            set PATH=c:\\python35\\;c:\\python35\\scripts\\;%PATH%
            python write_version.py --file version.h --prefix "#define version_build" --version ${NEW_VERSION}
            git add version.h
            git commit -m "Update version build"
            git push origin HEAD:master --force
           """
    }
    else {
        echo "Last commit was made by radeonprorender."
    }
}

