# views.py
import subprocess
import json
from django.shortcuts import render

def get_docker_status():
    """Получение статуса контейнеров через docker-compose ps --format json"""
    try:
        result = subprocess.run(
            ['docker-compose', 'ps', '--format', 'json'],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            containers = json.loads(result.stdout)
            return containers
    except:
        pass
    return []

def home(request):
    containers = get_docker_status()
    
    context = {
        'containers': containers,
        'docker_available': len(containers) > 0
    }
    
    return render(request, 'visitka/index.html', context)
