from app.app import create_app


def test_list_routes():
    """Vérifie si `/auth/token` est bien enregistré."""
    app = create_app()
    routes = [str(rule) for rule in app.url_map.iter_rules()]

    assert "/auth/token" in routes, f" Route `/auth/token` manquante ! Routes actuelles: {routes}"
