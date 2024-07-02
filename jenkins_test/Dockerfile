FROM jenkins/jenkins

USER root

# Installez les dépendances nécessaires pour Python
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3.11-venv

# Changez l'utilisateur par défaut de Jenkins pour éviter d'exécuter Jenkins en tant qu'utilisateur root
USER jenkins