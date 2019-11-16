from werkzeug.serving import run_simple
from app import app_factory


def run_application(port):
    run_simple(
        '0.0.0.0', port,
        app_factory.create_app(), use_reloader=True, use_debugger=True, threaded=True)

if __name__ == "__main__":
    run_application()
