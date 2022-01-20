# Installation
pip install --user ansible molecule[docker] pytest-testinfra pytest
pip install pytest-testinfra
# Initialisation
 molecule init role role_testinfra_verifier --driver-name docker

# Testinfra
https://testinfra.readthedocs.io/en/latest/modules.html
