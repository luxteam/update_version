node ("Windows && Builder")
{
    stage "Checkout"
    checkout scm

    stage "Get author"
    
    AUTHOR_NAME = bat (
            script: "git show -s --format='%%an' HEAD ",
            returnStdout: true
            ).split('\r\n')[2].trim()

    echo "The last commit was written by ${AUTHOR_NAME}."
    
    stage "Update version"
    
    if (AUTHOR_NAME != "'radeonprorender'") {
        OLD_VERSION = bat (
            script: """set PATH=c:\\python35\\;c:\\python35\\scripts\\;%PATH%
                       python version_read.py --file init.py  --prefix "'version': (" --delimiter ", "  """,
            returnStdout: true
            ).split('\r\n')[4].trim()
        echo OLD_VERSION
        
        NEW_VERSION = bat (
            script: """set PATH=c:\\python35\\;c:\\python35\\scripts\\;%PATH%
                       python version_inc.py --version "${OLD_VERSION}" --index 3 --delimiter ", "   """,
            returnStdout: true
            ).split('\r\n')[4].trim()
        echo NEW_VERSION
        bat """         
            set PATH=c:\\python35\\;c:\\python35\\scripts\\;%PATH%
            python version_write.py --file init.py --prefix ""version": (" --version ${NEW_VERSION} --delimiter ", "
            git add version.h
            git commit -m "Update version build"
            git push origin HEAD:master
           """
    }
    else {
        echo "Last commit was made by radeonprorender."
    }
}

