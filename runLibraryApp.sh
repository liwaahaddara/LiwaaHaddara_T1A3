
# ask if there is one parameter and if that parameter is equals to help
#!/bin/bash
if [ $# -eq 1 ] && [ $1 == "help" ]
then
    #print the help file
    cat libraryHelp.txt
else
    #run the app
    python3 library.py
fi

# to run the script:
# ./runLibrary.sh


# to run the help file:
# ./runLibrary.sh help