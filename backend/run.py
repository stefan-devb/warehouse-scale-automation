#!/usr/bin/env python3
"""
Safe entrypoint for Flask app.

Behavior controlled by environment variables:
- APP_ENV: "development" or "production" (default: "development")
- FLASK_DEBUG: "1"/"true" to enable debug in development only
- PORT: port to bind (default: 5001)
"""
import os
import sys
from app import create_app

def main():
    app = create_app()

    env = os.getenv("APP_ENV", "development").lower()
    port = int(os.getenv("PORT", "5001"))
    # debug flag: only enabled automatically in development
    debug_env = os.getenv("FLASK_DEBUG", "0").lower() in ("1", "true", "yes")

    if env == "development":
        host = "0.0.0.0"
        debug = True if debug_env else False
        print(f"[run] Running in development mode. host={host} port={port} debug={debug}")
    else:
        # production: bind to localhost only and force debug off
        host = "127.0.0.1"
        if debug_env:
            # Do not allow debug in production — override and warn
            print("[run] WARNING: FLASK_DEBUG is set but APP_ENV=production — overriding debug=False for safety", file=sys.stderr)
        debug = False
        print(f"[run] Running in PRODUCTION mode. host={host} port={port} (use gunicorn/nginx in production)")

    # Run built-in dev server only for development / local testing.
    # For production use gunicorn behind a reverse proxy (nginx) binding to 127.0.0.1
    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    main()
