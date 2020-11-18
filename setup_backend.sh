#!/bin/bash

ERROR_COUNT=0

# Sets up colors of text
setup_color() {
	if [ -t 1 ]; then
		RED=$(printf '\033[31m')
		GREEN=$(printf '\033[32m')
		YELLOW=$(printf '\033[33m')
		BLUE=$(printf '\033[34m')
		RESET=$(printf '\033[m')
	else
		RED=""
		GREEN=""
		YELLOW=""
		BLUE=""
		RESET=""
	fi
}

# Error handler, $1 is success message, $2 is error message
handle_errors() {
    if [ $? -eq 0 ]; then
        echo -e $1
    else
        echo -e $2
        let "ERROR_COUNT+=1"
    fi
}

display_start_message() {
    echo -e "$BLUE>>>> Starting app setup... <<<<$RESET"
}

setup_python_venv() {
    python3 -m venv backend/venv && source backend/venv/bin/activate

    handle_errors "$GREEN>>>> Python3 virtualenv created successfully. <<<<$RESET" "$RED>>>> Error while creating Python3 virtualenv. <<<<$RESET"
}

install_requirements() {
    pip3 install -r backend/requirements.txt

    handle_errors "$GREEN>>>> Python requirements installed successfully with Pip. <<<<$RESET" "$RED>>>> Error while installing requirements from requirements.txt <<<<$RESET"
}

generate_django_secret_key() {
    cd backend/backend/scripts/
    python3 keygen.py

    handle_errors "$GREEN>>>> Django SECRET_KEY generated successfully. <<<<$RESET" "$RED>>>> Error while generating Django SECRET_KEY <<<<$RESET"

    cd ../../../

    echo "# Django secret key" >> .gitignore
    echo "secrets.py" >> .gitignore
   
    handle_errors "$GREEN>>>> Django SECRET_KEY added to git-ignored files. <<<<$RESET" "$RED>>>> Error while adding SECRET_KEY to git-ignored files. <<<<$RESET"
}

setup_database() {
    python3 backend/manage.py makemigrations && python3 backend/manage.py migrate

    handle_errors "$GREEN>>>> Database constructed, migrations applied. <<<<$RESET" "$RED>>>> Error while constructing database. <<<<$RESET"
}

check_if_setup_succedeed() {
    if [ $ERROR_COUNT -eq 0 ]; then
        echo -e "$GREEN>>>> *** Setup done. *** <<<< $RESET"
    else
        echo -e "$RED>>>> Setup failed. $ERROR_COUNT errors occured. <<<<$RESET"
    fi
}


# Main function
setup_backend() {
    setup_color
    display_start_message
    setup_python_venv
    install_requirements
    generate_django_secret_key
    setup_database
    check_if_setup_succedeed
}

setup_backend