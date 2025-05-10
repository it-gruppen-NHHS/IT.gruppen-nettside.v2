#!/bin/bash
echo "Enter the name of the app, note that the name will be used as the navbar brand: " 
read name

echo "Generating secret app key"
key=$(openssl rand -hex 24)

echo "Generated Key: $key"

# Path to the Python file
python_file="app/config.py"
# Replace the key in the Python file
sed -i "s/s_key/$key/" "$python_file"
echo "Secret key generated"
# Path to the encryption file
cd app
encryption_file="encryption.py"
# Generate the encrypted key
echo "Genereting encryption key"
sed -i "s/#generate_key()/generate_key()/" "$encryption_file"
echo "Test verdi" | python $encryption_file 
sed -i "s/generate_key()/#generate_key()/" "$encryption_file"
echo "Encryption key generated"

echo "Setting the navbar brand name"
cd templates
template_file="template.html"
sed -i "s/ProsjektNavn/$name/" "$template_file"

echo "Navbar brand name set"
cd ..
python app.py 
