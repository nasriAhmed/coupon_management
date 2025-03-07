from app.models.config_base import db
from app.models.coupon import Coupon


def remplir_base():
    """Ajoute des coupons à la base de données."""
    coupons = [
        {"name": "BLACKFRIDAY", "discount": 30,
            "condition": "Minimum 50€ d'achat"},
        {"name": "WELCOME10", "discount": 10,
            "condition": "Pour les nouveaux clients"},
        {"name": "FREESHIP", "discount": 100,
            "condition": "Livraison gratuite sur toutes les commandes"},
        {"name": "SUMMER20", "discount": 20,
            "condition": "Offre estivale, valable jusqu'au 31 août"},
        {"name": "VIP15", "discount": 15,
            "condition": "Offre réservée aux membres VIP"}
    ]

    if db is None:
        print("Erreur : Impossible de se connecter à la base de données.")
        return

    for coupon in coupons:
        # Vérifie si le coupon existe déjà
        if not Coupon.get_coupon(coupon["name"]):
            Coupon.add_coupon(
                coupon["name"], coupon["discount"], coupon["condition"])
            print(f"Coupon ajouté : {coupon['name']}")
        else:
            print(f"Coupon déjà existant : {coupon['name']}")


if __name__ == "__main__":
    remplir_base()
