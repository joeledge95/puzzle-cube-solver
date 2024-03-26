# Activate the virtual environment
source venv/bin/activate

# Ask for the package name to install
echo "Please enter the package name that you want to install:"
read -p "Package Name: " PackageName

# Install the package with pip
pip install $PackageName

# Wait for user input before closing
read -p "Press any key to continue . . . " -n1 -s
echo
